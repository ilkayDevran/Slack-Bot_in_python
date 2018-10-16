# -*- coding: UTF-8 -*-

# A Dictionary of message attachment options
attachments_json = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "menu_options_2319",
        "actions": [
            {
                "name": "list1",
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
            },
            {
                "name": "list2",
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
            },
            {
                "name": "list3",
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
    }
]
attachments_json2= [
        {
            "text": "Choose a game to play",
            "fallback": "You are unable to choose a game",
            "callback_id": "wopr_game",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "game",
                    "text": "Chess",
                    "type": "button",
                    "value": "chess"
                },
                {
                    "name": "game",
                    "text": "Falken's Maze",
                    "type": "button",
                    "value": "maze"
                },
                {
                    "name": "game",
                    "text": "Thermonuclear War",
                    "style": "danger",
                    "type": "button",
                    "value": "war",
                    "confirm": {
                        "title": "Are you sure?",
                        "text": "Wouldn't you prefer a good game of chess?",
                        "ok_text": "Yes",
                        "dismiss_text": "No"
                    }
                }
            ]
        }
    ]

news_attachments = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "menu_options_2319",
        "actions": [
            {
                "name": "list1",
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
    }
]

topic_attachments = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "menu_options_2319",
        "actions": [
                    {
                        "name": "list2",
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
    }
]

date_attachments = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "menu_options_2319",
        "actions": [
                    {
                        "name": "list3",
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
    }
]


menu_list = [
    news_attachments, topic_attachments, date_attachments
]



### BUTTONS ###
menu_send_query_button = [
    {
      "fallback": "Book your flights at https://flights.example.com/book/r123456",
      "actions": [
            {
            "type": "button",
            "text": "Book flights 🛫",
            "url": "https://flights.example.com/book/r123456"
            }
        ]
    }
]

confirm_buttons = [
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