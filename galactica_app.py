# -*- coding: UTF-8 -*-

from flask import Flask, request, make_response, Response
from slackeventsapi import SlackEventAdapter
from bot import Bot
import json

# ------------------------------------------------------------------------
# GET KEYS
with open("keys.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]
f.close() 

SLACK_SIGNING_SECRET = content[0].split(" ")[1] 
SLACK_BOT_TOKEN = content[1].split(" ")[1]  
SLACK_VERIFICATION_TOKEN = content[2].split(" ")[1]
FIXER_API_KEY =  content[3].split(" ")[1]


app = Flask(__name__)

slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app) # bind the event api

sapsikbirbot = Bot(SLACK_BOT_TOKEN) # create bot

# ------------------------------------------------------------------------

# ***** SLACK EVENT API METHODS *****

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    #Filter out messages from this bot itself or updates to messages
    if event_data.get("subtype") is 'bot_message' or event_data.get("subtype") is 'message_changed':
        return
    sapsikbirbot.handleDirectMessage(event_data["event"])
  
# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    sapsikbirbot.reactionAdded(event_data["event"])
    
# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# ***** SERVER ROUTE METHODS for Interactive Components *****

@app.route("/")
def hello():
    # An example of one of your Flask app's routes
    return "Hello there!"

@app.route("/slack/message_actions", methods=["POST"])
def message_actions():
    # Parse the request payload
    payload = request.form["payload"]
    form_json = json.loads(payload)

    # Verify that the request came from Slack
    verify_slack_token(form_json["token"])

    if form_json["actions"][0]['type'] == 'select':
        sapsikbirbot.select_message_action(form_json)
    elif form_json["actions"][0]['type'] == 'button':
        sapsikbirbot.button_message_action(form_json)

    # Send an HTTP 200 response with empty body so Slack knows we're done here
    return make_response("", 200)

# ------------------------------------------------------------------------

# HELPER FUNCTIONS

def verify_slack_token(request_token):
    if SLACK_VERIFICATION_TOKEN != request_token:
        print("Error: invalid verification token!")
        print("Received {} but was expecting {}".format(request_token, SLACK_VERIFICATION_TOKEN))
        return make_response("Request contains invalid Slack verification token", 403)

# ------------------------------------------------------------------------

# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)