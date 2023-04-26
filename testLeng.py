# import requests
# from bs4 import BeautifulSoup
# import re
# import smart_headers 

# description = ''

# # url = "https:\/\/www.booking.com\/hotel\/zm\/le-elementos-by-mantis.html"
# # url = "https:\/\/www.booking.com\/hotel\/uz\/hilton-tashkent-city.html"
# # url = "https://www.booking.com/hotel/vn/flamingo-venus-resort-luxury.html"

# url = 'https:\\/\\/www.booking.com\\/hotel\\/vn\\/flamingo-venus-resort-luxury.html'
# fixed_url = re.sub(r'\\/', '/', url)
# params = {'lang': ['ru', 'en', 'uk']}
# try:
#     r = requests.get(fixed_url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15), params=params)
#     print(r.status_code)
# except Exception as ex:
#     print(f"15_____{ex}")


# try:
#     if r.status_code == 200:
#         response_text = r.text

#         soup1 = BeautifulSoup(response_text, "lxml")
#         descriptionBlock = soup1.find('div', attrs={'class': 'hp_desc_main_content'}).find_all('p')
#         for p in descriptionBlock:
#             description += p.get_text() 
#         description = re.sub(r'<.*?>', '', description)
#         print(description)
#     else:
#         print(f'Response error: {r.status_code}') 

# except Exception as ex:
#     print(f"44_____{ex}")


# import requests
# from bs4 import BeautifulSoup
# import re
# import smart_headers 
# import time

# start_time = time.time() 


# url = "https:\/\/www.booking.com\/hotel\/zm\/le-elementos-by-mantis.html"
# url = "https:\/\/www.booking.com\/hotel\/uz\/hilton-tashkent-city.html"

# # url = 'https://www.booking.com/hotel/vn/flamingo-venus-resort-luxury.html'
# params = {'lang': ['en', 'ru', 'fr']}
# description = {}

# for lang in params['lang']:
#     fixed_url = re.sub(r'\\/', '/', url)
#     try:
#         r = requests.get(fixed_url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15), params={'lang': lang})
#         if r.status_code == 200:
#             response_text = r.text

#             soup1 = BeautifulSoup(response_text, "lxml")
#             description[lang] = ''
#             description_block = soup1.find("div", attrs={"class": "hp_desc_main_content"})
#             description[lang] = description_block.get_text(strip=True, separator="\n")
#         else:
#             print(f'Response error: {r.status_code}') 
#     except Exception as ex:
#         print(f"15_{ex}") 


# print(description) 

# finish_time = time.time() - start_time 
# print(finish_time)


import requests
from bs4 import BeautifulSoup 
import time
import smart_headers


start_time = time.time()  

url = "https://www.booking.com/hotel/vn/flamingo-venus-resort-luxury.html"

# params = {'lang': ['en', 'ru', 'fr']}

try:

    r = requests.get(url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15))
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    description_block = soup.find("div", attrs={"class": "hp_desc_main_content"})
    description = description_block.get_text(strip=True, separator="\n")
    print(description)
    finish_time = time.time() - start_time 
    print(finish_time)
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"Error occurred: {e}")

# python testLeng.py 




# import requests
# from bs4 import BeautifulSoup
# import re
# import smart_headers 

# url = 'https://www.booking.com/hotel/vn/flamingo-venus-resort-luxury.html'
# params = {'lang': ['en', 'ru', 'uk']}
# description = {}

# for lang in params['lang']:
#     fixed_url = re.sub(r'\\/', '/', url)
#     try:
#         r = requests.get(fixed_url, headers=smart_headers.random_headers(), timeout=(9.15, 30.15), params={'lang': lang})
#         if r.status_code == 200:
#             response_text = r.text

#             soup1 = BeautifulSoup(response_text, "lxml")
#             descriptionBlock = soup1.find('div', attrs={'class': 'hp_desc_main_content'}).find_all('p')
#             description[lang] = ''
#             for p in descriptionBlock:
#                 description[lang] += p.get_text() 
#             description[lang] = re.sub(r'<.*?>', '', description[lang])
#         else:
#             print(f'Response error: {r.status_code}') 
#     except Exception as ex:
#         print(f"15_{ex}")

# print(description)


# descriptionBlock = soup1.find('div', attrs={'class': 'hp_desc_main_content'}).find_all('p')
# for p in descriptionBlock:
#     description += p.get_text() 
# description = re.sub(r'<.*?>', '', description)
# print(description)