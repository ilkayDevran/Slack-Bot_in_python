# -*- coding: utf-8 -*-
import os
import json
import argparse
import requests
import matplotlib.pyplot as plt


def draw_and_save_chart(url):
    saving_path = "/Users/ilkay/Desktop/hurriyet_development/slack-bot/app/assets/new_image.jpg"
    print "\n\n Hi! This message is from new_draw.py!\n\n"
    re = requests.get(url)
    # responsed json object
    print "\n\nRESPONSE FROM API!\n",json.dumps(json.loads(re.text),indent=4)

    json_obj = json.loads(re.text)
    base = "Page View"
    x = []
    y= []
    counter = 0
    for info in json_obj:
        y.append(info['Page_View'])
        x.append(info['BeginDate'])

    print '\nCHART IS PREPARING....'
    plt.title(url.split('=')[-1])
    plt.plot(x, y)
    plt.ylabel(base)
    plt.xticks(rotation=45)
    print 'SAVING...'
    plt.savefig(saving_path)
    print 'SAVEDDDDD! \n\n'
    #plt.show()


# MAIN
if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-url", "--url", required=True,
        help="API url")
    args = vars(ap.parse_args())

    draw_and_save_chart(args["url"])

   

    