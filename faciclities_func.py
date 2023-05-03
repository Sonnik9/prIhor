# import main
from bs4 import BeautifulSoup
import re


def page_scraper_facilities(resHtml, hotelid):
    result_facilities_upz = []
    result_facilities_upz_list = []
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")     
    except Exception as ex:
        # print(f"str102___{ex}") 
        # pass 
        return None

    try:
        # print('hello finder')        
        span_tag = soup1.find('span', attrs={'data-testid': 'facility-group-icon'})
        parent_div = span_tag.find_parent('div')
        parent_class = parent_div['class'][0]
        # print(parent_class)
        # facilities_block_pre = soup1.find_all('div', class_= parent_div)
        parent_div_main = parent_div.find_parent('div').find_parent('div').find_parent('div').get('class')[0]
        facilities_list = soup1.find_all('div', class_=parent_div_main)
        # print(len(facilities_list))
        
        # return len(facilities_list)
        for item in facilities_list:
            try:
                facilitytype_id = parent_class 
                # ????????
                # print(title)               
            except Exception as ex:
                facilitytype_id = 'not found'
                # print(f"str129___{ex}")
                pass
            try:
                name = item.find('div', class_= parent_class).get_text().strip()
                # print(name) 
                # return name             
            except Exception as ex:
                name = 'not found' 
                # print(f"str129___{ex}")
            try:
                facilitytype_name_list = []
                facilitytype_name =''
                hotelfacilitytype_id = '?'
                facilitytype_name_block = item.find_all('li')
                for li in facilitytype_name_block:
                    facilitytype_name = li.get_text(strip=True, separator="\n")
                    facilitytype_name_list.append({
                        'facilitytype_name': facilitytype_name,
                        'hotelfacilitytype_id': hotelfacilitytype_id,
                    })
                # print(cons)
            except Exception as ex:
                facilitytype_name = 'not found' 
                # print(f"str129___{ex}") 
            try:
                uniq = '?'
                # print(average_score)
            #    break
            except Exception as ex:
                uniq = 'not found'
                # print(f"str129___{ex}") 

            result_facilities_upz_list.append({
                "facilitytype_id": facilitytype_id, 
                "name": name, 
                'facilitytype_name_list': facilitytype_name_list,              
                "uniq": uniq, 
               
            })
            # print(len(result_review_upz_list))
    except Exception as ex:
        # print(f"str226___{ex}") 
        return None
        # pass
    try:
        result_facilities_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_review_upz_list": result_facilities_upz_list,            
        })
    except Exception as ex:
        # print(f"str226___{ex}") 
        return None
        # pass
    try:
        return result_facilities_upz[0]
    except:
        return None


