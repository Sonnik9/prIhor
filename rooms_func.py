# import main
from bs4 import BeautifulSoup
import re
import facilities_data

def page_scraper_room(resHtml, hotelid):
    result_room_upz = []
    result_room_upz_list = []  

    try:
        soup1 = BeautifulSoup(resHtml, "lxml")       
    except Exception as ex:
        # print(f"str102___{ex}") 
        # pass
        return None 

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
            room_id = 'not found'
            name_room = 'not found'
            endescription = 'not found'
            allow_children = 'not found'
            private_bathroom_highlight = 'not found'
            bed_config = 'not found'
            bed_index = []
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
                            allow_children = 'not found'
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
                            # print(f"202____{ex}") 
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
                            # print(f"215____{ex}") 
            except Exception as ex:
                # print(f"140____{ex}")  
                pass
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
                # print(f"150____{ex}") 
                # pass
                return None 

    except Exception as ex:
        # print(f"154____{ex}")
        # pass
        return None 

    try:
        result_room_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_room_upz_list": result_room_upz_list,            
        })
    except Exception as ex:
        # print(f"str163___{ex}") 
        # pass
        return None 
    # print(ok)
    try:
        # try:
        #     with open(f'room_upz_Test_16.json', "w", encoding="utf-8") as file: 
        #         json.dump(result_room_upz, file, indent=4, ensure_ascii=False)
        # except Exception as ex:
        #     print(f"str210__{ex}")
        # return
        return result_room_upz[0]
    except:
        return None
