# geizhals
Simple script to get notified when desired price is reached. This idea comes from the situation that <geizhals.de> did not send me notificagtions even if the target price was reached. I was too lazy to find out why so I wrote this simple script.

## Usage

Run the script in the following form to get the lowest price of the product you want to have e.g. a Gigabyte GeForce RTX 2070 SUPER Windforce OC 3X 8G:

### Syntax

```bash
python3 [LINK] [EMAIL] [EMAIL_PASSWORD]
```

### Example

```bash
python3 https://geizhals.de/gigabyte-geforce-rtx-2070-super-windforce-oc-3x-8g-gv-n207swf3oc-8gd-a2122943.html?hloc=at&hloc=de foo.bar@gettheprice.com 123456
```
