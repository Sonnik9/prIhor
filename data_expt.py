from requests_html import HTMLSession
import requests
# from requests import *
from bs4 import BeautifulSoup
import random 
from random import choice
import time
import json
from lxml import etree
from lxml import html
import math
import re
from datetime import datetime

import aiohttp
import asyncio
import db_handler, proxy_generator, smart_headers, json_reader_test



async def links_normalizator(data_exeptions):
    link = ''
    count_link_sessions = 0
    link = data_exeptions["url"]  
    # link = 'https://www.booking.com//hotel//uz//hilton-tashkent-city.html'
    #   // https://www.booking.com//hotel//al//elti-apartment.html
    # good url

    # link = 'https:\/\/www.booking.com\/hotel\/hn\/bo-39-s-island-house.html'
    # bad url     
    
    while True:            
        r = requests.get(link, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))             
    
        if str(r) == '<Response [200]>':
            print('Первый ответ сервера положительный')
        if str(r) == '<Response [503]>':            
            print('503-я ошибка!')

        if str(r) == '<Response [403]>':
            print('Сервер отверг запрос')

        if str(r) == '<Response [504]>':
            return [link, data_exeptions] 
        if str(r) == '<Response [404]>':
            print('Страница не найдена. Проверьте правильность url')

        
        try:
            soup_link = BeautifulSoup(r.text, "lxml")
        except Exception as ex:
            print(f"str56___{ex}") 
        try:                   
            link = soup_link.find('h3').find('a').get('href')
            if link != '':
                print(link)
                return [link, data_exeptions] 
                # return link                
            else:
                count_link_sessions += 1 
                if count_link_sessions == 3:
                    link = ''
                    print('something bad whith curent url')
                    return [link, data_exeptions] 
                    # return link  
                else:
                    time.sleep(random.randrange(2,7))
                    continue             
            
        except Exception as ex:
            print(f"str74___{ex}") 
            # pass                

async def async_links_tasker(data_upz_hotels):
    
    async with aiohttp.ClientSession() as session:       
        tasks = [] 
        for data_item in data_upz_hotels:
            task = asyncio.create_task(links_normalizator(data_item))
            tasks.append(task)
        await asyncio.gather(*tasks)

def main():
    data_upz_hotels = json_reader_test.data_upz_hotels_func()
    asyncio.run(async_links_tasker(data_upz_hotels))
    

if __name__ == "__main__":
    main() 


# python data_expt.py