# -*- coding: UTF-8 -*-

start_service_button = [
    {
        "color": "#5A352D",
        "title": "How can I help you?",
        "callback_id": "service:start",
        "actions": [
            {
                "name": "start",
                "text": "Start to choose parameters",
                "type": "button",
                "value": "service:start"
            }
        ]
    }
]

# First Demo Menu List
menu_list = [
    [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "chart:menu:1",
        "actions": [
            {
                "name": "m:1",
                "text": "Pick a beverage...",
                "type": "select",
                "options": [
                    {
                        "text": "Hürriyet",
                        "value": "hurriyet"
                    },
                    {
                        "text": "Milliyet",
                        "value": "milliyet"
                    },
                    {
                        "text": "Kelebek",
                        "value": "kelebek"
                    }
                ]
            }
        ]
    }], [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "chart:menu:2",
        "actions": [
                    {
                        "name": "m:2",
                        "text": "Pick a beverage...",
                        "type": "select",
                        "options": [
                            {
                                "text": "Page Views",
                                "value": "pageviews"
                            },
                            {
                                "text": "User",
                                "value": "user"
                    }
                ]
            }
        ]
    }], [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "chart:menu:3",
        "actions": [
                    {
                        "name": "m:3",
                        "text": "Pick a beverage...",
                        "type": "select",
                        "options": [
                            {
                                "text": "Today",
                                "value": "today"
                            },
                            {
                                "text": "Yesterday",
                                "value": "yesterday"
                    }
                ]
            }
        ]
    }]
]

confirm_buttons = [
    {      
          "color": "#3eb991",
          "title": "",
          "text": "",
          "callback_id": "confirm_buttons",
          "actions": [
                {
                    "name": "confirm",
                    "text": "Yes",
                    "type": "button",
                    "value": "yes"
                },
                {
                    "name": "cancel",
                    "text": "No",
                    "type": "button",
                    "value": "no",
					"style": "danger"
                }
            ]
        }
]


# Fileds version Demo
confirm_2 = [
    {      
          "color": "#3eb991",
          "title": "",
          "text": "",
          "callback_id": "confirm_buttons",
          "fields": [
            {
              "title": "",
              "value": "",
              "short": "true"
            },
            {
              "title": "",
              "value": "",
              "short": "true"
            },
			  {
              "title": "",
              "value": "",
              "short": "true"
            } 
          ],"actions": [
                {
                    "name": "game",
                    "text": "Yes",
                    "type": "button",
                    "value": "yes"
                },
                {
                    "name": "game",
                    "text": "No",
                    "type": "button",
                    "value": "maze",
					"style": "danger"
                }
            ]
        }
]