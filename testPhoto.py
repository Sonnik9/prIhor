import requests
from bs4 import BeautifulSoup
import re
import smart_headers
import json

url = "https://www.booking.com/hotel/zm/le-elementos-by-mantis.ru.html?label=gen173nr-1BCAso_AFCFmxlLWVsZW1lbnRvcy1ieS1tYW50aXNIM1gEaOkBiAEBmAEhuAEZyAEM2AEB6AEBiAIBqAIDuAKGyJCiBsACAdICJGE5M2JlYWQ4LThiNzctNDBkOS05ZTA0LTJkOTZiMzI0NDcyNNgCBeACAQ&sid=52c12d695260d02d8a98fb123e5b9e1e&dist=0&keep_landing=1&sb_price_type=total&type=total&"

url = "https://www.booking.com/hotel/uz/hilton-tashkent-city.ru.html?label=gen173nr-1BCAso7gFCFGhpbHRvbi10YXNoa2VudC1jaXR5SDNYBGjkAYgBAZgBIbgBGcgBDNgBAegBAYgCAagCA7gC6O2KogbAAgHSAiQ0MTA3MTA1Mi03ZjhkLTQ1NTktODE3YS1lZDQ4NzQ3Y2I4ZmPYAgXgAgE&sid=52c12d695260d02d8a98fb123e5b9e1e&dist=0&group_adults=2&keep_landing=1&sb_price_type=total&type=total&"

r = requests.get(url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
soup = BeautifulSoup(r.content, "html.parser")
resHtml = r.text
# with open("responsePhotos_1.html", "w") as f:
#     f.write(resHtml)

# try:
#     clean_links_set_max1280x900 = set()
#     clean_links_list_max1280x900 = []
#     result_photo = [] 

#     words = r.text.split()
#     links = set()
#     for word in words:
#         if re.search(r"https://cf\.bstatic\.com/xdata/images/hotel.*", word):
#             links.add(word)
#     dirty_links = list(links)
#     for link in dirty_links:
#         match = re.search(r"https://cf\.bstatic\.com/xdata/images/hotel/max1280x900.*?&hp=1", link)
#         if match:
#             clean_links_set_max1280x900.add(match.group(0))
#     clean_links_list_max1280x900 = list(clean_links_set_max1280x900)
#     for link in clean_links_set_max1280x900:
#         try:
#            id_photo = link.split('/')[-1].split('.')[0].strip()
#         except:
#             match = re.search(r"/(\d{9})\.", link)
#             if match:
#                 id_photo = match.group(1)
#                 print(id_photo)
#         # link
#         photo_max1024x768 = re.sub(r'max1280x900', 'max1024x768', link)
#         # link3 = link
#         photo_max200 = re.sub(r'max1280x900', 'max200', link)
#         result_photo.append({
#             'id_photo': id_photo,
#             'photo_max1280x900': link,
#             'photo_max1024x768': photo_max1024x768,
#             'photo_max200': photo_max200,
#         })
#     try:
#         with open(f'photo_list_test_n2.json', "w", encoding="utf-8") as file: 
#             json.dump(result_photo, file, indent=4, ensure_ascii=False)
#     except Exception as ex:
#         print(f"str226__{ex}") 

# except Exception as ex:
#      print(f"str115{ex}")









