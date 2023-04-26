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
# import asyncio

import smart_headers, json_reader_test, photos_func, description_func, review_func, faciclities_func, rooms_func
# db_handler
# proxy_generator


# ////////// upz_hotels block/////////////////////////////////////

def requests_generator(fixed_url):
    for sesCountt in range(3):
        r = ''
        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)  
        try:  
            print('hello req')                    
            r = requests.get(fixed_url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
            r.raise_for_status()
            print(r.status_code) 
            if r.status_code == 200:
                return r.text

        except requests.exceptions.HTTPError as ex:
            print(f"str44___HTTP error occurred: {ex}")           
            if sesCountt == 2:
                return None 
            else:
                continue
# ////////////////// others///////////////////////////////////
   


# ////////// others end/////////////////////////////////////

def mather_controller(data_upz_hotels_item):
    flagCount = 0
    flagTest = True

    result_photos_upz = []
    result_description_upz = []
    result_review_upz = []
    result_facilities_upz = []
    result_rooms_upz = []
    # upz_hotels_rooms_blocks = []
    # upz_hotels_rooms_highlights = []

    black_list = []
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item) 
    except:
        data_upz_hotels_item_dict = data_upz_hotels_item 

    hotelid = data_upz_hotels_item_dict["hotel_id"] 
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

    if flagCount == 5:
        black_list.append(hotelid)        
        return [[None], black_list] 
    
    else:
        try:
            link = ''
            link = data_upz_hotels_item_dict["url"] 
            fixed_url = re.sub(r'\\/', '/', link)  
        except Exception as ex:
            print(f"str199___{ex}")
            return [[None], black_list] 
        
        try:
            resHtml = requests_generator(fixed_url)          
        except Exception as ex:
            print(f"249____{ex}")
            return [[None], black_list]           
        # print( resHtml)

        if (photoInd != "1" and photoInd != 1) or flagTest == True:
            print("225str")
            rFoto = photos_func.page_scraper_photos(data_upz_hotels_item_dict, resHtml)
            result_photos_upz.append(rFoto)

        # if (descriptionInd != "1" and descriptionInd != 1) or flagTest == True:
        # # if (descriptionInd != "1" and descriptionInd != 1):
        #     # print("230str")
        #     rDescription = description_func.page_scraper_description(data_upz_hotels_item_dict, resHtml)
        #     result_description_upz.append(rDescription)
        
        # if (otzivInd != "1" and otzivInd != 1) or flagTest == True:
        #     result_review_upz.append(review_func.page_scraper_otziv(data_upz_hotels_item_dict, fixed_url))

        # if (facilityInd != "1" and facilityInd != 1) or flagTest == True:
        #     result_facilities_upz.append(faciclities_func.page_scraper_otziv(data_upz_hotels_item_dict, resHtml))

        # if (roomInd != "1" and roomInd != 1) or flagTest == True:
        #     result_rooms_upz.append(rooms_func.page_scraper_roomFather(data_upz_hotels_item_dict, resHtml))

        try:
            black_list.append(hotelid)
            return [[result_photos_upz, result_description_upz, result_review_upz, result_facilities_upz, result_rooms_upz], black_list] 
        
        except Exception as ex:
            print(f"220____{ex}")
            return [[None], black_list] 

def father_multiprocessor(data_upz_hotels):      
    from mpire import WorkerPool          
    finResArr = [] 
    total = [] 
    # data_upz_hotels = list(filter(None, data_upz_hotels))  
    # n = multiprocessing.cpu_count() * 10  
    n = 21
    vpnFraction = random.randrange(75,125)
    if len(data_upz_hotels) < vpnFraction:
        vpnFraction = len(data_upz_hotels)
    data_upz_hotels_args = list(f"{data_upz_hotels[i]}" for i in range(len(data_upz_hotels)))

    for i in range(0, len(data_upz_hotels), vpnFraction):        
        n1 = i 
        n2 = i+vpnFraction
        if n2 > len(data_upz_hotels):
           n2 = len(data_upz_hotels)
        # if n2 != len(data_upz_hotels) and i != 0:  
        #     yellowInput = input('Пожалуйста смените VPN', )
        #     if yellowInput:
        #         pass
        with WorkerPool(n_jobs = n) as p2:
            print('hello multi')                      
            finRes = p2.map(mather_controller, data_upz_hotels_args[n1:n2])
            finResArr.append(finRes)           
            # time.sleep(random.randrange(63,79))            
    for item in finResArr:
        total +=item

    writerr(total)     
    finRes = []
    finResArr = [] 
    total = []  

def writerr(total):
    print('hello total')
    # print(total)
    resPhoto = []
    resDescription = []
    resRevievs = []
    resFacilities = []
    resBlackList = []

    try:

        for t in total:
            resPhoto.append(t[0][0])
            resDescription.append(t[0][1])
            resRevievs.append(t[0][2])
            resFacilities.append(t[0][3])
            resBlackList.append(t[1]) 
        try:
            resPhoto = list(filter(None, resPhoto))
            resPhoto = list(filter([], resPhoto)) 
        except:
            pass
        try:
            resDescription = list(filter(None, resDescription))
            resDescription = list(filter([], resDescription)) 
        except:
            pass
        try:
            resRevievs = list(filter(None, resRevievs))
            resRevievs = list(filter([], resRevievs)) 
        except:
            pass

        try:
            resFacilities = list(filter(None, resFacilities))
            resFacilities = list(filter([], resFacilities)) 
        except:
            pass
        try:
            resBlackList = list(filter(None, resBlackList))
            resBlackList = list(filter([], resBlackList)) 
        except:
            pass 
    except Exception as ex:
        print(f"str342__{ex}")

    try:
        if resPhoto != None and resPhoto != []:
            try:
                with open(f'result_photos_upz_4.json', "w", encoding="utf-8") as file: 
                    json.dump(resPhoto, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str210__{ex}")
        if resDescription != None and resDescription != []:
            try:
                with open(f'result_description_upz_4.json', "w", encoding="utf-8") as file: 
                    json.dump(resDescription, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str216__{ex}") 
        if resRevievs != None and resRevievs != []:
            try:
                with open(f'result_review_upz_4.json', "w", encoding="utf-8") as file: 
                    json.dump(resRevievs, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}") 

        if resFacilities != None and resFacilities != []:
            try:
                with open(f'result_facilities_upz_4.json', "w", encoding="utf-8") as file: 
                    json.dump(resFacilities, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}") 

        if resBlackList != None and resBlackList != []:
            try:
                with open(f'black_list_1.json', "w", encoding="utf-8") as file: 
                    json.dump(resBlackList, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str226__{ex}") 



        # if total[0][4][0] != None and total[0][4] != []:
        #     try:
        #         with open(f'result_rooms_upz_1.json', "w", encoding="utf-8") as file: 
        #             json.dump(total[0][4][0], file, indent=4, ensure_ascii=False)
        #     except Exception as ex:
        #         print(f"str237__{ex}") 

        # if total[0][5][1] != None and total[0][5][1] != []:
        #     try:
        #         with open(f'upz_hotels_rooms_blocks_1.json', "w", encoding="utf-8") as file: 
        #             json.dump(total[0][5][1], file, indent=4, ensure_ascii=False)
        #     except Exception as ex:
        #         print(f"str242__{ex}") 

        # if total[0][6][2] != None and total[0][6][2] != []:
        #     try:
        #         with open(f'upz_hotels_rooms_highlights_1.json', "w", encoding="utf-8") as file: 
        #             json.dump(total[0][6][2], file, indent=4, ensure_ascii=False)
        #     except Exception as ex:
        #         print(f"str248__{ex}") 
    except Exception as ex:
        print(f"str320__{ex}")
  
def main():
    start_time = time.time() 
    data_upz_hotels_all = json_reader_test.data_upz_hotels_func()[0] 
    data_upz_hotels = json_reader_test.data_upz_hotels_func()[1][4:5]
    # print(data_upz_hotels)
    father_multiprocessor(data_upz_hotels)
    finish_time = time.time() - start_time 
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    

if __name__ == "__main__":
    main() 


# python main.py 



# return [[result_photos_upz, result_description_upz, result_review_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks, upz_hotels_rooms_highlights], data_upz_hotels, black_list] 



# try:
#     title = ''
#     title = soup1.find('div', attrs={'id': 'hp_hotel_name'}).find('h2').get_text().strip()
#     print(title)

# except Exception as ex:
#     print(f"str175___{ex}")  



# t = [
#     [[[], [], [], [], [None]], ['2061186']],
#     [[[], [], [], [], [None]], ['3060101']],
#     [[[], [], [], [], [None]], ['543969']],
#     [[[], [], [], [], [None]], ['1037647']],
#     [[[], [], [], [], [None]], ['1654758']]
# ]

# https://www.booking.com/hotel/uz/hilton-tashkent-city.ru.html?dist=0&sb_price_type=total&type=total&group_adults=2&sid=52c12d695260d02d8a98fb123e5b9e1e&label=gen173nr-1BCAso7gFCFGhpbHRvbi10YXNoa2VudC1jaXR5SDNYBGjkAYgBAZgBIbgBGcgBDNgBAegBAYgCAagCA7gC6O2KogbAAgHSAiQ0MTA3MTA1Mi03ZjhkLTQ1NTktODE3YS1lZDQ4NzQ3Y2I4ZmPYAgXgAgE&keep_landing=1#tab-reviews



