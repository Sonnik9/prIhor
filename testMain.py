import requests
import random 
from random import choice
import time
import json
import math
import re
import smart_headers, json_reader_test, photos_func, description_func, faciclities_func, rooms_func, rooms_block_func, writerr, b_filter_func, b_writerr_func

import atexit
import shutil
import tempfile
import sys 

# from requests_html import HTMLSession
# from datetime import datetime
# import aiohttp
# import asyncio
# import asyncio
# import multiprocessing
# from mpire import WorkerPool
# from lxml import etree
# from lxml import html
# from requests import *
# from bs4 import BeautifulSoup
# db_handler
# proxy_generator
# scraper_gr_mather_func

# ////////// grendMather_controller block/////////////////////////////////////

def grendMather_controller(data):
    flagCount = 0
    flagTest = True
    flag_photo = True
    flag_description = True 
    flag_facilities = True 
    flag_room = True 
    flag_room_block = True
    white_list = []
    black_list = []
    photoInd = 0
    descriptionInd = 0
    facilityInd = 0
    roomInd = 0
    room_blockInd = 0
    try:
        data_upz_hotels_item = data.split('SamsonovNik')[1]
    except Exception as ex:
        print(f"48____{ex}")
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except Exception as ex:
        print(f"53____{ex}")
        data_upz_hotels_item_dict = data_upz_hotels_item 
    # try:
    #     print(f"55__{data_upz_hotels_item_dict}")
    # except Exception as ex:
    #     print(f"57____{ex}")
    try:
        hotelid = data_upz_hotels_item_dict["hotel_id"] 
    except Exception as ex:
        print(f"61____{ex}")
        hotelid = 'not found'
    try:
        prLi_str = data.split('SamsonovNik')[0]
        try:
            prLi = eval(prLi_str)
        except Exception as ex:
            print(f"str68___{ex}")
            prLi = prLi_str
            pass
    except Exception as ex:
        print(f"str72___{ex}")
        pass 
    try:
        link = ''
        link = data_upz_hotels_item_dict["url"] 
        try:
            fixed_url = re.sub(r'\\/', '/', link)  
        except Exception as ex:
            print(f"74____{ex}")
            fixed_url = data_upz_hotels_item_dict["url"]
    except Exception as ex:
        print(f"str83___{ex}")
        try:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "?": '?',
            })
        except Exception as ex:
            print(f"91____{ex}")
        return [[None], white_list, black_list] 
    try:
        photoInd = data_upz_hotels_item_dict["fotos"]
    except:
        pass 
    try:
        descriptionInd = data_upz_hotels_item_dict["description"]
    except:
        pass 
    try:
        facilityInd = data_upz_hotels_item_dict["facility"] 
    except:
        pass
    try:
        roomInd = data_upz_hotels_item_dict["room"]
    except:
        pass
    try:
        room_blockInd = data_upz_hotels_item_dict["room_block"]
    except:
        pass
     

    if photoInd == "1" or photoInd == 1:
        flag_photo = False
        flagCount += 1  
    if descriptionInd == "1" or descriptionInd == 1:
        flag_description = False
        flagCount += 1 
    if facilityInd == "1" or facilityInd == 1:
        flag_facilities = False
        flagCount += 1 
    if roomInd == "1" or roomInd == 1:
        flag_room = False
        flagCount += 1
    if room_blockInd == "1" or room_blockInd == 1:
        flag_room_block = False
        flagCount += 1

    if flagCount == 5 and flagTest != True:
        white_list.append({
            "hotel_id": hotelid,
            "url": fixed_url,             
        })    
        return [[None], white_list, black_list] 
    
    else:
        for _ in range(2):
            try:
                result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = '', '', '', '', ''
                white_list = []
                black_list = []
                proxy_item = {       
                    "https": f"http://{choice(prLi)}"          
                } 
                k = 2 / random.randrange(1, 5)
                m = 1 / random.randrange(1, 11)
                g = random.randrange(1, 5)
                n = round(g + k + m, 2) 
                time.sleep(n)  
                try:        
                    r = requests.get(fixed_url, headers=smart_headers.random_headers(), proxies=proxy_item, timeout=(3.15, 21.15))
                    r.raise_for_status()
                    # print(r.status_code)
                    if r.status_code == 404: 
                        return None
                    if r.status_code == 200 and r.text is not None and r.text != '':
                        try:
                            # result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = scraper_gr_mather_func.scraper_grendmather(r.text, hotelid, photoInd, descriptionInd, facilityInd, roomInd)
                            # if flag_photo == True or flagTest == True:
                            #     try:
                            #         result_photos_upz = photos_func.page_scraper_photos(r.text, hotelid)
                            #     except:
                            #         result_photos_upz = None  
                            if flag_facilities == True or flagTest == True:
                                try:
                                    result_facilities_upz = faciclities_func.page_scraper_facilities(r.text, hotelid)
                                except:
                                    result_facilities_upz = None
                            # if flag_description == True or flagTest == True:
                            #     try:                       
                            #         result_description_upz = description_func.page_scraper_description(r.text, hotelid)                           
                            #     except:
                            #         result_description_upz = None 
                            #         # print(result_description_upz)
                            # if flag_room == True or flagTest == True:
                            #     try:
                            #         result_rooms_upz = rooms_func.page_scraper_room(r.text, hotelid)
                            #     except:
                            #         result_rooms_upz = None 

                            # if flag_room_block == True or flagTest == True:
                            #     try:
                            #         upz_hotels_rooms_blocks = rooms_block_func.page_scraper_room_block(r.text, hotelid)
                            #     except:
                            #         upz_hotels_rooms_blocks = None 
                            if result_photos_upz is None or result_description_upz is None or result_facilities_upz is None or result_rooms_upz is None or upz_hotels_rooms_blocks is None:
                                continue
                            elif result_photos_upz is not None and result_description_upz is not None and result_facilities_upz is not None and result_rooms_upz is not None and upz_hotels_rooms_blocks is not None:
                                white_list.append({
                                    "hotel_id": hotelid,
                                    "url": fixed_url,             
                                })
                                break                           
                        except Exception as ex:
                            # print(f"str225___{ex}")
                            # continue
                            pass
                        break
                    else:
                        continue
                except requests.exceptions.HTTPError as ex:
                    # print(f"str44___HTTP error occurred: {ex}") 
                    continue

            except Exception as ex:
                # print(f"237____{ex}")
                continue
                # return [[None], black_list] 
        if (flag_photo == True or flagTest == True) and result_photos_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "fotos": 0,
            })
        if (flag_description == True or flagTest == True) and result_description_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "description": 0,
            })

        if (flag_facilities == True or flagTest == True) and result_facilities_upz is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "facility": 0,
            }) 
        if (flag_room == True or flagTest == True) and result_rooms_upz is None:
            # print("room condition")
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "room": 0,
            })

        if (flag_room == True or flagTest == True) and upz_hotels_rooms_blocks is None:
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "room_block": 0,
            })        
        try:
            return [[result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks, None], white_list, black_list] 
        
        except Exception as ex:
            # print(f"220____{ex}")
            black_list.append({
                "hotel_id": hotelid,
                "url": fixed_url,
                "?": '?',
            })
            return [[None], white_list, black_list] 
        
# ////////// grendMather_controller block end/////////////////////////////////////

        
def proxy_reader():
    with open("proxy_booking.txt", encoding="utf-8") as f1:    
        prLi = ''.join(f1.readlines()).split('\n')
        prLi= list(i.strip() for i in prLi)
        prLi = list(filter(lambda item: item != '', prLi))
    return prLi

def father_multiprocessor(data_upz_hotels):
    from mpire import WorkerPool   
    # n = multiprocessing.cpu_count() * 10  
    try:
        data_upz_hotels_new = eval(data_upz_hotels) 
    except Exception as ex:
        print(f"277____{ex}")
        data_upz_hotels_new = data_upz_hotels
    # try:
    #     print(data_upz_hotels[1])
    # except Exception as ex:
    #     print(f"246____{ex}")
    try:
        prLi = proxy_reader()
    except Exception as ex:
        print(f"283____{ex}")
    try:
        n = 22
        data_upz_hotels_args = list(f"{prLi}SamsonovNik{item}" for item in data_upz_hotels_new)
    except Exception as ex:
        print(f"288____{ex}")
    try:
        with WorkerPool(n_jobs = n) as p2:
            print('hello multi')                                
            finRes = p2.map(grendMather_controller, data_upz_hotels_args)
    except Exception as ex:
        print(f"295____{ex}")
    # writerr.writerr(finRes) 
    try:  
        return finRes
    except Exception as ex:
        print(f"300____{ex}")
        return None



def cycles_worker(var_data, n1, n2, const_data, counter, flag_end_cycles, flag_choice):
    finRes = []
    black_list = []

    try:
        if flag_end_cycles == True and flag_choice == True:
            return print('Finish')
    except Exception as ex:
        print(f"334____{ex}")

    if flag_choice == True:
        interval_chekcer = len(const_data) - n2
        # print(f"357___{interval_chekcer}")
        # print(f"358___{len(const_data)}")
        try:
            if interval_chekcer <= 100:
                n2 = len(const_data)
                flag_end_cycles = True
                print(f"362___{n2}")
        except Exception as ex:
            print(f"343____{ex}")
        # print(f"348___{n1, n2}")
        start_time = time.time() 
        var_data = const_data[n1:n2]
        try:
            finRes = father_multiprocessor(var_data)
        except Exception as ex:
            print(f"374____{ex}")
        try:
            writerr.writerr(finRes, n1, n2)
        except Exception as ex:
            print(f"378____{ex}")

        finish_time = time.time() - start_time 
        print(f"Total time for working of {n1}__{n2} items:  {math.ceil(finish_time)} сек")

        try:
            black_list = b_filter_func.black_filter(finRes) 
        except Exception as ex:
            print(f"390____{ex}")
        print(black_list)
        return
        try:
            var_data = black_list
            n1 = 0
            n2 = len(black_list)
            counter +=1
            flag_choice = False
            # print(f"375___{type(black_list)}")
            # print(f"376___{len(black_list)}")
        except Exception as ex:
            print(f"398____{ex}")

        cleanup_cache()
        try:
            cycles_worker(var_data, n1, n2, const_data, counter, flag_end_cycles, flag_choice) 
        except Exception as ex:
            print(f"408____{ex}")
    else:
        # print('sec cycle')
        start_time = time.time() 
        try:
            var_data = var_data[n1:n2]
            # print(f"394__{type(var_data)}")
            # print(f"395__{len(var_data)}")
        except Exception as ex:
            print(f"415____{ex}")
        # try:
        #     print(f"399__{var_data[0]}")
        # except Exception as ex:
        #     print(f"418____{ex}")
        try:
            finRes = father_multiprocessor(var_data)
        except Exception as ex:
            print(f"422____{ex}")
        try:
            black_list = b_filter_func.black_filter(finRes) 
        except Exception as ex:
            print(f"409____{ex}")
        # try:
        #     print(f"425___{black_list}")
        # except Exception as ex:
        #     print(f"427____{ex}")
        try:
            writerr.writerr(finRes, n1, n2)
        except Exception as ex:
            print(f"378____{ex}")
        try:
            if flag_end_cycles == True:
                b_writerr_func.b_w_writerr(black_list, n1, n2)
                finish_time = time.time() - start_time
                print(f"Total time for reworking of black_list: {math.ceil(finish_time)} сек")
        except Exception as ex:
            print(f"433____{ex}")
        try:
            var_data = const_data
            n1 = (counter*100) - 100
            n2 = counter*100  
            flag_choice = True 
        except Exception as ex:
            print(f"439____{ex}")
        cleanup_cache()   
        try:  
            cycles_worker(var_data, n1, n2, const_data, counter, flag_end_cycles, flag_choice)
        except Exception as ex:
            print(f"444____{ex}")

def cleanup_cache():
    import os
    print('cache')
    try:
        cache_dir = tempfile.mkdtemp()
    except Exception as ex:
        print(f"386____{ex}")
    
    try:
        if os.path.exists("__pycache__"):
            shutil.rmtree("__pycache__")
    except Exception as ex:
        print(f"392____{ex}")
    
    try:
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir)
    except Exception as ex:
        print(f"396____{ex}")
  
def main():
    # start_time = time.time() 
    try:   
        data_upz_hotels_renevate = json_reader_test.data_upz_hotels_func() 
        var_data = data_upz_hotels_renevate
        const_data = data_upz_hotels_renevate
    except Exception as ex:
        print(f"443____{ex}")

    # for url in data_upz_hotels_renevate:        
    #     print(url["url"])
    #     print(url["hotel_id"])
    # return
    # print(data_upz_hotels_renevate[0]["url"])
    fixed_url = 'https://www.booking.com/hotel/vn/vinpearl-resort-spa.html'  
    r = requests.get(fixed_url, headers=smart_headers.random_headers(), timeout=(3.15, 21.15))
    
    with open('faci_256084_.html', 'w', encoding='utf-8') as f:
        f.write(r.text) 
    # return
    # white_list, black_list = father_multiprocessor(var_data)
    # finish_time = time.time() - start_time
    # print(f"Total time for working:  {math.ceil(finish_time)} сек")  
    return
    n1 = 0
    n2 = 100
    counter = 1
    flag_cycles = False
    flag_choice = True
    try:
        cycles_worker(var_data, n1, n2, const_data, counter, flag_cycles, flag_choice)
    except Exception as ex:
        print(f"454____{ex}")

if __name__ == "__main__":
    try:
        atexit.register(cleanup_cache)
    except Exception as ex:
        print(f"461____{ex}")
    main() 
    # cleanup_cache()
    try:
        sys.exit()
    except Exception as ex:
        print(f"467____{ex}")


# python testMain.py 

# t = [
#     [[[], [], [], [], [None]], ['2061186']],
#     [[[], [], [], [], [None]], ['3060101']],
#     [[[], [], [], [], [None]], ['543969']],
#     [[[], [], [], [], [None]], ['1037647']],
#     [[[], [], [], [], [None]], ['1654758']]
# ]


# for url in data_upz_hotels:
#     urls_list.append(url["url"]) 
# try:
#     with open(f'urls_list_1-50.json', "w", encoding="utf-8") as file: 
#         json.dump(urls_list, file, indent=4, ensure_ascii=False)
# except Exception as ex:
#     print(f"str226__{ex}") 

# asyncio.run(async_father_multiprocessor(data_upz_hotels))


# https://www.booking.com/hotel/vn/the-seashell.html
# 2475885

# https://www.booking.com/hotel/vn/vinpearl-resort-spa.html
# 256084

# https://www.booking.com/hotel/vn/mia-resort-nha-trang.html
# 398814

# https://www.booking.com/hotel/vn/ha-long-royal.html
# 505289

# https://www.booking.com/hotel/vn/rex.html
# 71004

# https://www.booking.com/hotel/vn/renaissance-riverside-saigon.html
# 172294

# https://www.booking.com/hotel/vn/elegant-suites-westlake.html
# 1123472

# https://www.booking.com/hotel/vn/sheraton-grand-danang-resort.html
# 2944240

# https://www.booking.com/hotel/vn/worldhotel-amiana-nha-trang.html
# 545839

# https://www.booking.com/hotel/vn/risemount-resort-danang.html
# 1996992

