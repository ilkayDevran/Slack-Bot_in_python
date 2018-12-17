# -*- coding: UTF-8 -*-

##-----------------------------BUTTONS---------------------------------------

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


################################### QUESTION TEMPLATES #####################

company_question = [
    {
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
    }
]

platform_question = [
    {
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
    }
]

period_question = [
    {
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
    }
]

category_question = [
    {
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
    }
]

### SUB QUESTION ###
newsCategory_question = {
    "Hurriyet" : [
        {
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
        }
    ],

    "Bigpara" : [
        {
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
        }
    ],

    "Fanatik" : [
        {
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
        }
    ],

    "Posta" : [
        {
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
        }
    ]
}

####################


year_question = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Calendar:Daily:Year",
        "actions": [
            {
                "name": "parameter:Calendar",
                "text": "Calendar...",
                "type": "select",
                "options": [
                    {
                        "text": "2018",
                        "value": "2018"
                    },
                    {
                        "text": "2019",
                        "value": "2019"
                    }
                ]
            }
        ]
    }
]

month_question = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Calendar:Daily:Month",
        "actions": [
            {
                "name": "parameter:Calendar",
                "text": "Calendar...",
                "type": "select",
                "options": [
                    {
                        "text": "Ocak",
                        "value": "01"
                    },
                    {
                        "text": "Şubat",
                        "value": "02"
                    },
                    {
                        "text": "Mart",
                        "value": "03"
                    },
                    {
                        "text": "Nisan",
                        "value": "04"
                    },
                    {
                        "text": "Mayıs",
                        "value": "05"
                    },
                    {
                        "text": "Haziran",
                        "value": "06"
                    },
                    {
                        "text": "Temmuz",
                        "value": "07"
                    },
                    {
                        "text": "Ağustos",
                        "value": "08"
                    },
                    {
                        "text": "Eylül",
                        "value": "09"
                    },
                    {
                        "text": "Ekim",
                        "value": "10"
                    },
                    {
                        "text": "Kasım",
                        "value": "11"
                    },
                    {
                        "text": "Aralık",
                        "value": "12"
                    }
                ]
            }
        ]
    }
]

day_question = [
    {
        "fallback": "Upgrade your Slack client to use messages like these.",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "parameter:Calendar:Daily:Day",
        "actions": [
            {
                "name": "parameter:Calendar",
                "text": "Calendar...",
                "type": "select",
                "options": []
            }
        ]
    }
]

############################################################################

# ALL IN ONE
question_list = [
    company_question,
    platform_question,
    period_question,
    category_question,
    newsCategory_question,
    year_question,
    month_question,
    day_question
]

#-------------------------------------------------------------------------------------------#


# OLD PARTS #

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

# Custom newsCategories parameters json
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

# Custom calendar parameters json
calendar_menu = {
    "Daily" : [
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Year",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }],
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Month",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }],
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Day",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }]
    ],

    "Weekly":[
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Year",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }],
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Month",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }],
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Day",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }]
    ],

    "Monthly":[
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Year",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }],
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Month",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }],
                    [{
                        "fallback": "Upgrade your Slack client to use messages like these.",
                        "color": "#3AA3E3",
                        "attachment_type": "default",
                        "callback_id": "parameter:Calendar:Daily:Day",
                        "actions": [
                                        {
                                            "name": "parameter:Calendar",
                                            "text": "Calendar...",
                                            "type": "select",
                                            "options": []
                                        }
                                    ]
                    }]
    ]
}
