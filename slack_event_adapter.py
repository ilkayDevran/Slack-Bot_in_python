# -*- coding: UTF-8 -*-

from flask import Flask, request, make_response, Response
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import json

import attachments


global orders
global USER_ID
global text
orders = []
USER_ID = ""
text = ""

with open("keys.txt", "r") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
f.close() 

SLACK_SIGNING_SECRET = content[0].split(" ")[1] 
SLACK_BOT_TOKEN = content[1].split(" ")[1]  
SLACK_VERIFICATION_TOKEN = content[2].split(" ")[1] 


# This `app` represents your existing Flask app
# Flask webserver for incoming traffic from Slack
app = Flask(__name__)


# Bind the Events API route to your existing Flask app by passing the server
# instance as the last param, or with `server=app`.
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events", app)

# Slack client for Web API requests
slack_client = SlackClient(SLACK_BOT_TOKEN)


# Helper for verifying that requests came from Slack
def verify_slack_token(request_token):
    if SLACK_VERIFICATION_TOKEN != request_token:
        print("Error: invalid verification token!")
        print("Received {} but was expecting {}".format(request_token, SLACK_VERIFICATION_TOKEN))
        return make_response("Request contains invalid Slack verification token", 403)


# An example of one of your Flask app's routes
@app.route("/")
def hello():
    return "Hello there!"



""" ### Slack Event API Funtions ### """

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    message = event_data["event"]
    decideWhat2Do(message)

# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.api_call("chat.postMessage", channel=channel, text=text)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))




""" ### Flask Route Functions for Interactive Components ### """

# The endpoint Slack will send the user's menu selection to
@app.route("/slack/message_actions", methods=["POST"])
def message_actions():
    global orders, text, USER_ID
    # Parse the request payload
    payload = request.form["payload"]
    form_json = json.loads(payload)

    # Verify that the request came from Slack
    verify_slack_token(form_json["token"])

    if form_json["actions"][0]['type'] == 'select':
        select_message_action(form_json)
    elif form_json["actions"][0]['type'] == 'button':
        button_message_action(form_json)



    # Send an HTTP 200 response with empty body so Slack knows we're done here
    return make_response("", 200)



# My Helper Functions
def get_message_according_to_selection(selection):
    if selection == "hurriyet":
        return "Hürriyet"
    elif selection == "milliyet":
        return "Milliyet"
    elif selection == "kelebek":
        return "Kelebek"
    elif selection == "pageviews":
        return "Page View"
    elif selection == "user":
        return "User"
    elif selection == "today":
        return "Today"
    elif selection == "yesterday":
        return "Today"
    else:
        return

def decideWhat2Do(message):
    global USER_ID

    # If the incoming message contains "hi", then respond with a "Hello" message
    if message.get("subtype") is None and "hi" in message.get('text'):
        channel = message["channel"]
        USER_ID = message["user"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message)
    
    # START ORDER
    elif message.get("subtype") is None and "menu" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message, attachments=attachments.menu_list[0])
    
    elif message.get("subtype") is None and "games" in message.get('text'):
        channel = message["channel"]
        message = "Hello <@%s>! :tada:" % message["user"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message, attachments=attachments.attachments_json2)
    
    elif message.get("subtype") is None and "req" in message.get('text'):
        channel = message["channel"]
        slack_client.api_call("chat.postMessage", channel=channel, text=message)

def select_message_action(form_json):
    global orders, text

    # Check to see what the user's selection was and update the message accordingly
    selection = form_json["actions"][0]["selected_options"][0]["value"]

    # Edit message text according to user selection
    message_text = get_message_according_to_selection(selection)
    
    if len(orders) is not 0:
        text += "\n" + str(message_text) + " has been chosen :white_check_mark:" 
    else:
        text = str(message_text) + " has been chosen :white_check_mark:" 
    
    orders.append(selection)
    
    try:
        # send message
        response = slack_client.api_call(
        "chat.update",
        channel=form_json["channel"]["id"],
        ts=form_json["message_ts"],
        text=text,
        color="#3AA3E3",
        attachments=attachments.menu_list[len(orders)] # empty `attachments` to clear the existing massage attachments
        )
        #print (response)
    except:
        attch = attachments.confirm_buttons
        attch[0]['fields'][0]['value'] = text.split('\n')[0]
        attch[0]['fields'][1]['value'] = text.split('\n')[1]
        attch[0]['fields'][2]['value'] = text.split('\n')[2]
        attch[0]['title'] = "Selected parameters in below. Do you want to run the query?"

        # send message
        response = slack_client.api_call(
        "chat.update",
        channel=form_json["channel"]["id"],
        ts=form_json["message_ts"],
        text="",
        attachments=attch
        )
        #orders = []
        text = ""

def button_message_action(form_json):
    global orders
    # send message
    response = slack_client.api_call(
        "chat.update",
        channel=form_json["channel"]["id"],
        ts=form_json["message_ts"],
        text="You choosed: " + orders[0] + " " + orders[1] + " " + orders[2],
        color="#3AA3E3",
        attachments=[] # empty `attachments` to clear the existing massage attachments
    )
    orders = []


# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)