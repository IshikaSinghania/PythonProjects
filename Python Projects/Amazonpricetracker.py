import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re

def download_image():
    pass


def check_price():
    #enter url of the product you want to keep price track of
    URL = 'https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJFDW/ref=sr_1_5?dchild=1&keywords=bluetooth+headphones&qid=1590592542&sr=8-5'
    header = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find(id = 'productTitle').get_text()
    price = soup.find(id = 'priceblock_ourprice').get_text()
    converted_price = float(price[2:8].replace(",",""))
    print(title.strip())
    print(converted_price)
    image = soup.find('img', {'id': 'landingImage'})
    imgurl = dict(image.attrs)["src"]
    if(converted_price < 1500.0):
        send_mail()
    


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
#add email and password to the email id through which you want to send the email
    server.login('fakeemail@gmail.com', 'fakepassword')

    subject = 'Price fell down!'
    body = 'Check the link https://www.amazon.in/255-Bluetooth-Wireless-Earphone-Immersive/dp/B07C2VJFDW/ref=sr_1_5?dchild=1&keywords=bluetooth+headphones&qid=1590592542&sr=8-5'
    
    msg =f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'fakeemail@gmail.com',#sender
        'recieveremail@gmail.com',  #reciever
        msg
    )

    print('Mail is sent')

    
while(True):
    check_price()
    #time.sleep(25) #sends email every 25 seconds