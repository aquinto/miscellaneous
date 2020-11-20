from bs4 import BeautifulSoup   
import urllib.request  
import smtplib
from email.message import EmailMessage
from file_vars import email_sender 
from file_vars import email_password
from file_vars import email_receiver
def sendEmail():
    msg = EmailMessage()
    msg["Subject"] = "3070 IN STOCK NOW"
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg.set_content("BACK IN STOCK: https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: 
        smtp.login(email_sender,email_password)
        smtp.send_message(msg)

def checkStock():
    page_url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
    hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }

    req = urllib.request.Request(page_url,headers=hdr)
    response = urllib.request.urlopen(req)
    page_html = response.read()
    response.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')
    stuff_we_want = html_soup.find('button',class_="btn btn-disabled btn-lg btn-block add-to-cart-button").text
    if str(stuff_we_want) == "Add to Cart":
        sendEmail()

checkStock()