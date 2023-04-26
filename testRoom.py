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
import smart_headers, json_reader_test



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
                    # with open('room_test_Req_3.html', 'w', encoding='utf-8') as f:
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
    try:
       hotelid = data_upz_hotels["hotel_id"] 
    except:
        pass
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")
    except Exception as ex:
        print(f"str102___{ex}") 

    try:
        words = resHtml.split('{}')
        section = soup1.find('section', class_='roomstable')
        list_elements = section.find_all('div', recursive=False)
        # print(len(list_elements))
        for item in list_elements[1:]:
            room_id = ''
            name_room = ''
            endescription = ''
            allow_children = ''
            private_bathroom_highlight = ''
            bed_configurations = ''
            apartament_photo_list = []
            try:
                room_id_pre = item.find('a').get('href')            
                room_id = re.findall('\d+', room_id_pre)[0]
            except:
                rooom_id = 'not found'
            try:
                name_room_pre = item.find('a')
                name_room = name_room_pre.get_text(strip=True, separator="\n")
            except:
                rooom_id = 'not found'
            try:                
                pattern1 = f'"roomId":{room_id}.*__typename":"RTRoomCard".*"description".*"hasRoomInventory".*' 
                # pattern3 = f'RTRoomPhoto:\d+'            
                for word in words:
                    match1 = re.search(pattern1, word)                   
                    if match1:
                        match_general_block = match1.group()
                        #    print(match_general_block)
                        match_allow_children = re.search(r'"maxChildren":\d', match_general_block)
                        count_allow_children = match_allow_children.group().split(':')[1].strip()
                        try:
                            allow_children = int(count_allow_children)
                            if allow_children and allow_children >0:
                                allow_children = '1'
                            else:
                                allow_children = '0'
                            # print(allow_children)  
                        except:
                            allow_children = '0'
                           
                        print(allow_children)
                    #    match_general_block.split("maxChildren")[1]
                        return
                        endescription = match_general_block.split('"description":')[1].split('","hasRoomInventory"')[0] 
                        match_children_block  = ''
                        
                        match_photos_block = match_general_block.split('"photos":[')[1].split(',"isSmoking"')[0]
                        photo_id_list_pre = eval(f"[{match_photos_block}")
                        #    print(photo_id_list_pre)                       
                        for ind in photo_id_list_pre:
                            indInd = ind['__ref'].split(':')[1].strip()
                            subInd =  indInd[:3]
                            room_photo_link = f"https://cf.bstatic.com/images/hotel/max1024x768/{subInd}/{indInd}.jpg"
                            apartament_photo_list.append(room_photo_link)
                        #    print(apartament_photo_list)
            except Exception as ex:
                print(f"140____{ex}")  
            try:
                result_room_upz_list.append({
                    'rooom_id': rooom_id, 
                    'name_room': name_room, 
                    'endescription': endescription, 
                    'allow_children': allow_children,
                    'apartament_photo_list': apartament_photo_list,
                    'private_bathroom_highlight': private_bathroom_highlight,
                    'bed_configurations': bed_configurations,
                })
            except Exception as ex:
                print(f"150____{ex}") 

       
    except Exception as ex:
        print(f"154____{ex}")

    try:
        result_room_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_room_upz_list": result_room_upz_list,            
        })
    except Exception as ex:
        print(f"str163___{ex}") 
    try:
        return print(result_room_upz[0])
    except:
        return None

def main():
    start_time = time.time() 
    data_upz_hotels_all = json_reader_test.data_upz_hotels_func()[0] 
    data_upz_hotels = json_reader_test.data_upz_hotels_func()[1][7]
    data_upz_hotels["url"] = 'https://www.booking.com/hotel/vn/compass-parkview.html'
    # return

    # https://www.booking.com/hotel/vn/compass-parkview.html
    
    responss(data_upz_hotels)

    finish_time = time.time() - start_time 
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")
    

if __name__ == "__main__":
    main() 



    # https://cf.bstatic.com/xdata/images/hotel/square60/383202859.jpg?k=300baa767f2e12e8707693334c350187ad658da81d3010a572ec313e07f6828e&o=
    # https://www.booking.com/hotel/vn/compass-parkview.ru.html?label=gen173nr-&group_adults=2&group_children=0&keep_landing=1&no_rooms=1&sb_price_type=total&type=total&#room_
    # review_list_new_item_block


#    https://www.booking.com/reviewlist.ru.html?&cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=10&rows=100&offset=970
#    https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=10&rows=100&offset=3900

# https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&rows=700&offset=0


# "roomId":111370304,"__typename":"RTRoomCard","roomIndex":0,"roomTypeId":1,"name":"Апартаменты с 2 спальнями","description":"Offering city views, living and dining areas, spacious air-conditioned apartments come with a wardrobe and a flat-screen TV with cable/satellite channels. The en suite bathrooms have a bathtub or shower, hairdryer and free toiletries.","hasRoomInventory":true,"highlights":[{"__typename":"RTRoomPrivacyHighlight","privacyLevel":"PRIVACY_LEVEL_2"},{"__typename":"RTRoomSizeHighlight","areaValue":84},{"__ref":"RTRoomFacilityHighlight:110"},{"__ref":"RTRoomFacilityHighlight:121"},{"__ref":"RTRoomFacilityHighlight:11"},{"__ref":"RTRoomFacilityHighlight:38"},{"__ref":"RTRoomFacilityHighlight:75"},{"__ref":"RTRoomFacilityHighlight:79"},{"__ref":"RTRoomFacilityHighlight:3"},{"__ref":"RTHotelFacilityHighlight:107"}],"categorizedFacilities":[{"__typename":"RTFacilitiesWithCategory","category":"VIEW","facilities":[110,121]},{"__typename":"RTFacilitiesWithCategory","category":"BATHROOM_PRIVATE","facilities":[27,100,31,69,43,12,141]},{"__typename":"RTFacilitiesWithCategory","category":"OTHER","facilities":[23,6,82,75,84,26,139,8,125,76,68,116,11,138,74,126,132,39,83,215,13,77,124,134,137,184,91,22,3,18,70,86,9,41,95,79,44,73,85]}],"facilities":[27,6,100,31,77,69,82,124,125,184,116,23,26,18,76,8,43,22,9,44,73,12,39,41,91,13,70,86,68,83,84,74,95,85,126,132,137,138,139,141,134,215],"occupancy":{"__typename":"RTOccupancy","maxPersons":4,"maxChildren":1,"maxGuests":4},"hasSubUnits":true,"hasRoomPage":true,"bedConfigurations":[],"apartmentRooms":[{"__typename":"RTApartmentRoom","apartmentRoomId":62303275,"name":"Спальня 1","beds":[{"__typename":"RTBedType","count":1,"bedTypeId":6}]},{"__typename":"RTApartmentRoom","apartmentRoomId":62303276,"name":"Спальня 2","beds":[{"__typename":"RTBedType","count":1,"bedTypeId":3}]}],"bathroomCount":2,"photos":[{"__ref":"RTRoomPhoto:116076121"},{"__ref":"RTRoomPhoto:383202327"},{"__ref":"RTRoomPhoto:78416558"},{"__ref":"RTRoomPhoto:383205089"},{"__ref":"RTRoomPhoto:383205995"},{"__ref":"RTRoomPhoto:383202859"},{"__ref":"RTRoomPhoto:78656298"}],"isSmoking":false,"parkingInfo":{"__typename":"RTParkingInfo","hasParking":false},"nrStaysWithCheapestPriceForRoomLevelInventory":null,"onlyXLeftMessageDetails":null,"roomAvBlocks":[]},"RTRoomPhoto:48446605":{"id":48446605,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/48446605.jpg?k=730f97a0cbbbd6deec5613c27d1e77330ed33d20fe1ad8a9c7feaf2f30c6f8f3\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/48446605.jpg?k=730f97a0cbbbd6deec5613c27d1e77330ed33d20fe1ad8a9c7feaf2f30c6f8f3\u0026o=","ranking":10},"RTRoomPhoto:77788506":{"id":77788506,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/77788506.jpg?k=651536f0fa74d8931955f8d85db2e03df654b8be372a10febc52dfaee431d7af\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/77788506.jpg?k=651536f0fa74d8931955f8d85db2e03df654b8be372a10febc52dfaee431d7af\u0026o=","ranking":15},"RTRoomPhoto:77788348":{"id":77788348,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/77788348.jpg?k=4fe1a4215e52e0bc4b935192f602c8b04d2a289ec49746cc21f5dc7d64fb2141\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/77788348.jpg?k=4fe1a4215e52e0bc4b935192f602c8b04d2a289ec49746cc21f5dc7d64fb2141\u0026o=","ranking":25},"RTRoomPhoto:78417468":{"id":78417468,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/78417468.jpg?k=eed2badd729a54114de13777966ce33fc4b6bacaf3d0bcaa3558708dc13adc52\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/78417468.jpg?k=eed2badd729a54114de13777966ce33fc4b6bacaf3d0bcaa3558708dc13adc52\u0026o=","ranking":24},"RTRoomPhoto:36063679":{"id":36063679,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/36063679.jpg?k=0d3ea42db948d996cdc1022dd00c9001246c1cc31c43d689e6e4a784943aed81\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/36063679.jpg?k=0d3ea42db948d996cdc1022dd00c9001246c1cc31c43d689e6e4a784943aed81\u0026o=","ranking":0},"RTRoomCard:{\"roomId\":111370309}":{"roomId":111370309,"__typename":"RTRoomCard","roomIndex":1,"roomTypeId":9,"name":"Двухместный номер Делюкс с 1 кроватью","description":"Двухместный номер с 1 кроватью, кондиционером, мини-баром и кабельным телевидением.","hasRoomInventory":true,"highlights":[{"__typename":"RTRoomPrivacyHighlight","privacyLevel":"PRIVACY_LEVEL_1"},{"__typename":"RTRoomSizeHighlight","areaValue":30},{"__ref":"RTRoomFacilityHighlight:121"},{"__ref":"RTRoomFacilityHighlight:11"},{"__ref":"RTRoomFacilityHighlight:38"},{"__ref":"RTRoomFacilityHighlight:75"},{"__ref":"RTRoomFacilityHighlight:79"},{"__ref":"RTRoomFacilityHighlight:3"},{"__ref":"RTHotelFacilityHighlight:107"}],"categorizedFacilities":[{"__typename":"RTFacilitiesWithCategory","category":"VIEW","facilities":[121]},{"__typename":"RTFacilitiesWithCategory","category":"BATHROOM_PRIVATE","facilities":[27,100,31,69,43,12,141]},{"__typename":"RTFacilitiesWithCategory","category":"OTHER","facilities":[74,23,6,82,132,75,39,83,215,13,77,84,124,134,137,26,184,139,91,8,22,125,3,70,18,76,86,9,41,68,95,116,79,44,11,85,138]}],"facilities":[27,6,100,31,77,69,82,124,125,184,116,23,26,18,76,8,43,22,9,44,12,39,41,91,13,70,86,68,83,84,74,95,85,132,137,138,139,141,134,215],"occupancy":{"__typename":"RTOccupancy","maxPersons":2,"maxChildren":1,"maxGuests":2},"hasSubUnits":false,"hasRoomPage":true,"bedConfigurations":[{"__typename":"RTBedConfiguration","configurationId":1,"beds":[{"__typename":"RTBedType","count":1,"bedTypeId":3}]}],"apartmentRooms":[],"bathroomCount":1,"photos":[{"__ref":"RTRoomPhoto:48446605"},{"__ref":"RTRoomPhoto:77788506"},{"__ref":"RTRoomPhoto:77788348"},{"__ref":"RTRoomPhoto:78417468"},{"__ref":"RTRoomPhoto:36063679"}],"isSmoking":false,"parkingInfo":{"__typename":"RTParkingInfo","hasParking":false},"nrStaysWithCheapestPriceForRoomLevelInventory":null,"onlyXLeftMessageDetails":null,"roomAvBlocks":[]},"RTRoomPhoto:77862891":{"id":77862891,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/77862891.jpg?k=12b37e98c6088d9de3e4ebf5b1f1ce99186ab85950335299f92d702ef472c9b5\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/77862891.jpg?k=12b37e98c6088d9de3e4ebf5b1f1ce99186ab85950335299f92d702ef472c9b5\u0026o=","ranking":9},"RTRoomPhoto:77862878":{"id":77862878,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/77862878.jpg?k=6ad89b8e12c2fd666b42c14cfccc2c840b01b090734015d10c8e3a4097e4e14c\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/77862878.jpg?k=6ad89b8e12c2fd666b42c14cfccc2c840b01b090734015d10c8e3a4097e4e14c\u0026o=","ranking":14},"RTRoomPhoto:382987736":{"id":382987736,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/382987736.jpg?k=c8d9417bc14032c9078602084564faaf3aba14852f2a208bffcb38b164687735\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/382987736.jpg?k=c8d9417bc14032c9078602084564faaf3aba14852f2a208bffcb38b164687735\u0026o=","ranking":26},"RTRoomCard:{\"roomId\":111370310}":{"roomId":111370310,"__typename":"RTRoomCard","roomIndex":2,"roomTypeId":9,"name":"Номер Делюкс \"Сеньор\"","description":"This double room features a sofa, air conditioning and minibar.","hasRoomInventory":true,"highlights":[{"__typename":"RTRoomPrivacyHighlight","privacyLevel":"PRIVACY_LEVEL_1"},{"__typename":"RTRoomSizeHighlight","areaValue":57},{"__ref":"RTRoomFacilityHighlight:110"},{"__ref":"RTRoomFacilityHighlight:121"},{"__ref":"RTRoomFacilityHighlight:11"},{"__ref":"RTRoomFacilityHighlight:38"},{"__ref":"RTRoomFacilityHighlight:75"},{"__ref":"RTRoomFacilityHighlight:79"},{"__ref":"RTRoomFacilityHighlight:3"},{"__ref":"RTHotelFacilityHighlight:107"}],"categorizedFacilities":[{"__typename":"RTFacilitiesWithCategory","category":"VIEW","facilities":[110,121]},{"__typename":"RTFacilitiesWithCategory","category":"BATHROOM_PRIVATE","facilities":[27,100,31,69,43,12,141]},{"__typename":"RTFacilitiesWithCategory","category":"OTHER","facilities":[74,23,6,82,126,132,75,83,215,13,77,84,124,134,137,26,184,139,91,8,22,125,3,70,18,76,86,9,41,68,95,116,79,44,11,85,138]}],"facilities":[27,6,100,31,77,69,82,124,125,184,116,23,26,18,76,8,43,22,9,44,12,41,91,13,70,86,68,83,84,74,95,85,126,132,137,138,139,141,134,215],"occupancy":{"__typename":"RTOccupancy","maxPersons":2,"maxChildren":1,"maxGuests":2},"hasSubUnits":false,"hasRoomPage":true,"bedConfigurations":[{"__typename":"RTBedConfiguration","configurationId":1,"beds":[{"__typename":"RTBedType","count":1,"bedTypeId":6}]}],"apartmentRooms":[],"bathroomCount":1,"photos":[{"__ref":"RTRoomPhoto:383202859"},{"__ref":"RTRoomPhoto:383202327"},{"__ref":"RTRoomPhoto:77862891"},{"__ref":"RTRoomPhoto:77862878"},{"__ref":"RTRoomPhoto:382987736"},{"__ref":"RTRoomPhoto:116076121"}],"isSmoking":false,"parkingInfo":{"__typename":"RTParkingInfo","hasParking":false},"nrStaysWithCheapestPriceForRoomLevelInventory":null,"onlyXLeftMessageDetails":null,"roomAvBlocks":[]},"RTRoomPhoto:78414596":{"id":78414596,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/78414596.jpg?k=34d8ff3833019a76ff12360c94cb53855947d3c0ce2c0b6b37688cc854299036\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/78414596.jpg?k=34d8ff3833019a76ff12360c94cb53855947d3c0ce2c0b6b37688cc854299036\u0026o=","ranking":8},"RTRoomPhoto:88981496":{"id":88981496,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/88981496.jpg?k=90a99a1b15fe1958c87d977afd604e0c0d0ad7ebeef6974408754913cc722c99\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/88981496.jpg?k=90a99a1b15fe1958c87d977afd604e0c0d0ad7ebeef6974408754913cc722c99\u0026o=","ranking":21},"RTRoomPhoto:166515193":{"id":166515193,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/166515193.jpg?k=b56e75fe4dcfa4b62db4c25a61388271595ae294ce6c5b65c2d3ac0cef49ec7a\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/166515193.jpg?k=b56e75fe4dcfa4b62db4c25a61388271595ae294ce6c5b65c2d3ac0cef49ec7a\u0026o=","ranking":11},"RTRoomPhoto:48446862":{"id":48446862,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/48446862.jpg?k=57206aff9973cf0657a8cd0e003b6c115c099d59ef71d0387f360b11138bcd08\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/48446862.jpg?k=57206aff9973cf0657a8cd0e003b6c115c099d59ef71d0387f360b11138bcd08\u0026o=","ranking":7},"RTRoomPhoto:48446634":{"id":48446634,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/48446634.jpg?k=5242144da460e4ba34091f5ab0806f17070be6bd2544fce71f5dd1abd6969d76\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/48446634.jpg?k=5242144da460e4ba34091f5ab0806f17070be6bd2544fce71f5dd1abd6969d76\u0026o=","ranking":12},"RTRoomPhoto:78415078":{"id":78415078,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/78415078.jpg?k=d37270b63d8eadd6c6e063861a9b5621f6594d124377e256559bff5b79a0ead1\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/78415078.jpg?k=d37270b63d8eadd6c6e063861a9b5621f6594d124377e256559bff5b79a0ead1\u0026o=","ranking":19},"RTRoomPhoto:383204636":{"id":383204636,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/383204636.jpg?k=ed3e42ffd413a7baace6d8fe80b854b8b2fbae90eee3384ca62d863cc75b8b34\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/383204636.jpg?k=ed3e42ffd413a7baace6d8fe80b854b8b2fbae90eee3384ca62d863cc75b8b34\u0026o=","ranking":31},"RTRoomPhoto:383206421":{"id":383206421,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/383206421.jpg?k=5576c8803ade8bc82326228110b434015a351f2b2c1d75faac08cf5b7a04c6eb\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/383206421.jpg?k=5576c8803ade8bc82326228110b434015a351f2b2c1d75faac08cf5b7a04c6eb\u0026o=","ranking":35},"RTRoomPhoto:383206420":{"id":383206420,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/383206420.jpg?k=effa33e7d75fa2d161ca27a3e4c3ee4073d978ea5498352279b692c520a6f2cf\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/383206420.jpg?k=effa33e7d75fa2d161ca27a3e4c3ee4073d978ea5498352279b692c520a6f2cf\u0026o=","ranking":34},"RTRoomCard:{\"roomId\":111370313}":{"roomId":111370313,"__typename":"RTRoomCard","roomIndex":3,"roomTypeId":1,"name":"Роскошные апартаменты","description":"Звукоизолированные апартаменты с мини-баром и кондиционером.","hasRoomInventory":true,"highlights":[{"__typename":"RTRoomPrivacyHighlight","privacyLevel":"PRIVACY_LEVEL_2"},{"__typename":"RTRoomSizeHighlight","areaValue":66},{"__ref":"RTRoomFacilityHighlight:110"},{"__ref":"RTRoomFacilityHighlight:121"},{"__ref":"RTRoomFacilityHighlight:11"},{"__ref":"RTRoomFacilityHighlight:38"},{"__ref":"RTRoomFacilityHighlight:75"},{"__ref":"RTRoomFacilityHighlight:79"},{"__ref":"RTRoomFacilityHighlight:3"},{"__ref":"RTHotelFacilityHighlight:107"}],"categorizedFacilities":[{"__typename":"RTFacilitiesWithCategory","category":"VIEW","facilities":[110,121]},{"__typename":"RTFacilitiesWithCategory","category":"BATHROOM_PRIVATE","facilities":[27,100,31,69,43,12,141]},{"__typename":"RTFacilitiesWithCategory","category":"OTHER","facilities":[74,23,6,82,126,132,75,39,83,215,13,77,84,124,134,137,26,184,139,91,8,22,125,3,70,18,76,86,9,41,68,95,116,79,44,11,85,138]}],"facilities":[27,6,100,31,77,69,82,124,125,184,116,23,26,18,76,8,43,22,9,44,12,39,41,91,13,70,86,68,83,84,74,95,85,126,132,137,138,139,141,134,215],"occupancy":{"__typename":"RTOccupancy","maxPersons":2,"maxChildren":1,"maxGuests":2},"hasSubUnits":true,"hasRoomPage":true,"bedConfigurations":[],"apartmentRooms":[{"__typename":"RTApartmentRoom","apartmentRoomId":65232390,"name":"Спальня ","beds":[{"__typename":"RTBedType","count":1,"bedTypeId":3}]}],"bathroomCount":1,"photos":[{"__ref":"RTRoomPhoto:78414596"},{"__ref":"RTRoomPhoto:88981496"},{"__ref":"RTRoomPhoto:166515193"},{"__ref":"RTRoomPhoto:48446862"},{"__ref":"RTRoomPhoto:48446634"},{"__ref":"RTRoomPhoto:78415078"},{"__ref":"RTRoomPhoto:383204636"},{"__ref":"RTRoomPhoto:383206421"},{"__ref":"RTRoomPhoto:383206420"}],"isSmoking":false,"parkingInfo":{"__typename":"RTParkingInfo","hasParking":false},"nrStaysWithCheapestPriceForRoomLevelInventory":null,"onlyXLeftMessageDetails":null,"roomAvBlocks":[]},"RTRoomPhoto:78413682":{"id":78413682,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/78413682.jpg?k=aabe2607bc8ac11fe84f7afc4c055f1ea53db4470fd74f2afe7ca9ff770229dc\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/78413682.jpg?k=aabe2607bc8ac11fe84f7afc4c055f1ea53db4470fd74f2afe7ca9ff770229dc\u0026o=","ranking":18},"RTRoomPhoto:383203312":{"id":383203312,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/383203312.jpg?k=b1efceb0c70c8f36f6deccec9dbc0624f2bee39624455b3b4b4d8981e0261063\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/383203312.jpg?k=b1efceb0c70c8f36f6deccec9dbc0624f2bee39624455b3b4b4d8981e0261063\u0026o=","ranking":29},"RTRoomPhoto:383204418":{"id":383204418,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/383204418.jpg?k=cdd6613bb81fa67ff1cbba6af2663d1f97bab692e26265381664bb61f404ec86\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/383204418.jpg?k=cdd6613bb81fa67ff1cbba6af2663d1f97bab692e26265381664bb61f404ec86\u0026o=","ranking":30},"RTRoomPhoto:123585100":{"id":123585100,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/123585100.jpg?k=90bc536d206e8c261d172b0861a2923fbf02c12fed9a0f1e95751227c242439d\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/123585100.jpg?k=90bc536d206e8c261d172b0861a2923fbf02c12fed9a0f1e95751227c242439d\u0026o=","ranking":25},"RTRoomPhoto:383208835":{"id":383208835,"__typename":"RTRoomPhoto","photoUri":"/xdata/images/hotel/max1024x768/383208835.jpg?k=d3f207e7b8b02fdae72b2fdd957186091c17f331f5e6f241964b19a7a1a56df1\u0026o=","thumbnailUri":"/xdata/images/hotel/square60/383208835.jpg?k=d3f207e7b8b02fdae72b2fdd957186091c17f331f5e6f241964b19a7a1a56df1\u0026o=","ranking":36},"RTRoomCard:{\"roomId\":111370329}":{"roomId":111370329,"__typename":"RTRoomCard","roomIndex":4,"roomTypeId":9,"name":"Номер Делюкс «Премиум»","description":"This double room has a soundproofing, garden view and private entrance.","hasRoomInventory":true,"highlights":[{"__typename":"RTRoomPrivacyHighlight","privacyLevel":"PRIVACY_LEVEL_1"},{"__typename":"RTRoomSizeHighlight","areaValue":45},{"__ref":"RTRoomFacilityHighlight:110"},{"__ref":"RTRoomFacilityHighlight:121"},{"__ref":"RTRoomFacilityHighlight:11"},{"__ref":"RTRoomFacilityHighlight:38"},{"__ref":"RTRoomFacilityHighlight:75"},{"__ref":"RTRoomFacilityHighlight:79"},{"__ref":"RTRoomFacilityHighlight:3"},{"__ref":"RTHotelFacilityHighlight:107"}],"categorizedFacilities":[{"__typename":"RTFacilitiesWithCategory","category":"VIEW","facilities":[110,121]},{"__typename":"RTFacilitiesWithCategory","category":"BATHROOM_PRIVATE","facilities":[27,100,31,69,43,12,141]},{"__typename":"RTFacilitiesWithCategory","category":"OTHER","facilities":[74,23,6,82,126,132,75,83,215,13,77,84,124,134,137,26,184,139,91,8,22,125,3,70,18,76,86,9,41,68,95,116,79,44,11,85,138]}],"facilities":[27,6,100,31,77,69,82,124,125,184,116,23,26,18,76,8,43,22,9,44,12,41,91,13,70,86,68,83,84,74,95,85,126,132,137,138,139,141,134,215],"occupancy":{"__typename":"RTOccupancy","maxPersons":2,"maxChildren":1,"maxGuests":2},"hasSubUnits":false,"hasRoomPage":true,"bedConfigurations":[{"__typename":"RTBedConfiguration","configurationId":1,"beds":[{"__typename":"RTBedType","count":1,"bedTypeId":6}]}],"apartmentRooms":[],"bathroomCount":1,"photos":[{"__ref":"RTRoomPhoto:78413682"},{"__ref":"RTRoomPhoto:383203312"},{"__ref":"RTRoomPhoto:383204418"},{"__ref":"RTRoomPhoto:123585100"},{"__ref":"RTRoomPhoto:383208835"}],"isSmoking":false,"parkingInfo":{"__typename":"RTParkingInfo","hasParking":false},"nrStaysWithCheapestPriceForRoomLevelInventory":null,"onlyXLeftMessageDetails":null,"roomAvBlocks":[]},"RoomTableQueryResult:
