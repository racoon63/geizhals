#!/usr/bin/env pyhton3

# Run this script with:
# 
# python3 geizhals.py

from email.mime.text import MIMEText
import os
import requests
import smtplib
import ssl
import sys

from bs4 import BeautifulSoup


def send_mail(message):

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.ehlo()
            server.login(email_sender, email_password)
            server.sendmail(email_sender, email_receiver, message)
    
    except Exception as err:
        print(err)
    
    else:
        print("Sent email notification successfully!")
        return


if __name__ == "__main__":
    
    try:
        baseUrl        = os.environ["URL"]
        target_price   = os.environ["PRICE"]
        smtp_server    = "smtp.gmail.com"
        smtp_port      = 465
        email_sender   = os.environ["SENDER"]
        email_password = os.environ["PASS"]
        email_receiver = os.environ["RECEIVER"]
        
        response = requests.get(baseUrl)
        html = BeautifulSoup(response.text, "html.parser")

        enclose = html.find_all("dd", {"itemprop": "offers", "itemtype": "http://schema.org/AggregateOffer"})

        price = enclose[0].meta.get("content")

        if float(price) <= float(target_price):
            msg = MIMEText("Price reached your target price or is below: {}. The price is now: {}".format(target_price, price))

            msg['Subject'] = "Your item reached your desired price"

            send_mail(msg.as_string())
    except Exception as err:
        print(err)
