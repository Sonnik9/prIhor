# from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
from random import choice
import time
import smart_headers
# import http

# Selmenlo889:M7z1HsW@185.33.85.195:50100

def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi


def checkIP(): 
    # print(proxiess)  
    prLi = proxy_reader()
    # link = 'http://checkip.dyndns.org'
    link = 'https://api.ipify.org'

    for pr in prLi:
        proxy_item = {       
            "https": f"http://{pr}"          
        } 
        print(proxy_item)

        ip = requests.get(link, headers=smart_headers.random_headers(), proxies=proxy_item, timeout=(3.15, 21.15))
        print(ip.text)


checkIP()

# python toKnowYourAdress.py