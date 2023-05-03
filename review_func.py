import requests
# import main
from bs4 import BeautifulSoup
# import re
import random
import smart_headers
import time


# data_upz_hotels["url"] = 'https://www.booking.com/reviewlist.ru.html?cc1=uz&pagename=hilton-tashkent-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&rows=100&offset=0'



def req_generatorReview(link):
    r = ''
    for sesCountt in range(3):
        r = ''
        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)  
        try:  
            # print('hello req')                    
            r = requests.get(link, headers=smart_headers.random_headers(), timeout=(3.15, 21.15))
            r.raise_for_status()
            print(r.status_code)
            if r.status_code == 404: 
                return None
            if r.status_code == 200:
                return r.text 
            else:
                continue

        except Exception as ex:
            print(f"str214___{ex} \n status_code: {r.status_code}") 
            if sesCountt == 2:
                return None 
            else:
                continue 
    try:
        return r.text 
    except:
        return None


def page_scraper_otziv(fixed_url, hotelid):
    result_review_upz = []
    result_review_upz_list = []

    try:       
        # print(fixed_url)
        reworked_title = fixed_url.split('/')[-1].split('.')[0].strip()         
        reworked_link  = f'https://www.booking.com/reviewlist.ru.html?cc1=vn&pagename={reworked_title}&r_lang=&review_topic_category_id=&type=total&score=&sort=&time_of_year=&dist=1&offset=0&rows=100&rurl=&text=&'

    except Exception as ex:
        # print(f"str199___{ex}")
        return None


    try:
        for _ in range(3):
            resHtml2 = req_generatorReview(reworked_link)  
            if resHtml2 is not None:
                break 
            else:
                continue      
    except Exception as ex:
        # print(f"249____{ex}")
        return None

    try:
        for _ in range(2):
            soup1 = BeautifulSoup(resHtml2, "lxml")  
            if soup1 is not None:
                break  
            else:
                continue 
        
    except Exception as ex:
        # print(f"str102___{ex}") 
        pass

    try:
        # print('hello finder')
        try:
           review_block = soup1.find('ul', attrs={}).find_all('li', class_='review_list_new_item_block')
        except:
            return None
        # print(len(review_block))
        for item in review_block:
            try:
                title = item.find('h3', attrs={'class': 'c-review-block__title', 'class': 'c-review__title--ltr'}).get_text().strip()
                # print(title)               
            except Exception as ex:
                title = 'not found'
                # print(f"str129___{ex}")
            try:
                pros = item.find('p').find('span', class_='c-review__body').get_text().strip()
                # print(pros)              
            except Exception as ex:
                pros = 'not found' 
                # print(f"str129___{ex}")
            try:
                cons = item.find_all('p')[1].find('span', class_='c-review__body').get_text().strip()
                # print(cons)
            except Exception as ex:
                cons = 'not found' 
                # print(f"str129___{ex}") 
            try:
                dt1 = item.find_all('span', class_='c-review-block__date')[1].get_text().split(':')[1].strip()
                # print(dt1)
            #    break
            except Exception as ex:
                dt1 = 'not found'
                # print(f"str129___{ex}") 
            try:
                average_score = item.find('div', class_='bui-review-score__badge').get_text().strip()
                # print(average_score)
            #    break
            except Exception as ex:
                average_score = 'not found'
                # print(f"str129___{ex}") 
            try:
                author_name = item.find('span', class_='bui-avatar-block__title').get_text().strip()
                # print(author_name)
            #    break
            except Exception as ex:
                author_name = 'not found'
                # print(f"str129___{ex}") 
            try:
                room_id = item.find('div', class_='bui-list__body').get_text().strip()
                # print(room_id)
            #    break
            except Exception as ex:
                room_id = 'not found'
                # print(f"str129___{ex}") 
            try:
                checkinBlock = item.find_all('div', class_='bui-list__body')[1]
                #    print(checkinBlock)
                checkin = checkinBlock.get_text(strip=True, separator="\n")
                # print(checkin)
                #    break
            except Exception as ex:
                checkin = 'not found'
                # print(f"str129___{ex}") 
            try:
                checkout = checkin 
            except Exception as ex:
                checkout = 'not found'
                # print(f"str129___{ex}") 
            try:                
                languagecode = '?'
            except Exception as ex:
                # print(f"str129___{ex}") 
                pass

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
        print(f"str162___{ex}") 
        pass
    try:
        result_review_upz.append({
            "id":"",
            "hotelid": hotelid,
            "result_review_upz_list": result_review_upz_list,            
        })
    except Exception as ex:
        # print(f"str226___{ex}") 
        pass
    try:
        return result_review_upz[0]
    except:
        return None