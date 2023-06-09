import requests
# import main
from bs4 import BeautifulSoup
# import re
import random
import smart_headers
import time


# data_upz_hotels["url"] = 'https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&rows=100&offset=0'



def req_generatorReview(link):

    for sesCountt in range(3):
        r = ''
        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)  
        try:  
            print('hello req')                    
            r = requests.get(link, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
            r.raise_for_status()
            print(r.status_code) 
            if r.status_code == 200:
            #    with open('review_test_doubleReq_2.html', 'w', encoding='utf-8') as f:
            #         f.write(r.text)                    
                return r.text
        except Exception as ex:
            print(f"str214___{ex}") 
            if sesCountt == 2:
                return None 
            else:
                continue 



def page_scraper_otziv(data_upz_hotels_item, link):
    result_review_upz = []
    result_review_upz_list = []
   
    try:
        data_upz_hotels_item_dict = eval(data_upz_hotels_item)
    except:
        data_upz_hotels_item_dict = data_upz_hotels_item

    try:       
        # print(fixed_url)
        reworked_title = link.split('/')[-1].split('.')[0].strip()         
        reworked_link  = f'https://www.booking.com/reviewlist.ru.html?cc1=vn&pagename={reworked_title}&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&offset=0&rows=100&rurl=&text=&'

    except Exception as ex:
        print(f"str199___{ex}")
        return None
    try:
       hotelid = data_upz_hotels_item["hotel_id"] 
    except:
        hotelid = 'not found'

    try:
        resHtml = req_generatorReview(reworked_link)
    except:
        return None
    try:
        soup1 = BeautifulSoup(resHtml, "lxml")
    except Exception as ex:
        print(f"str226___{ex}") 

    try:
        # print('hello finder')
        review_block = soup1.find('ul', attrs={}).find_all('li', class_='review_list_new_item_block')
        print(len(review_block))
        for item in review_block:
            try:
                title = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get_text().strip()
                # print(title)               
            except Exception as ex:
                title = 'not found'
                print(f"str129___{ex}")
            try:
                pros = item.find('p').find('span', class_='c-review__body').get_text().strip()
                # print(pros)              
            except Exception as ex:
                pros = 'not found' 
                print(f"str129___{ex}")
            try:
                cons = item.find_all('p')[1].find('span', class_='c-review__body').get_text().strip()
                # print(cons)
            except Exception as ex:
                cons = 'not found' 
                print(f"str129___{ex}") 
            try:
                dt1 = item.find_all('span', class_='c-review-block__date')[1].get_text().split(':')[1].strip()
                # print(dt1)
            #    break
            except Exception as ex:
                dt1 = 'not found'
                print(f"str129___{ex}") 
            try:
                average_score = item.find('div', class_='bui-review-score__badge').get_text().strip()
                # print(average_score)
            #    break
            except Exception as ex:
                average_score = 'not found'
                print(f"str129___{ex}") 
            try:
                author_name = item.find('span', class_='bui-avatar-block__title').get_text().strip()
                # print(author_name)
            #    break
            except Exception as ex:
                author_name = 'not found'
                print(f"str129___{ex}") 
            try:
                room_id = item.find('div', class_='bui-list__body').get_text().strip()
                # print(room_id)
            #    break
            except Exception as ex:
                room_id = 'not found'
                print(f"str129___{ex}") 
            try:
                checkinBlock = item.find_all('div', class_='bui-list__body')[1]
                #    print(checkinBlock)
                checkin = checkinBlock.get_text(strip=True, separator="\n")
                # print(checkin)
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
            # print(len(result_review_upz_list))
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
        return result_review_upz[0]
    except:
        return None