# -*- coding: utf-8 -*-
import os
import json
import argparse
import requests
import matplotlib.pyplot as plt

# USAGE
# python allinone.py -t ../ROI_images/training -e ../ROI_images/testing

def currency_api_get_request():
    saving_path = "/Users/ilkay/Desktop/python-slackapp/app/assets/new_image.jpg"
    FIXER_API_KEY = ""
    # send request to api with user selection as parameter
    re = requests.get('http://data.fixer.io/api/latest?access_key=' + FIXER_API_KEY + '&base%20=%20'+ "EUR")
    # responsed json object
    json_obj = json.loads(re.text)
    base = json_obj['base']
    x = []
    y= []
    counter = 0
    for key in json_obj['rates'].keys():
        if counter == 5:
            break
        x.append(key)
        y.append(json_obj['rates'][key])
        counter +=1

    print '\nCHART IS PREPARING....'
    plt.title('Currency Chart')
    plt.plot(x, y)
    plt.ylabel(base)
    print 'SAVING...'
    plt.savefig(saving_path)
    print 'SAVEDDDDD! \n\n'
    #plt.show()


def main(cmp, plt, prd, ctg, nctg):
    print "Hi FROM SCRIPT 2"
    currency_api_get_request()

# MAIN
if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-cmp", "--company", required=True,
        help="company parameter")
    ap.add_argument("-plt", "--platform", required=True,
        help="platform parameter")
    ap.add_argument("-prd", "--period", required=True,
        help="Period parameter")
    ap.add_argument("-ctg", "--category", required=True,
        help="Category parameter")
    ap.add_argument("-nctg", "--newscategory", type=str, default=None,
        help="NewsCategory parameter")
    args = vars(ap.parse_args())

    main(
        args["company"],
        args["platform"],
        args["period"],
        args["category"],
        args["newscategory"]
        )

   

    