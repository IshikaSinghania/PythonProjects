import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re

def download_image():
    pass


def check_price():
    URL = 'https://www.amazon.in/JBL-Wireless-Headphones-Battery-Charging/dp/B07XRW6NVS/ref=sr_1_3?dchild=1&keywords=jblt160bt&qid=1590065422&s=computers&sr=8-3'

    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = 'priceblock_ourprice').get_text()
    converted_price = float(price[2:8].replace(",",""))
    print(title.strip())
    print(converted_price)
    #   ---change
    image = soup.find('img', {'id': 'landingImage'})
    imgurl = dict(image.attrs)["src"]
    # resp2 = requests.ur
    # for images in image:
    #    print(images)
    if(converted_price< 1600.0):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nielsbohra@gmail.com', 'uodonugexhlvfrxc')
    subject = 'The price fell down bruh'
    body = 'Check the amazon link https://www.amazon.in/JBL-Wireless-Headphones-Battery-Charging/dp/B07XRW6NVS/ref=sr_1_3?dchild=1&keywords=jblt160bt&qid=1590065422&s=computers&sr=8-3 '
    msg = f'Subject : {subject}\n\n {body}'
    server.sendmail(
        'nielsbohra@gmail.com',
        'karankharode.kk@gmail.com',
        msg
    )
    print('Email has been sent')

#    ---for continuous background checking with pyw file---
# hour = 1
# while(hour<6):
#     check_price()
#     hour= hour+1
#     time.sleep(60)

#   ---for single IDE run---
check_price()