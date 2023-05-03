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
# import aiohttp
import asyncio

import smart_headers, json_reader_test, photos_func, description_func, review_func, faciclities_func, rooms_func, rooms_block_func, writerr
# db_handler
# proxy_generator


# ////////// upz_hotels block/////////////////////////////////////

def requests_generator(prLi, fixed_url):
    r = ''
    for sesCountt in range(3):
        proxy_item = {       
            "https": f"http://{choice(prLi)}"          
        } 
        # print(proxy_item)
        r = ''
        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)  
        try:  
            # print('hello req')                    
            r = requests.get(fixed_url, headers=smart_headers.random_headers(), proxies=proxy_item, timeout=(3.15, 21.15))
            r.raise_for_status()
            print(r.status_code)
            if r.status_code == 404: 
                return None
            if r.status_code == 200:
                return r.text 
            else:
                continue

        except requests.exceptions.HTTPError as ex:
            print(f"str44___HTTP error occurred: {ex}")           
            if sesCountt == 2:
                return None                
            else:
                continue 
    try:
        return r.text 
    except:
        return None
# ////////////////// async///////////////////////////////////

async def scraper_grendmather(resHtml, hotelid, photoInd, descriptionInd, facilityInd, roomInd):
    flagTest = True
    result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = [], [], [], [], []

    async def mather_controller_two():
        nonlocal flagTest, result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks 
        tasks = [
            asyncio.create_task(async_page_scraper_photos()),
            asyncio.create_task(async_page_scraper_description()), 
            asyncio.create_task(async_page_scraper_facilities()),
            asyncio.create_task(async_page_scraper_room()),
            asyncio.create_task(async_page_scraper_room_block())
        ]
        
        await asyncio.gather(*tasks)

    async def async_page_scraper_photos():
        nonlocal flagTest, result_photos_upz
        # print(resHtml)
        if (photoInd != "1" and photoInd != 1) or flagTest == True:
            try:
                rFoto = photos_func.page_scraper_photos(resHtml, hotelid)
                result_photos_upz.append(rFoto) 
            except:
                result_photos_upz = None
    async def async_page_scraper_description():
        nonlocal flagTest, result_description_upz
        if (descriptionInd != "1" and descriptionInd != 1) or flagTest == True:
            try:
                rDescription = description_func.page_scraper_description(resHtml, hotelid)
                result_description_upz.append(rDescription)
            except:
                result_description_upz = None 

    async def async_page_scraper_facilities():
        nonlocal flagTest, result_facilities_upz
        if (facilityInd != "1" and facilityInd != 1) or flagTest == True:
            try:
               result_facilities_upz.append(faciclities_func.page_scraper_facilities(resHtml, hotelid))
            except:
               result_facilities_upz = None
    async def async_page_scraper_room():
        nonlocal flagTest, result_rooms_upz
        if (roomInd != "1" and roomInd != 1) or flagTest == True:
            try:
               result_rooms_upz.append(rooms_func.page_scraper_room(resHtml, hotelid))
            except:
               result_rooms_upz = None 
    async def async_page_scraper_room_block():
        nonlocal  flagTest, upz_hotels_rooms_blocks
        if (roomInd != "1" and roomInd != 1) or flagTest == True:
            try:
               upz_hotels_rooms_blocks.append(rooms_block_func.page_scraper_room_block(resHtml, hotelid))
            except:
               upz_hotels_rooms_blocks = None  

    await mather_controller_two()

    return result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks

# ////////// asynk end/////////////////////////////////////

def grendMather_controller(data):
    flagCount = 0
    flagTest = True
    resHtml = ''

    result_photos_upz = []
    result_description_upz = []
    result_review_upz = []
    result_facilities_upz = []
    result_rooms_upz = []
    upz_hotels_rooms_blocks = []
    upz_hotels_rooms_highlights = []

    black_list = []
    white_list = []
    try:
        data_upz_hotels_item = data.split('SamsonovNik')[1]
    except:
        pass

    try:
        prLi_str = data.split('SamsonovNik')[0]
        try:
            prLi = eval(prLi_str)
        except:
            pass
    except:
        pass

    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item) 
    except:
        data_upz_hotels_item_dict = data_upz_hotels_item 
    try:
       hotelid = data_upz_hotels_item_dict["hotel_id"] 
    except:
       hotelid = 'not found'
    photoInd = data_upz_hotels_item_dict["fotos"]
    descriptionInd = data_upz_hotels_item_dict["description"]
    otzivInd = data_upz_hotels_item_dict["otziv"]
    facilityInd = data_upz_hotels_item_dict["facility"] 
    roomInd = data_upz_hotels_item_dict["room"]
    # print('ok var')

    if photoInd == "1" or photoInd == 1:
        flagCount += 1  
    if descriptionInd == "1" or descriptionInd == 1:
        flagCount += 1 
    if otzivInd == "1" or otzivInd == 1:
        flagCount += 1 
    if facilityInd == "1" or facilityInd == 1:
        flagCount += 1 
    if roomInd == "1" or roomInd == 1:
        flagCount += 1

    if flagCount == 5 and flagTest != True:
        black_list.append(hotelid)        
        return [[None], black_list] 
    
    else:
        try:
            link = ''
            link = data_upz_hotels_item_dict["url"] 
            try:
               fixed_url = re.sub(r'\\/', '/', link)  
            except:
               fixed_url = data_upz_hotels_item_dict["url"]
        except Exception as ex:
            # print(f"str199___{ex}")
            return [[None], black_list] 
        try:
        #    resHtml, result_review_upz = response_grendmather(prLi, fixed_url, otzivInd, hotelid)  
        # 
           resHtml = requests_generator(prLi, fixed_url)               
     
        except Exception as ex:
            # print(f"249____{ex}")
            # return [[None], black_list]           
        # print( resHtml)
            pass

        try:
            # print('h')
            # data_upz_hotels_args = [resHtml, hotelid, photoInd]
            result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks= scraper_grendmather(resHtml, hotelid, photoInd, descriptionInd, facilityInd, roomInd)
        except Exception as ex:
            # print(f"249____{ex}")
            # return [[None], black_list] 
            pass          
        # print( resHtml)
        try:
            black_list.append(hotelid)
            return [[result_photos_upz, result_description_upz, result_review_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks, None], black_list] 
        
        except Exception as ex:
            # print(f"220____{ex}")
            return [[None], black_list] 

def father_multiprocessor(data_upz_hotels):
    from mpire import WorkerPool   
    # n = multiprocessing.cpu_count() * 10  
    prLi = proxy_reader()
    n = 21
    data_upz_hotels_args = list(f"{prLi}SamsonovNik{data_upz_hotels[i]}" for i in range(len(data_upz_hotels)))
    with WorkerPool(n_jobs = n) as p2:
        # print('hello multi')                      
        finRes = p2.map(grendMather_controller, data_upz_hotels_args)
    writerr.writerr(finRes)     
    finRes = []  

        
def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi


def main():
    start_time = time.time() 
    urls_list = []
    data_upz_hotels_all = json_reader_test.data_upz_hotels_func()[0] 
    data_upz_hotels = json_reader_test.data_upz_hotels_func()[1]
    # for url in data_upz_hotels:
    #     urls_list.append(url["url"]) 
    # try:
    #     with open(f'urls_list_1-50.json', "w", encoding="utf-8") as file: 
    #         json.dump(urls_list, file, indent=4, ensure_ascii=False)
    # except Exception as ex:
    #     print(f"str226__{ex}") 


    father_multiprocessor(data_upz_hotels)
    finish_time = time.time() - start_time 
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")   

if __name__ == "__main__":
    main() 


# python main.py 

# t = [
#     [[[], [], [], [], [None]], ['2061186']],
#     [[[], [], [], [], [None]], ['3060101']],
#     [[[], [], [], [], [None]], ['543969']],
#     [[[], [], [], [], [None]], ['1037647']],
#     [[[], [], [], [], [None]], ['1654758']]
# ]
