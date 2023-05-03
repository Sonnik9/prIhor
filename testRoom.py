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
                    # with open('room_test_Req_4.html', 'w', encoding='utf-8') as f:
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
    result_room_upz = []
    result_room_upz_list = []  
    responss_count = 0 

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
        # with open('all_scripts_en_6.html', 'w', encoding='utf-8') as f:
        #     f.write(all_scripts_str) 
        #     return
        scripts_fraction_list = all_scripts_str.split('{}')
        section = soup1.find('section', class_='roomstable')
        list_elements = section.find_all('div', recursive=False)
        for i, item in enumerate(list_elements):
            room_id = 'not found'
            name_room = 'not found'
            endescription = 'not found'
            allow_children = 'not found'
            private_bathroom_highlight = 'not found'
            apartament_photo_list = []
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
 
            try:
                bed_config = ''
                bed_index = []
                pattern_bed = r'\b\d.*?(?:bed|beds)'
                all_bed_text = item.get_text(strip=True, separator="\n").split('\n')
                for i, item in enumerate(all_bed_text):
                    matches_bed = re.search(pattern_bed, item)
                    if matches_bed:
                       bed_index.append(i) 
                try:
                    bed_config = ' '.join(all_bed_text[bed_index[0]:bed_index[-1]+1])                        
                except:
                    try:
                        bed_config = ' '.join(all_bed_text[bed_index[0]])
                    except:
                        bed_config = 'not found'
                # print(bed_config)
                # continue

            except:
                bed_config = 'not found'
            # continue
            try:                
                pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                # pattern3 = f'RTRoomPhoto:\d+'            
                for fr in scripts_fraction_list:
                    match1 = re.search(pattern1, fr)                   
                    if match1:
                        match_general_block = match1.group()
                        #    print(match_general_block)
                        try:
                            match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                            count_allow_children = match_allow_children.group().split(':')[1].strip() 
                            # print(match_allow_children.group())
                            # print(count_allow_children)
                            # continue
                        except:
                            match_allow_children = 'not found'
                            # allow_children = '0'
                        try:
                            allow_children = int(count_allow_children)
                            if allow_children and allow_children >0:
                                allow_children = '1'
                            else:
                                allow_children = '0'
                            # print(allow_children)  
                        except:
                            allow_children = 'not found'                           
                        # print(allow_children) 
                        # continue
                        try:
                            private_bathroom_highlight = ''
                            try:
                                bathroom_facilities_list = []
                                try:
                                    bathroom_facilities_pre = re.search(r'"BATHROOM_PRIVATE","facilities":\[[^]]*?\]', match_general_block)
                                    bathroom_facilities_match = bathroom_facilities_pre.group()
                                    bathroom_facilities_list = int(eval(bathroom_facilities_match.split('"BATHROOM_PRIVATE"')[1].split(':')[1].strip()))
                                except:
                                    try:
                                        bathroom_facilities_list = int(eval(match_general_block.split('"BATHROOM_PRIVATE"')[1].split('"facilities"')[1].split('"__typename"')[0][1:-3].strip()))
                                        
                                    except:
                                        pattern3 = r'\[(.*?)\]'
                                        match_facilities = re.search(pattern3, bathroom_facilities_match)
                                        bathroom_facilities_list = eval(match_facilities.group())
                                        # print(f"ok_____{bathroom_facilities_list}")
                                # print(bathroom_facilities_list)
                            except:
                                bathroom_facilities_list = []
                            try:
                                for fs in bathroom_facilities_list:
                                    private_bathroom_highlight += facilities_data.roomfacility[str(fs)] +'\n'
                                    
                            except:                                
                                pass 
                        except:
                            private_bathroom_highlight = 'not found'
                        try:
                           endescription = match_general_block.split('"description":')[1].split('","hasRoomInventory"')[0][1:]                        
                        except Exception as ex:
                            print(f"202____{ex}") 
                            endescription = 'not found'

                        try:
                            match_photos_block = match_general_block.split('"photos":[')[1].split(',"isSmoking"')[0]
                            photo_id_list_pre = eval(f"[{match_photos_block}")                     
                            for ind in photo_id_list_pre:
                                indInd = ind['__ref'].split(':')[1].strip()
                                subInd =  indInd[:3]
                                room_photo_link = f"https://cf.bstatic.com/images/hotel/max1024x768/{subInd}/{indInd}.jpg"
                                apartament_photo_list.append(room_photo_link)
                        except Exception as ex:
                            apartament_photo_list = 'not found'
                            print(f"215____{ex}") 
            except Exception as ex:
                print(f"140____{ex}")  
            try:
                result_room_upz_list.append({
                    'room_id': str(room_id), 
                    'name_room': str(name_room), 
                    'endescription': str(endescription), 
                    'allow_children': str(allow_children),
                    'apartament_photo_list': str(apartament_photo_list),
                    'private_bathroom_highlight': str(private_bathroom_highlight),
                    'bed_configurations': bed_config,
                })
            except Exception as ex:
                print(f"150____{ex}") 
        # return

            
        # with open('bed_configurations_5.html', 'w', encoding='utf-8') as f:
        #     f.write(match_bed_configurations_all) 
            # return 

       
    except Exception as ex:
        responss(data_upz_hotels)  
        print(f"154____{ex}")

    try:
        result_room_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_room_upz_list": result_room_upz_list,            
        })
    except Exception as ex:
        print(f"str163___{ex}") 
    # print(ok)
    try:
        try:
            with open(f'room_upz_Test_16.json', "w", encoding="utf-8") as file: 
                json.dump(result_room_upz, file, indent=4, ensure_ascii=False)
        except Exception as ex:
            print(f"str210__{ex}")
        return
        # return print(result_room_upz[0])
    except:
        return None

def main():
    start_time = time.time() 
    data_upz_hotels_all = json_reader_test.data_upz_hotels_func()[0] 
    data_upz_hotels = json_reader_test.data_upz_hotels_func()[1][2]
    # print(data_upz_hotels["url"])
    responss(data_upz_hotels)

    finish_time = time.time() - start_time 
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    

if __name__ == "__main__":
    main() 



# try:
#                             # "category":"BATHROOM_PRIVATE","facilities":[27,4,100,31,43,12,141]
#                             match_bathroomCount = re.search(r'"bathroomCount":\d', match_general_block)
#                             private_bathroom_highlight = match_bathroomCount.group().split(':')[1].strip() 
                            
#                             # continue
#                         except:
#                             private_bathroom_highlight = '' 



                    #    try:
                    #         pattern2 = r'"apartmentRooms":\[(?!\]).*'
                    #         match_bed_configurations = re.search(pattern2, match_general_block)
                    #         # print(match_bed_configurations)

                    #         match_bed_configurations_all += str(match_bed_configurations.group()) + '\n\n\n'
                    #         # print(match_bed_configurations.group())
                    #         # continue                            
                    #         bed_configurations_pre = eval(match_bed_configurations.group().split(',"bathroomCount"')[0].split('"apartmentRooms":')[1])
                    #         # print(bed_configurations_pre)
                    #         # continue
                    #         for bed in bed_configurations_pre:
                    #             try:
                    #                 bed_configurations += int(bed['beds'][0]['count'])
                                    
                    #             except:
                    #                 bed_configurations = 0
                    #         # print(bed_configurations) 
                    #         # continue
                    #     except Exception as ex:
                    #         print(f"189___{ex}")
                    #         bed_configurations = 'not found'
                    #     # "apartmentRooms"
                    #     # continue 