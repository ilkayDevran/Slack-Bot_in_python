# -*- coding: UTF-8 -*-

from slackclient import SlackClient
from calendar import monthrange
from attches import *
import requests
import json
import os
import time


class Bot():
    def __init__(self, SLACK_BOT_TOKEN):
        self.services = {}
        self.slack_client = SlackClient(SLACK_BOT_TOKEN)
    
    # major methods
    def handleDirectMessage(self, message):
        try: 
            if message['user'] not in self.services.keys():
                self.decideWhat2Do(message)
            else:
                channel = message['channel']
                text = 'Let\'s keep working on the open order.'
                self.slack_client.api_call('chat.postMessage', channel=channel, text=text)
        except:
            pass

    def decideWhat2Do(self, message):
        channel = message['channel']
        if message.get('subtype') is None and ('hi' in message.get('text') or 'hey' in message.get('text')):
            text = 'Hello <@%s>! :tada:\nI am SapsikBirBot, and I\'m here to help bring you :chart_with_upwards_trend:\n' % message['user'] 
            self.slack_client.api_call('chat.postMessage', channel=channel, text=text)
        
        elif message.get('subtype') is None and 'chart' in message.get('text'):
            text = 'Let\'s start creating a chart! :tada:'
            self.slack_client.api_call('chat.postMessage', channel=channel, text=text, attachments=start_service_button)
        
        elif message.get('subtype') is None and 'sapsik' in message.get('text'):
            print self.services
            self.slack_client.api_call(
                                'files.upload', 
                                channels=channel, 
                                filename='pic.jpg', 
                                file=open('./assets/cute-robot.jpg', 'rb'),
                                )

    def reactionAdded(self, event):
        emoji = event['reaction']
        channel = event['item']['channel']
        text = ':%s:' % emoji
        self.slack_client.api_call('chat.postMessage', channel=channel, text=text)

    def sendMessage(self, chat_action_type, jsn, text, attach, clr='#3AA3E3'):
        self.slack_client.api_call(
            chat_action_type,
            channel = jsn['channel']['id'],
            ts = jsn['message_ts'],
            text = text,
            color = clr,
            attachments = attach
        )

    def sendConfirmButtons(self, chat_action_type, jsn, text, attach):
        self.slack_client.api_call(
                    chat_action_type,
                    channel = jsn['channel']['id'],
                    ts = jsn['message_ts'],
                    text = text,
                    attachments = attach
                )

    # EVENT TYPES 
    def select_message_action(self,jsn):
        if (jsn['actions'][0]['name'] == 'parameter:Company' or 
            jsn['actions'][0]['name'] == 'parameter:Platform' or 
            jsn['actions'][0]['name'] == 'parameter:Period' or 
            jsn['actions'][0]['name'] == 'parameter:Category' or
            jsn['actions'][0]['name'] == 'parameter:NewsCategory' or
            jsn['actions'][0]['name'] == 'parameter:Calendar'):
            self.handle_chart_service(jsn)
            
    def button_message_action(self, jsn):
        #print json.dumps(jsn, indent=4)
        userId = jsn['user']['id']
        channel = jsn['channel']['id']

        if jsn['callback_id'] == 'service:start':
            self.startService(jsn)

        elif jsn['callback_id'] == 'confirm_buttons':
            if jsn['actions'][0]['value'] == 'yes':
                # SEND REQUEST HERE
                self.get_from_uluc_and_draw(userId,channel)
                text = '-'.join(self.services[userId]['answers'])
                
                self.slack_client.api_call(
                    'chat.update',
                    channel = jsn['channel']['id'],
                    ts = jsn['message_ts'],
                    color = '#3AA3E3',
                    text = text,
                    attachments=[]
                )
            else:
                # CANCEL SERVICE
                self.slack_client.api_call(
                    'chat.update',
                    channel = jsn['channel']['id'],
                    ts = jsn['message_ts'],
                    color = '#3AA3E3',
                    text = 'Service has been cancelled. OK!',
                    attachments=[]
                )
            del self.services[userId]
            print ('DICT:', self.services)
        

    # Action handling methods
    def startService(self, jsn):
        userId = jsn['user']['id']
        # error handling
        if  userId in self.services.keys():
            text = 'I\'m already working on an order for you, please be patient'
            self.slack_client.api_call('chat.postMessage', channel=jsn['channel']['id'], text=text)
            return
        
        # initialize the order
        self.services[userId] = {
            'answers':[], 
            'next_question':0
            }

        text = 'Great! What can I get started for you?'
        self.sendMessage('chat.update',jsn,text, question_list[self.services[userId]['next_question']])
        self.services[userId]['next_question'] += 1
        print json.dumps(self.services, indent=4)

    def get_from_uluc_and_draw(self, userId, channel):
        url = 'https://l4y9s79bxi.execute-api.eu-west-1.amazonaws.com/prod/getdata?key1='
        print self.services[userId]['answers']
        
        if len(self.services[userId]['answers']) != 5:
            tmp = '-'.join(str(item) for item in self.services[userId]['answers']) 
            url = str(url) + str(tmp) + '-Total'
            
        else:
            tmp = '-'.join(str(item) for item in self.services[userId]['answers'])
            url = str(url) + str(tmp) 
        print url

        cmd = 'python helper_scripts/new_draw.py -url ' + url
        
        if os.system(cmd) == 0:
            print 'SAVED BEEEE! :D hadi yolla artık'
            print self.services
            self.slack_client.api_call(
                                'files.upload', 
                                channels=channel, 
                                filename='pic.jpg', 
                                file=open('./assets/new_image.jpg', 'rb'),
                                )
        
    def handle_chart_service(self, jsn):
        # Append selected value into answers list of user
        userId = jsn['user']['id']
        selected_value = jsn['actions'][0]['selected_options'][0]['value']
        self.services[userId]['answers'].append(selected_value)

        # Edit message text according to user selection
        if len(self.services[userId]['answers']) == 1:
            text = ':white_check_mark: ' + str(selected_value)
        else:
            text = ':white_check_mark: ' + '\n:white_check_mark: '.join(self.services[userId]['answers'])
        
        print 'Oestion:', self.services[userId]['next_question']

        # CHART QUESTIONS FLOW IN BELLOW #
        if self.services[userId]['next_question'] == 4:
            if self.services[userId]['answers'][0] in question_list[4].keys():
                self.sendMessage('chat.update',jsn,text, question_list[4][self.services[userId]['answers'][0]])
                self.services[userId]['next_question'] += 1 
            else:
                self.services[userId]['next_question'] += 1 # Pass 5. question for undetermined companies
                self.services[userId]['answers'].append('NULL')
                self.sendMessage('chat.update',jsn,text, question_list[self.services[userId]['next_question']])
                self.services[userId]['next_question'] += 1 # Increment next question index
        elif self.services[userId]['next_question'] == 7:
            if self.services[userId]['answers'][2] == 'Daily':
                self.sendMessage('chat.update',jsn,text, self.prepare_days_template(userId))
                self.services[userId]['next_question'] += 1
            else:
                self.sendConfirmButtons('chat.update',jsn,text, confirm_buttons)
        elif len(self.services[userId]['answers']) >= len(question_list):
            self.sendConfirmButtons('chat.update',jsn,text, confirm_buttons)
        else:
            self.sendMessage('chat.update',jsn,text, question_list[self.services[userId]['next_question']])
            self.services[userId]['next_question'] += 1
        print self.services[userId]['answers']

    # Helper methods
    def prepare_days_template(self, userId):
        template = day_question
        # monthrange(year, month)
        daysInChosenMonth = monthrange(int(self.services[userId]['answers'][5]), int(self.services[userId]['answers'][6]))[1] + 1
        for i in range(1, daysInChosenMonth):
            template[0]['actions'][0]['options'].append(
                { 
                    'text': str(i), 
                    'value': str(i)
                } 
            )
        return template