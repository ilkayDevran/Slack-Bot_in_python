# -*- coding: UTF-8 -*-

from slackclient import SlackClient
from attches import *
import json

class Bot():
    def __init__(self, SLACK_BOT_TOKEN):
        self.services = {}
        self.slack_client = SlackClient(SLACK_BOT_TOKEN)
    
    # major methods
    def handleDirectMessage(self, message):
        try: 
            if message["user"] not in self.services.keys():
                self.decideWhat2Do(message)
            else:
                channel = message["channel"]
                text = "Let\'s keep working on the open order."
                self.slack_client.api_call("chat.postMessage", channel=channel, text=text)
        except:
            pass

    def decideWhat2Do(self, message):
        channel = message["channel"]
        if message.get("subtype") is None and ("hi" in message.get('text') or "hey" in message.get('text')):
            text = "Hello <@%s>! :tada:\nI am SapsikBirBot, and I\'m here to help bring you :chart_with_upwards_trend:\n" % message["user"] 
            self.slack_client.api_call("chat.postMessage", channel=channel, text=text)
        
        elif message.get("subtype") is None and "chart" in message.get('text'):
            text = "Let\'s start creating a chart! :tada:"
            self.slack_client.api_call("chat.postMessage", channel=channel, text=text, attachments=start_service_button)
        
        elif message.get("subtype") is None and "sapsik" in message.get('text'):
            print self.services
            self.slack_client.api_call(
                                'files.upload', 
                                channels=channel, 
                                filename='pic.jpg', 
                                file=open('./assets/cute-robot.jpg', 'rb'),
                                )

    def reactionAdded(self, event):
        emoji = event["reaction"]
        channel = event["item"]["channel"]
        text = ":%s:" % emoji
        self.slack_client.api_call("chat.postMessage", channel=channel, text=text)

    # EVENT TYPES 
    def select_message_action(self,jsn):
        #print json.dumps(jsn, indent=4)
        userId = jsn["user"]['id']

        if (jsn["actions"][0]["name"] == "parameter:Company" or 
            jsn["actions"][0]["name"] == "parameter:Platform" or 
            jsn["actions"][0]["name"] == "parameter:Period" or 
            jsn["actions"][0]["name"] == "parameter:Category" or
            jsn["actions"][0]["name"] == "parameter:NewsCategory"):

            selected_value = jsn["actions"][0]["selected_options"][0]["value"]
            self.services[userId].append(selected_value)

            if len(self.services[userId]) == len(chart_parameters_list):
                try:
                    self.slack_client.api_call(
                        "chat.update",
                        channel = jsn["channel"]["id"],
                        ts = jsn["message_ts"],
                        color = "#3AA3E3",
                        attachments = newsCategories[self.services[userId][0]] 
                    )
                except:
                    #text = '-'.join(self.services[userId])
                    # send message
                    self.slack_client.api_call(
                        "chat.update",
                        channel = jsn["channel"]["id"],
                        ts = jsn["message_ts"],
                        text = "",
                        attachments = confirm_buttons
                    )
                    #del self.services[userId]
                    #print 'DICT:',self.services
            else:
                try:
                    self.slack_client.api_call(
                        "chat.update",
                        channel = jsn["channel"]["id"],
                        ts = jsn["message_ts"],
                        color = "#3AA3E3",
                        attachments = chart_parameters_list[len(self.services[userId])] 
                    )
                except:
                    #text = '-'.join(self.services[userId])
                    # send message
                    self.slack_client.api_call(
                        "chat.update",
                        channel = jsn["channel"]["id"],
                        ts = jsn["message_ts"],
                        text = "",
                        attachments = confirm_buttons
                    )
                    #del self.services[userId]
                    #print 'DICT:',self.services
    
    def button_message_action(self, jsn):
        #print json.dumps(jsn, indent=4)
        userId = jsn["user"]['id']

        if jsn['callback_id'] == "service:start":
            self.startService(jsn)

        elif jsn['callback_id'] == "confirm_buttons":
            # BURAYA KONTROL EKLE USER IDDEN. JSONDADA USER A READY KEY I TANIMLA
            if jsn['actions'][0]['value'] == "yes":
                text = '-'.join(self.services[userId])
                self.slack_client.api_call(
                    "chat.update",
                    channel = jsn["channel"]["id"],
                    ts = jsn["message_ts"],
                    color = "#3AA3E3",
                    text = text,
                    attachments=[]
                )
            else:
                self.slack_client.api_call(
                    "chat.update",
                    channel = jsn["channel"]["id"],
                    ts = jsn["message_ts"],
                    color = "#3AA3E3",
                    text = 'Service has been cancelled. OK!',
                    attachments=[]
                )
            del self.services[userId]
            print ('DICT:', self.services)
        

    # Action handling methods
    def startService(self, jsn):
        userId = jsn["user"]['id']
        # error handling
        if  userId in self.services.keys():
            text = "I\'m already working on an order for you, please be patient"
            self.slack_client.api_call("chat.postMessage", channel=jsn['channel']['id'], text=text)
            return
        
        # initialize the order
        self.services[userId] = []
        text = "Great! What can I get started for you?"
        self.slack_client.api_call("chat.update", 
                                    channel=jsn['channel']['id'],
                                    ts=jsn["message_ts"],
                                    text=text,
                                    attachments=chart_parameters_list[len(self.services[userId])]
                                    )
        print json.dumps(self.services, indent=4)


