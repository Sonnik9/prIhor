from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import time
import random
from random import choice
# import csv
import json
# import asyncio
# import aiohttp
import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from fake_useragent import UserAgent
import random 
import math
import re
import multiprocessing
from fake_useragent import UserAgent
from lxml import etree
# import socks
import socket

# Selmenlo889:M7z1HsW@185.33.85.195:50100
# Selmenlo889:M7z1HsW@94.124.160.250:50100
# Selmenlo889:M7z1HsW@45.152.177.241:50100
# Selmenlo889:M7z1HsW@216.185.46.231:50100
# Selmenlo889:M7z1HsW@2.59.60.162:50100
# Selmenlo889:M7z1HsW@23.26.229.1:50100
# Selmenlo889:M7z1HsW@108.165.218.102:50100




# with open("proxy.txt", encoding="utf-8") as file:
#     PROXY_LIST = ''.join(file.readlines()).split('\n')

# proxiess = {
#     "http": f"http://{choice(PROXY_LIST)}"     
# }

def checkIP(): 
    # print(proxiess)  
    # socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
    # socket.socket = socks.socksocket
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)

checkIP()