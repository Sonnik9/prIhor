
# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import smart_headers

# url = "https://www.booking.com/hotel/zm/le-elementos-by-mantis.ru.html?label=gen173nr-1BCAso_AFCFmxlLWVsZW1lbnRvcy1ieS1tYW50aXNIM1gEaOkBiAEBmAEhuAEZyAEM2AEB6AEBiAIBqAIDuAKGyJCiBsACAdICJGE5M2JlYWQ4LThiNzctNDBkOS05ZTA0LTJkOTZiMzI0NDcyNNgCBeACAQ&sid=52c12d695260d02d8a98fb123e5b9e1e&dist=0&keep_landing=1&sb_price_type=total&type=total&"

# # загружаем страницу и создаем объект soup
# r = requests.get(url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
# # r.raise_for_status()
# print(r.status_code) 
# soup = BeautifulSoup(r.content, "lxml")

# # находим все теги img
# img_tags = soup.find_all("img")
# a_tags = soup.find_all("a")
# print(len(img_tags))
# print(len(a_tags))

# https://cf.bstatic.com/xdata/images/hotel




# создаем регулярное выражение для извлечения ссылок на изображения
# pattern = re.compile(r"(http(s?):)([/|.|\w|\s|-])*\.(?:jpg|jpeg)")

# # создаем список ссылок на изображения
# img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

# # добавляем ссылки на изображения из стилей CSS
# style_tags = soup.find_all('style')
# for tag in style_tags:
#     css = tag.get_text()
#     img_urls += pattern.findall(css) 

# print(len(img_urls))

# try:
#     with open(f'result_photos_Test_1.json', "w", encoding="utf-8") as file: 
#         json.dump(str(img_tags), file, indent=4, ensure_ascii=False)
# except Exception as ex:
#     print(f"str210__{ex}")

# загружаем изображения по ссылкам
# for url in img_urls:
#     response = requests.get(url)
#     # сохраняем изображение в файл
#     with open("image.jpg", "wb") as f:
#         f.write(response.content) 



# https://cf.bstatic.com/xdata/images/hotel/max1024x768/218942678.jpg?k=5b1b92c4d716debd9217097925b37ecba30df99689c2b93147188ae82e463ab1&o=&hp=1



# import requests
# from bs4 import BeautifulSoup
# import json
# import re
# import smart_headers

# url = "https://www.booking.com/hotel/zm/le-elementos-by-mantis.ru.html?label=gen173nr-1BCAso_AFCFmxlLWVsZW1lbnRvcy1ieS1tYW50aXNIM1gEaOkBiAEBmAEhuAEZyAEM2AEB6AEBiAIBqAIDuAKGyJCiBsACAdICJGE5M2JlYWQ4LThiNzctNDBkOS05ZTA0LTJkOTZiMzI0NDcyNNgCBeACAQ&sid=52c12d695260d02d8a98fb123e5b9e1e&dist=0&keep_landing=1&sb_price_type=total&type=total&"

# # загружаем страницу и создаем объект soup
# r = requests.get(url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
# print(r.status_code)
# soup = BeautifulSoup(r.content, "lxml")

# # находим все теги img и a
# img_tags = soup.find_all("img")
# a_tags = soup.find_all("a")

# # создаем множество для хранения найденных ссылок
# links = set()

# # проходим по всем тегам img и a и ищем ссылки
# for tag in img_tags + a_tags:
#     for attr in tag.attrs.values():
#         if isinstance(attr, str) and "https://cf.bstatic.com/xdata/images/hotel" in attr:
#             links.add(attr)

# # сохраняем результаты в JSON файл
# with open("links.json", "w") as f:
#     json.dump(list(links), f) 


# <a href="https://cf.bstatic.com/xdata/images/hotel/max1024x768/218925858.jpg?k=3c701ab5d0d9da69a1c054114206fa09daefbbfeae5f86982cdce50b656e7835&amp;o=&amp;hp=1" target="_blank" area-label="Галерея фотографий этого варианта размещения" data-id="218925858" class="bh-photo-modal-grid-item-wrapper" data-et-click=" customGoal:aXBNTfZHQSVTMIcOcfPUMVBFUWe:1"><img class="bh-photo-modal-grid-image" data-id="218925858" alt="Галерея фотографий этого варианта размещения" height="6.8980496453900715px" src="https://cf.bstatic.com/xdata/images/hotel/max1024x768/218925858.jpg?k=3c701ab5d0d9da69a1c054114206fa09daefbbfeae5f86982cdce50b656e7835&amp;o=&amp;hp=1"></a>




# import requests
# from bs4 import BeautifulSoup
# import re
# import smart_headers
# import json

# url = "https://www.booking.com/hotel/zm/le-elementos-by-mantis.ru.html?label=gen173nr-1BCAso_AFCFmxlLWVsZW1lbnRvcy1ieS1tYW50aXNIM1gEaOkBiAEBmAEhuAEZyAEM2AEB6AEBiAIBqAIDuAKGyJCiBsACAdICJGE5M2JlYWQ4LThiNzctNDBkOS05ZTA0LTJkOTZiMzI0NDcyNNgCBeACAQ&sid=52c12d695260d02d8a98fb123e5b9e1e&dist=0&keep_landing=1&sb_price_type=total&type=total&"

# r = requests.get(url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
# soup = BeautifulSoup(r.content, "html.parser")

# links = set()
# linksArr = []
# for tag in soup.find_all(['a', 'img']):
#     if 'src' in tag.attrs and re.search('https://cf.bstatic.com/xdata/images/hotel', tag['src']):
#         links.add(tag['src'])
#     elif 'href' in tag.attrs and re.search('https://cf.bstatic.com/xdata/images/hotel', tag['href']):
#         links.add(tag['href']) 

# linksArr = list(links)
# print(len(linksArr))

# with open("links.json", "w") as f:
#     json.dump(linksArr, f)   





# Please, one more. We have the next data: 
data1 = [{'links_list_max1280x900': ['https://cf.bstatic.com/xdata/images/hotel/max1280x900/199518553.jpg?k=fd87a93dcc2ff2829265c6adee5015928623eba53fc8f47570265cdaf4c9389b&o=&hp=1', 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/218923865.jpg?k=13e34c87885fcd7bc265887daaad3f79c1964abf36b8e094035fa8668ff2e205&o=&hp=1'], 'links_list_max1024x768': ['https://cf.bstatic.com/xdata/images/hotel/max1024x768/219198926.jpg?k=bac14a9cdc69741843d16d24af2370e29938d3244891987be665b6f8537b53d5&o=&hp=1', 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/218924699.jpg?k=67e6b968301a7bdb70d21738f16892fe2fd3281404d23974f4fe6759899534cb&o=&hp=1'], 'links_list_max200': ['https://cf.bstatic.com/xdata/images/hotel/max200/239649247.jpg?k=2853349c029e70cd2c7c813511feba4bc717a080e6a15b1f91a868107a7e99ee&o=&hp=1', 'https://cf.bstatic.com/xdata/images/hotel/max200/218942016.jpg?k=f2f051af7376417b834cb3a1f4bb3079b915f24995fe931f580a31c51d60bcba&o=&hp=1']}]


# I need you get data of data1 end sorted this data such way to be get the next result,
# I want to get nessesarly like that:
# data_sorted = [{
#     'id_photo': '199518553',
#     'links_list_max1280x900': 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/199518553.jpg?k=da6cedb48aa5589d95effdc1d4c7140e303b7f3465607232fdb5db031de1d006&o=&hp=1', 'links_list_max1024x768': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/199518553.jpg?k=555e05443c65a66ffbbbbcd42ae3dc71e5b8149140b5d5db74656b4205cf75b3&o=&hp=1', 'links_list_max200': 'https://cf.bstatic.com/xdata/images/hotel/max200/199518553.jpg?k=3e14243562a5f45589984c2d6030b2586cf0c13fa4a4c6287af109b6e76c678f&o=&hp=1'}, 
#  {
#     'id_photo': '239649247',
#     'links_list_max1280x900': 'https://cf.bstatic.com/xdata/images/hotel/max1280x900/239649247.jpg?k=da6cedb48aa5589d95effdc1d4c7140e303b7f3465607232fdb5db031de1d006&o=&hp=1', 'links_list_max1024x768': 'https://cf.bstatic.com/xdata/images/hotel/max1024x768/239649247.jpg?k=555e05443c65a66ffbbbbcd42ae3dc71e5b8149140b5d5db74656b4205cf75b3&o=&hp=1', 'links_list_max200': 'https://cf.bstatic.com/xdata/images/hotel/max200/239649247.jpg?k=3e14243562a5f45589984c2d6030b2586cf0c13fa4a4c6287af109b6e76c678f&o=&hp=1'}, 
 
#  ]

# please turn your attention on unik id wich any links have (9 number). This is criteri for selected data1.
# Write me python code how can I do it 





#             #    with open('review_test_doubleReq_2.html', 'w', encoding='utf-8') as f:
#             #         f.write(r.text)     
# # import main
# from bs4 import BeautifulSoup
# import re


# def page_scraper_photos(data_upz_hotels, resHtml):
#     result_photos_upz = []
#     print('hello photos!')
#     try:
#         hotelid = ''        
#         hotelid = data_upz_hotels["hotel_id"]        
#     except:
#         pass
#     try:
#         soup1 = BeautifulSoup(resHtml, "lxml")
#     except Exception as ex:
#         print(f"str226___{ex}")

#     try:
#         list_photo = []
#         imgBlock1 = soup1.find_all('a', attrs={'class': 'bh-photo-grid-item', 'class': 'bh-photo-grid-side-photo', 'class': 'active-image' }) 
#         imgBlock2 = soup1.find('div', attrs={'id': 'hotel_main_content'}).find_all('div', class_='bh-photo-grid-thumb-cell')
#         # print(f"str 122________ {len(imgBlock2) + len(imgBlock1)}") 
#         try:
#             photo_item_large = ''
#             photo_item_large =  imgBlock1[0].find('img').get('src')
#             # print(photo_item_large)
#         except Exception as ex:
#             print(f"str45__{ex}") 
#         try:
#             url_square60 = ''
#             url_square60 = imgBlock2[0].find('a').find('img').get('src')
#             # print(photo_item_large)

#         except Exception as ex:
#             print(f"str52__{ex}")

#         try:
#             for src in imgBlock1:
#                 try:
#                     photo_item_src = src.find('img').get('src')
#                     # print(photo_item_src)
#                 except:
#                     pass 

#                 try:
#                     photo_item_id = src.get('data-id')
#                 except:
#                     pass 

#                 try:
#                     photo_item_title = src.find('img').get('alt')
#                     # print(photo_item)
#                     # photo_list_src.append(photo_item_title) 
#                 except:
#                     pass 
#                 list_photo.append({
#                     'photo_item_src': photo_item_src,
#                     'photo_item_id': photo_item_id,
#                     'photo_item_title': photo_item_title,
#                 }) 
#         except Exception as ex:
#             print(f"str65__{ex}") 

#         try:
#             for src in imgBlock2:
#                 if src.find('a').find('img').get('src') != None:
#                     try:
#                         photo_item_src = src.find('a').find('img').get('src')
#                         # print(photo_item)
#                         # photo_list_src.append(photo_item_src) 
#                     except:
#                         pass 

#                     try:
#                         photo_item_id = src.find('a').get('data-id')
#                     except:
#                         pass 

#                     try:
#                         photo_item_title = src.find('a').find('img').get('alt')
#                     except:
#                         pass

#                     list_photo.append({
#                         'photo_item_src': photo_item_src,
#                         'photo_item_id': photo_item_id,
#                         'photo_item_title': photo_item_title,
#                     }) 
#         except Exception as ex:
#             print(f"str94__{ex}")

#         try:
#             photoRes = []
#             clean_links_set_max1280x900 = set()
#             clean_links_set_max1024x768 = set()
#             clean_links_set_max200 = set()
#             clean_links_list_max1280x900 = []
#             clean_links_list_max1024x768 = []
#             clean_links_list_max200 = []
#             photo_data1 = []
#             photo_data2 = []
#             photo_data3 = []
#             id_photo = []
#             id_photo2 = []
#             result_photo = [] 


#             # https://cf.bstatic.com/xdata/images/hotel/square60/

#             words = resHtml.split()
#             links = set()
#             for word in words:
#                 if re.search(r"https://cf\.bstatic\.com/xdata/images/hotel.*", word):
#                     links.add(word)
#             dirty_links = list(links)
#             for link in dirty_links:
#                 match = re.search(r"https://cf\.bstatic\.com/xdata/images/hotel/max1280x900.*?&hp=1", link)
#                 if match:
#                     clean_links_set_max1280x900.add(match.group(0))
#             for link in dirty_links:
#                 match = re.search(r"https://cf\.bstatic\.com/xdata/images/hotel/max1024x768.*?&hp=1", link)
#                 if match:
#                     clean_links_set_max1024x768.add(match.group(0))
#             for link in dirty_links:
#                 match = re.search(r"https://cf\.bstatic\.com/xdata/images/hotel/max200.*?&hp=1", link)
#                 if match:
#                     clean_links_set_max200.add(match.group(0))

#             clean_links_list_max1280x900 = list(clean_links_set_max1280x900)
#             clean_links_list_max1024x768 = list(clean_links_set_max1024x768)
#             clean_links_list_max200 = list(clean_links_set_max200)

#             photoRes.append({
#                 "links_list_max1280x900": clean_links_list_max1280x900,
#                 "links_list_max1024x768": clean_links_list_max1024x768,
#                 "links_list_max200": clean_links_list_max200, 

#             })
#             # print(len(clean_links_list_max1280x900))
#             # print(len(clean_links_list_max1024x768))
#             # print(len(clean_links_list_max200))
#             ids = set()
#             for link in photoRes[0]['links_list_max1280x900']:
#                 ids.add(link.split('/')[-1].split('.')[0])
#             id_photo = list(ids)
#             for id in id_photo:
#                 for x in photoRes[0]['links_list_max1280x900']:       
#                     if id == x.split('/')[-1].split('.')[0]:
#                         photo_data1.append(x)
#             for link in photo_data1:
#                 id_photo2.append(link.split('/')[-1].split('.')[0])
#             for id in id_photo2:
#                 for y in photoRes[0]['links_list_max1024x768']:       
#                     if id == y.split('/')[-1].split('.')[0]:
#                         photo_data2.append(y)
#             for id in id_photo2:
#                 for z in photoRes[0]['links_list_max200']:       
#                     if id == z.split('/')[-1].split('.')[0]:
#                         photo_data3.append(z)

#             for i, id in enumerate(id_photo2):
#                 result_photo.append({
#                     'id_photo': id,
#                     'photo_max1280x900': photo_data1[i],
#                     'photo_max1024x768': photo_data2[i],
#                     'photo_max200': photo_data3[i]
#                 })
#         except Exception as ex:
#             print(f"str115{ex}")

#         result_photos_upz.append({
#             "id": "",
#             "hotelid": hotelid,
#             "url_max": photo_item_large,
#             "url_square60": url_square60,
#             "list_photo_1-7,10": list_photo,
#             "all_photos": result_photo

#         })
#         # print(result_photos_upz)      
          
#     except Exception as ex:
#         print(f"str105__{ex}") 
#         # return None 

#     try:
#         return result_photos_upz[0]   
#     except:
#         return None
        
