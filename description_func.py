# import main 
from bs4 import BeautifulSoup
import re


def page_scraper_description(data_upz_hotels, resHtml):
    print('hello description!')
    result_description_upz = []
    try:
       hotelid = data_upz_hotels["hotel_id"] 
    except:
        pass
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")
    except Exception as ex:
        print(f"str226___{ex}") 
    try:
        description_block = soup1.find("div", attrs={"class": "hp_desc_main_content"})
        description = description_block.get_text(strip=True, separator="\n")

        result_description_upz.append({
            "id": "",
            "hotelid": hotelid,
            "enusname": description,
        })

    except Exception as ex:
        print(f"str119___{ex}") 
        # return None 

    try:
        return result_description_upz[0] 
    except:
        return None
