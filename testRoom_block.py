# https://www.booking.com/hotel/us/mount-princeton-hot-springs-resort.ru.html?sid=52c12d695260d02d8a98fb123e5b9e1e&srpvid=df1f82463ac8015f&req_adults=2&hpos=1&srepoch=1681929102&req_children=0&group_children=0&room1=A%2CA&hapos=1&aid=304142&sb_price_type=total&no_rooms=1&ucfs=1&type=total&dist=0&sr_order=popularity&group_adults=2&label=gen173nr-1FCBcoggI46AdIM1gEaOkBiAEBmAEhuAEZyAEM2AEB6AEB-AECiAIBqAIDuAL85YCiBsACAdICJGUyMmM5YjU2LTdiNjUtNDBhNy04NDZjLTg4NTYwOGUxMDIyNtgCBeACAQ#room_105563103 



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
import smart_headers, json_reader_test, facilities_data



def responss(data_upz_hotels_item):
    flagCount = 0
    flagTest = True
    result_review_upz = []
    black_list = []
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except:
        data_upz_hotels_item_dict = data_upz_hotels_item


    hotelid = data_upz_hotels_item_dict["hotel_id"] 

    roomInd = data_upz_hotels_item_dict["room"]
    # print('ok var')

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
                r = requests.get(fixed_url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
                r.raise_for_status()
                print(r.status_code) 
                if r.status_code == 200:
                    # with open('room_ru_test_block_1.html', 'w', encoding='utf-8') as f:
                    #     f.write(r.text)
                    # return
                        
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

        if (roomInd  != "1" and roomInd != 1) or flagTest == True:
            result_review_upz.append(page_scraper_otziv(data_upz_hotels_item_dict, resHtml))

def page_scraper_otziv(data_upz_hotels, resHtml):
    meal_facilities_const = [1, 166, 167, 168, 169, 170, 171, 217, 218, 219, 220]
    result_room_block_upz = []
    result_room_block_upz_list = []

    try:
       hotelid = data_upz_hotels["hotel_id"] 
    except:
        pass
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")
    except Exception as ex:
        print(f"str102___{ex}") 

    try:
        all_sripts_list = []
        scripts_fraction_list = []
        all_scripts_str = ''
        all_sripts_list = soup1.find_all('script')
        for fr in all_sripts_list:
            all_scripts_str += str(fr) + '\n'
        scripts_fraction_list = all_scripts_str.split('{}')           
        section = soup1.find('section', class_='roomstable')
        list_elements = section.find_all('div', recursive=False)
        for i, item in enumerate(list_elements):
            room_id = ''
            name_room = ''
            gross_price = 'api info'
            currency = 'api info'
            max_occupancy = ''
            nr_children = ''
            nr_adults = ''
            mealplan = ''
            all_inclusive = 'not found'
            room_surface_in_m2 = 'not found' 
            all_facilities_of_room = ''
            
            try:
                room_id_pre = item.find('a').get('href')            
                room_id = re.findall('\d+', room_id_pre)[0]                
            except:
                room_id = 'not found'
                continue
            # print(room_id)
            try:
                name_room_pre = item.find('a')
                name_room = name_room_pre.get_text(strip=True, separator="\n")
            except:
                name_room = 'not found'
                continue 
            # print(name_room)
# "maxPersons":2,"maxChildren":0,"maxGuests":3
            try:
                for element in item.find_all(True):
                    aria_label = element.get('aria-label')
                    if aria_label:
                        max_occupancy = aria_label.strip()
                        # print(aria_label)
                        break
            except:
                max_occupancy = 'not found'

            try:            
                pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                # pattern_meal = r'(?:"mealPlans"::\[[^]]*?\]|"mealPlans":^\[\s*\]$)'
                pattern_meal = f'"facilities":\[[^]]*?\]'
                for fr in scripts_fraction_list:
                    match1 = re.search(pattern1, fr)                                   
                    if match1:
                        match_general_block = match1.group()
                        # print('True')
                        try:
                            match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                            nr_children = match_allow_children.group().split(':')[1].strip() 
                        except:
                            nr_children = 'not found'
                        try:
                            match_nr_adults = re.search(r'"maxPersons":\d', match_general_block)
                            nr_adults = match_nr_adults.group().split(':')[1].strip() 
                        except:
                            nr_adults = 'not found'
                        try:
                            match2 = re.findall(pattern_meal, str(match_general_block))
                            list_fs_meal = []
                            meal_facilities_set_list = []
                            if match2:
                                for mf in match2:
                                    list_fs_meal += eval(mf.split(':')[1].strip())
                            # print(list_fs_meal)
                            meal_facilities_set_list = list(set(list_fs_meal))
                            # print(meal_facilities_set_list)
                            common_facilities_items = [item for item in meal_facilities_const if item in meal_facilities_set_list]
                            # print(common_facilities_items)
                            if common_facilities_items:
                                for fs in common_facilities_items:
                                    mealplan += facilities_data.roomfacility[str(fs)] +'\n' 
                            else:
                                # mealplan = "There was not finding mealplan's information"
                                mealplan = "not found"
                        except:
                            mealplan = "not found"
                        
                        try:
                            for fs in meal_facilities_set_list:
                                all_facilities_of_room += facilities_data.roomfacility[str(fs)] +'\n'
                        except:
                            all_facilities_of_room = "not found"                
            except:
                try:
                    max_occupancy2 = max_occupancy             
                    nr_children = max_occupancy.split(',')[1].strip()                    
                except: 
                    nr_children = 'not found'                
                try:
                    nr_adults = max_occupancy2.split(',')[0].strip()
                except:
                    nr_adults = 'not found'           
            try:
                result_room_block_upz_list.append({
                    'room_id': str(room_id), 
                    'room_name': str(name_room),
                    'gross_price': str(gross_price), 
                    'currency': str(currency),                    
                    'nr_children': str(nr_children),
                    'max_occupancy': str(max_occupancy),
                    'mealplan': mealplan,
                    'room_surface_in_m2': room_surface_in_m2,
                    'nr_adults': nr_adults,
                    'all_inclusive': all_inclusive,
                    'all_facilities_of_room': all_facilities_of_room,
                })
            except Exception as ex:
                print(f"150____{ex}") 
        # return

    except Exception as ex:
        # responss(data_upz_hotels)  
        print(f"154____{ex}")

    try:
        result_room_block_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_room_block_upz_list": result_room_block_upz_list,            
        })
    except Exception as ex:
        print(f"str163___{ex}") 
    # print(ok)
    try:
        try:
            with open(f'room_blok_upz_test_3.json', "w", encoding="utf-8") as file: 
                json.dump(result_room_block_upz, file, indent=4, ensure_ascii=False)
        except Exception as ex:
            print(f"str210__{ex}")
        return
        # return print(result_room_upz[0])
    except:
        return None

def main():
    start_time = time.time() 
    # data_upz_hotels_all = json_reader_test.data_upz_hotels_func()[0] 
    data_upz_hotels = json_reader_test.data_upz_hotels_func()[1][9]
    # print(data_upz_hotels["url"])

    responss(data_upz_hotels)

    finish_time = time.time() - start_time 
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    

if __name__ == "__main__":
    main() 




    # my_list = []

    # if re.match(r'^\[\s*\]$', str(my_list)):
    #     print("The list is empty!")
    # else:
    #     print("The list is not empty.")
    # return 

    # list_a = [10]
    # list_b = [0, 1, 2, 3, 4]

    # if set(list_a).issubset(set(list_b)):
    #     print("List A is a subset of list B")
    # else:
    #     print("List A is not a subset of list B")
    # list_a = [1, 10, 3]
    # list_b = [0, 1, 2, 3, 4]

    # common_items = [item for item in list_a if item in list_b]

    # print(common_items)
    # return