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


# menu for chart parameters 
chart_parameters_list = [
    [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Company",
        "actions": [
            {
                "name": "parameter:Company",
                "text": "Company...",
                "type": "select",
                "options": [
                    {
                        "text": "Hürriyet",
                        "value": "Hurriyet"
                    },
                    {
                        "text": "Milliyet",
                        "value": "Milliyet"
                    },
                    {
                        "text": "Posta",
                        "value": "Posta"
                    },
                    {
                        "text": "Vatan",
                        "value": "Vatan"
                    },
                    {
                        "text": "Kelebek",
                        "value": "Kelebek"
                    },
                    {
                        "text": "Bigpara",
                        "value": "Bigpara"
                    },
                    {
                        "text": "Fanatik",
                        "value": "Fanatik"
                    },
                    {
                        "text": "Hürriyet Aile",
                        "value": "H_aile"
                    },
                    {
                        "text": "Hürriyet Oto.",
                        "value": "H_oto"
                    }

                ]
            }
        ]
    }], [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Platform",
        "actions": [
                        {
                            "name": "parameter:Platform",
                            "text": "Platform...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "IOS",
                                    "value": "IOS"
                                },
                                {
                                    "text": "Android",
                                    "value": "Android"
                                },
                                {
                                    "text": "Web",
                                    "value": "Web"
                                }
                            ]
                        }
                    ]
    }], [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Period",
        "actions": [
                        {
                            "name": "parameter:Period",
                            "text": "Period...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "Daily",
                                    "value": "Daily"
                                },
                                {
                                    "text": "Weekly",
                                    "value": "Weekly"
                                },
                                {
                                    "text": "Monthly",
                                    "value": "Monthly"
                                }
                            ]
                        }
                    ]
    }],[{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Category",
        "actions": [
                        {
                            "name": "parameter:Category",
                            "text": "Category...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "Gallery",
                                    "value": "Gallery"
                                },
                                {
                                    "text": "Article",
                                    "value": "Article"
                                },
                                {
                                    "text": "Total",
                                    "value": "Total"
                                }
                            ]
                        }
                    ]
    }]
]


# Custom newsCategories parameters list
newsCategories = {
    "Hurriyet" : [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:NewsCategory:Hurriyet",
        "actions": [
                        {
                            "name": "parameter:NewsCategory",
                            "text": "NewsCategory...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "Anasayfa",
                                    "value": "anasayfa"
                                },
                                {
                                    "text": "Gündem",
                                    "value": "gundem"
                                },
                                {
                                    "text": "Kelebek",
                                    "value": "kelebek"
                                },
                                {
                                    "text": "Bigpara",
                                    "value": "bigpara"
                                },
                                {
                                    "text": "Ekonomi",
                                    "value": "ekonomi"
                                },
                                {
                                    "text": "Dünya",
                                    "value": "dunya"
                                },
                                {
                                    "text": "Spor",
                                    "value": "spor"
                                },
                                {
                                    "text": "Yazarlar",
                                    "value": "yazarlar"
                                }
                            ]
                        }
                    ]
    }],

    "Bigpara" : [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:NewsCategory:Bigpara",
        "actions": [
                        {
                            "name": "parameter:NewsCategory",
                            "text": "NewsCategory...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "Döviz",
                                    "value": "doviz"
                                },
                                {
                                    "text": "Haberler",
                                    "value": "haberler"
                                },
                                {
                                    "text": "Altın",
                                    "value": "altin"
                                },
                                {
                                    "text": "Borsa",
                                    "value": "borsa"
                                },
                                {
                                    "text": "Hisseler",
                                    "value": "Haberler"
                                },
                                {
                                    "text": "Kredi",
                                    "value": "kredi"
                                },
                                {
                                    "text": "Kobi",
                                    "value": "kobi"
                                },
                                {
                                    "text": "Bigpara Uzmanları",
                                    "value": "bigpara-uzmanlari"
                                },
                                {
                                    "text": "Mevduat",
                                    "value": "mevduat"
                                },
                                {
                                    "text": "Faiz",
                                    "value": "faiz"
                                }
                            ]
                        }
                    ]
    }],

    "Fanatik" : [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:NewsCategory:Fanatik",
        "actions": [
                        {
                            "name": "parameter:NewsCategory",
                            "text": "NewsCategory...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "Anasayfa",
                                    "value": "anasayfa"
                                },
                                {
                                    "text": "Galatasaray",
                                    "value": "galatasaray"
                                },
                                {
                                    "text": "Fenerbahçe",
                                    "value": "fenerbahce"
                                },
                                {
                                    "text": "Beşiktaş",
                                    "value": "besiktas"
                                },
                                {
                                    "text": "Video",
                                    "value": "video"
                                },
                                {
                                    "text": "Futbol",
                                    "value": "futbol"
                                },
                                {
                                    "text": "Plus",
                                    "value": "plus"
                                },
                                {
                                    "text": "Milli Takım",
                                    "value": "milli-takim"
                                }
                            ]
                        }
                    ]
    }],

    "Posta" : [{
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:NewsCategory:Posta",
        "actions": [
                        {
                            "name": "parameter:NewsCategory",
                            "text": "NewsCategory...",
                            "type": "select",
                            "options": [
                                {
                                    "text": "Anasayfa",
                                    "value": "anasayfa"
                                },
                                {
                                    "text": "Magazin",
                                    "value": "magazin"
                                },
                                {
                                    "text": "Gündem",
                                    "value": "gundem"
                                },
                                {
                                    "text": "Ekonomi",
                                    "value": "ekonomi"
                                },
                                {
                                    "text": "Dünya",
                                    "value": "dunya"
                                },
                                {
                                    "text": "3. Sayfa",
                                    "value": "3-sayfa"
                                },
                                {
                                    "text": "Yazarlar",
                                    "value": "yazarlar"
                                },
                                {
                                    "text": "Yaşam",
                                    "value": "yasam"
                                },
                                {
                                    "text": "Kadın",
                                    "value": "kadin"
                                },
                            ]
                        }
                    ]
    }]

}
