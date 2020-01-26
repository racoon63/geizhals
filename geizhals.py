#!/usr/bin/env pyhton3

# Run this script with:
# 
# python3 geizhals.py

import requests
from bs4 import BeautifulSoup

target_price = 510.00
baseUrl = "https://geizhals.de/gigabyte-geforce-rtx-2070-super-windforce-oc-3x-8g-gv-n207swf3oc-8gd-a2122943.html?hloc=at&hloc=de"

if __name__ == "__main__":
    
    response = requests.get(baseUrl)
    html = BeautifulSoup(response.text, "html.parser")
    
    enclose = html.find_all("dd", {"itemprop": "offers", "itemtype": "http://schema.org/AggregateOffer"})

    price = enclose[0].meta.get("content")

    if float(price) <= target_price:
        print("Price reached your target price of: {}".format(target_price))
        print("Price of your requested item is: {}".format(price))
    else:
        print("Price is still too high. Current lowest price is: {}".format(price))
