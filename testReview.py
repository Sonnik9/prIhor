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
import smart_headers, json_reader_test



def responss(data_upz_hotels_item):
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
    # print(data_upz_hotels_item)
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
        print('ok')
        # print(data_upz_hotels_item_dict)
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
            link = data_upz_hotels_item_dict["url"] 
            fixed_url = re.sub(r'\\/', '/', link)
            # print(fixed_url)
            reworked_title = fixed_url.split('/')[-1].split('.')[0].strip()         
            reworked_link  = f'https://www.booking.com/reviewlist.ru.html?cc1=vn&pagename={reworked_title}&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&offset=0&rows=100&rurl=&text=&'

        except Exception as ex:
            print(f"str199___{ex}")
            return [[None], black_list] 
        for sesCountt in range(3):
            r = ''
            k = 2 / random.randrange(1, 5)
            m = 1 / random.randrange(1, 11)
            g = random.randrange(1, 5)
            n = round(g + k + m, 2) 
            time.sleep(n)  
            try:  
                print('hello req')                    
                r = requests.get(reworked_link, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
                r.raise_for_status()
                print(r.status_code) 
                if r.status_code == 200:
                #    with open('review_test_doubleReq_2.html', 'w', encoding='utf-8') as f:
                #         f.write(r.text)
                        
                   break

            except requests.exceptions.HTTPError as ex:
                print(f"HTTP error occurred: {ex}")

            except Exception as ex:
                print(f"str214___{ex}") 
                if sesCountt == 2:
                    return [[None], black_list] 
                else:
                    continue 
        try:
            resHtml = r.text           
        except Exception as ex:
            print(f"249____{ex}")

        if (otzivInd != "1" and otzivInd != 1) or flagTest == True:
            result_review_upz.append(page_scraper_otziv(data_upz_hotels_item_dict, resHtml))

def page_scraper_otziv(data_upz_hotels, resHtml):
    result_review_upz = []
    result_review_upz_list = []
    try:
       hotelid = data_upz_hotels["hotel_id"] 
    except:
        pass
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")
    except Exception as ex:
        print(f"str226___{ex}") 

    try:
        print('hello finder')
        review_block = soup1.find('ul', attrs={}).find_all('li', class_='review_list_new_item_block')
        print(len(review_block))
        for item in review_block:
            try:
                title = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get_text().strip()
                print(title)               
            except Exception as ex:
                title = 'not found'
                print(f"str129___{ex}")
            try:
                pros = item.find('p').find('span', class_='c-review__body').get_text().strip()
                print(pros)              
            except Exception as ex:
                pros = 'not found' 
                print(f"str129___{ex}")
            try:
                cons = item.find_all('p')[1].find('span', class_='c-review__body').get_text().strip()
                print(cons)
            except Exception as ex:
                cons = 'not found' 
                print(f"str129___{ex}") 
            try:
                dt1 = item.find_all('span', class_='c-review-block__date')[1].get_text().split(':')[1].strip()
                print(dt1)
            #    break
            except Exception as ex:
                dt1 = 'not found'
                print(f"str129___{ex}") 
            try:
                average_score = item.find('div', class_='bui-review-score__badge').get_text().strip()
                print(average_score)
            #    break
            except Exception as ex:
                average_score = 'not found'
                print(f"str129___{ex}") 
            try:
                author_name = item.find('span', class_='bui-avatar-block__title').get_text().strip()
                print(author_name)
            #    break
            except Exception as ex:
                author_name = 'not found'
                print(f"str129___{ex}") 
            try:
                room_id = item.find('div', class_='bui-list__body').get_text().strip()
                print(room_id)
            #    break
            except Exception as ex:
                room_id = 'not found'
                print(f"str129___{ex}") 
            try:
                checkinBlock = item.find_all('div', class_='bui-list__body')[1]
                #    print(checkinBlock)
                checkin = checkinBlock.get_text(strip=True, separator="\n")
                print(checkin)
                #    break
            except Exception as ex:
                checkin = 'not found'
                print(f"str129___{ex}") 
            try:
                checkout = checkin 
            except Exception as ex:
                checkout = 'not found'
                print(f"str129___{ex}") 
            try:                
                languagecode = '?'
            except Exception as ex:
                print(f"str129___{ex}") 

            result_review_upz_list.append({
                "title": title, 
                "cons": cons, 
                "pros":pros, 
                "dt1": dt1, 
                "average_score": average_score, 
                "author_name": author_name, 
                "room_id":room_id, 
                "checkin": checkin, 
                "checkout": checkout, 
                "languagecode": languagecode,                
            })
            print(len(result_review_upz_list))

    except Exception as ex:
        print(f"str226___{ex}") 
    try:
        result_review_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_review_upz_list": result_review_upz_list,            
        })
    except Exception as ex:
        print(f"str226___{ex}") 
    try:
        return print(result_review_upz[0])
    except:
        return None

def main():
    start_time = time.time() 
    data_upz_hotels_all = json_reader_test.data_upz_hotels_func()[0] 
    data_upz_hotels = json_reader_test.data_upz_hotels_func()[1][7]
    # data_upz_hotels["url"] = 'https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&rows=100&offset=0'
    
    responss(data_upz_hotels)

    finish_time = time.time() - start_time 
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    

if __name__ == "__main__":
    main() 

    # review_list_new_item_block


#    https://www.booking.com/reviewlist.ru.html?&cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=10&rows=100&offset=970
#    https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=10&rows=100&offset=3900

# https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&rows=700&offset=0


# c-review-block__response__inner
