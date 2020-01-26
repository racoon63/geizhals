# Geizhals

Simple script to get notified when desired price is reached. This idea comes from the situation that <geizhals.de> did not send me notificagtions even if the target price was reached. I was too lazy to find out why so I wrote this simple script.

## Usage

Run the script in the following form to get the lowest price of the product you want to have e.g. a Gigabyte GeForce RTX 2070 SUPER Windforce OC 3X 8G:

### Syntax

```bash
docker run  --rm \
            -e URL=[LINK] \
            -e PRICE=[TARGET_PRICE] \
            -e SENDER=[SENDER_EMAIL] \
            -e PWD=[SENDER_EMAIL_PASSWORD] \
            -e RECEIVER=[RECEIVER_EMAIL] \
            racoon/geizhals
```

### Example

```bash
docker run  --rm \
            -e URL="https://geizhals.de/gigabyte-geforce-rtx-2070-super-windforce-oc-3x-8g-gv-n207swf3oc-8gd-a2122943.html" \
            -e PRICE=520 \
            -e SENDER="foo@bar.com" \
            -e PWD="123456" \
            -e RECEIVER="bar@foo.com" \
            racoon/geizhals
```
