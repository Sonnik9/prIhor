# import main
from bs4 import BeautifulSoup
import re


def page_scraper_photos(resHtml, hotelid):
    result_photos_upz = []
    # print('hello photos!')

    try:
        soup1 = BeautifulSoup(resHtml, "lxml")       
    except Exception as ex:
        # print(f"str102___{ex}") 
        # pass
        return None 

    try:
        preview_list_photo = []
        imgBlock1 = soup1.find_all('a', attrs={'class': 'bh-photo-grid-item', 'class': 'bh-photo-grid-side-photo', 'class': 'active-image' }) 
        imgBlock2 = soup1.find('div', attrs={'id': 'hotel_main_content'}).find_all('div', class_='bh-photo-grid-thumb-cell')
        # print(f"str 122________ {len(imgBlock2) + len(imgBlock1)}") 
        try:
            photo_item_large = ''
            photo_item_large =  imgBlock1[0].find('img').get('src')
            # print(photo_item_large)
        except Exception as ex:
            # print(f"str45__{ex}") 
            pass
        try:
            url_square60 = ''
            url_square60 = imgBlock2[0].find('a').find('img').get('src')
            # print(photo_item_large)

        except Exception as ex:
            # print(f"str52__{ex}")
            pass

        try:
            for src in imgBlock1:
                try:
                    photo_item_src = src.find('img').get('src')
                    # print(photo_item_src)
                except:
                    pass 

                try:
                    photo_item_id = src.get('data-id')
                except:
                    pass 

                try:
                    photo_item_title = src.find('img').get('alt')
                    # print(photo_item)
                    # photo_list_src.append(photo_item_title) 
                except:
                    pass 
                preview_list_photo.append({
                    'photo_item_src': photo_item_src,
                    'photo_item_id': photo_item_id,
                    'photo_item_title': photo_item_title,
                }) 
        except Exception as ex:
            print(f"str65__{ex}") 

        try:
            for src in imgBlock2:
                if src.find('a').find('img').get('src') != None:
                    try:
                        photo_item_src = src.find('a').find('img').get('src')
                        # print(photo_item)
                        # photo_list_src.append(photo_item_src) 
                    except:
                        pass 

                    try:
                        photo_item_id = src.find('a').get('data-id')
                    except:
                        pass 

                    try:
                        photo_item_title = src.find('a').find('img').get('alt')
                    except:
                        pass

                    preview_list_photo.append({
                        'photo_item_src': photo_item_src,
                        'photo_item_id': photo_item_id,
                        'photo_item_title': photo_item_title,
                    }) 
        except Exception as ex:
            # print(f"str94__{ex}")
            pass

        try:
            clean_links_set_max1280x900 = set()
            clean_links_list_max1280x900 = []
            result_photo = [] 

            words = resHtml.split()
            links = set()
            for word in words:
                if re.search(r"https://cf\.bstatic\.com/xdata/images/hotel.*", word):
                    links.add(word)
            dirty_links = list(links)
            for link in dirty_links:
                match = re.search(r"https://cf\.bstatic\.com/xdata/images/hotel/max1280x900.*?&hp=1", link)
                if match:
                    clean_links_set_max1280x900.add(match.group(0))
            clean_links_list_max1280x900 = list(clean_links_set_max1280x900)
            for link in clean_links_list_max1280x900:
                try:
                    id_photo = link.split('/')[-1].split('.')[0].strip()
                except:
                    match = re.search(r"/(\d{9})\.", link)
                    if match:
                        id_photo = match.group(1)
                        # print(id_photo)
                photo_max1024x768 = re.sub(r'max1280x900', 'max1024x768', link)
                photo_max200 = re.sub(r'max1280x900', 'max200', link)
                result_photo.append({
                    'id_photo': id_photo,
                    'photo_max1280x900': link,
                    'photo_max1024x768': photo_max1024x768,
                    'photo_max200': photo_max200,
                })

        except Exception as ex:
            # print(f"str115{ex}")
            pass
        try:
            result_photos_upz.append({
                "id": "",
                "hotelid": str(hotelid),
                "url_max": str(photo_item_large),
                "url_square60": str(url_square60),
                "list_photo_1-7,10": preview_list_photo,
                "all_photos": result_photo

            })
        except:
            # pass
            return None 
        # print(result_photos_upz)      
        
    except Exception as ex:
        # print(f"str105__{ex}") 
        # pass
        return None 
    # return None 
    try:
        return result_photos_upz[0]   
    except:
        return None
    
