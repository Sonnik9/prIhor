from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import random 
from random import choice
import time
import csv
import json
from lxml import etree
import math
import re
from datetime import datetime
from fake_useragent import UserAgent 
import agVar 
from agVar import *
import sys 
import pandas as pd 
import openpyxl
from openpyxl import load_workbook 

yellowInfo = False   

def random_headers(argLink):   
    global yellowInfo
    if yellowInfo == True:
       agVar.agRestart() 
 
    if argLink == 'ebay.com':        
       uaG = choice(agVar.uagEbay())
    else: 
        uaG = choice(agVar.uagAmazon())   
            
    device_memoryHelper = [2,4,8,16,32]
    sett = set()
    finHeaders = []
    headFront = [{
            'authority': f"www.{argLink}",
            'accept': choice(agVar.desktop_accept), 
            'User-Agent': uaG,           
            'accept-language': choice(agVar.aceptLengv),           
            'origin': f'https://www.{argLink}',
            'device-memory': f'{choice(device_memoryHelper)}',
            # 'Transfer-Encoding': 'chunked',
            # 'Connection': 'keep-alive',
            # 'Server': 'Server',         
                   
            }]
    headersHelper = [       
            {"sec-fetch-dest": "empty"},
            {"sec-fetch-mode": "cors"},
            {"sec-fetch-site": "same-origin"},
            {"accept-ch": "sec-ch-ua-model,sec-ch-ua-platform-version,sec-ch-ua-full-version"},
            {'cache-control': 'no-cache'},
            {'content-type': 'application/json'},
            {'rtt': '200'},
            {"ect": "4g"},
            {'sec-fetch-user': '?1'},
            {"viewport-width": "386"},            
            {'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"'},
            {'upgrade-insecure-requests': '1'}
    ]
    headersHelperFormated = []
    strr = ''
    for i in headersHelper[0:len(headersHelper)-random.randrange(0,len(headersHelper))]:
        strr += ((str(choice(headersHelper)))[1:-1]).strip() + ',' + ' '  
         
    sett.add(strr)    
    headersHelperFormated = list(sett)    
    finHeaders = headFront + headersHelperFormated
    finHeaders[1] = eval("{" + finHeaders[1] + "}")    
    finfin = finHeaders[0]|finHeaders[1]    
    return finfin 

def proxyGenerator(proxArg):
    proxiess = {       
        "https": f"http://{proxArg}"          
    }   
    return proxiess

def linksHandlerAmazon(dataForHandler):
    global yellowInfo    
    agrForAmazon = 'amazon.com' 
   
    try:
        arrContent = f"{dataForHandler}".split('SamsonovNik')      
        try:
            proxArg = arrContent[1]                           
        except:
            proxArg = arrContent[0]
        try:
            urlAm = arrContent[9].strip()
        except:
            pass 
        try:                
            oldCategoryLOwer = arrContent[6].strip().lower()
        except:
            pass
        try:                
            oldBrandLower = arrContent[7].strip().lower()
        except:
            pass  
        try:
            determinantChanell = int(arrContent[-1]) 
        except:
            determinantChanell = 1

    except:
        pass
    
    # time.sleep(random.randrange(1, 10))
    for sesCountt in range(2):        
        flagPriceAm = False 
        resultAm = []         
        newPrice = ''
        priceCorrector = 0 
        newCategory = '' 
        newBrand = ''
        brandAdd = '' 
        remarksAm = ''
        remarksAm2 = ''      
        newPriceContr = '' 
        deliveryAmPrice = ''

        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)
        try:           
            if determinantChanell == 2:                     
               r = requests.get(urlAm, headers=random_headers(agrForAmazon), proxies=proxyGenerator(proxArg), timeout=(9.15, 30.15))          
            else:
               r = requests.get(urlAm, headers=random_headers(agrForAmazon), timeout=(9.15, 30.15))          

            if str(r) == '<Response [200]>':
                yellowInfo = False
                
            if str(r) == '<Response [503]>': 
                if determinantChanell == 2:               
                   print(f'Желтая карточка от Amazon. Прокси: {proxArg} (см файл proxyAm.txt)') 
                else: 
                   print('Желтая карточка от Amazon')              
                remarksAm = '503 err' + '\n'                       
                yellowInfo = True            
                proxArg = arrContent[0] 
                if sesCountt == 1: 
                    pass                  
                else:
                    continue 
                              
            if str(r) == '<Response [403]>':
                print('Amazon отверг запрос')               
                remarksAm = '403 err' + '\n'
                if sesCountt == 1: 
                    pass                  
                else:
                    continue         
                
            if str(r) == '<Response [504]>':
                pass  
            if str(r) == '<Response [404]>':
                remarksAm = 'The page not found' + '\n'

            if str(r) == '<Response [400]>':
                pass 
            if str(r) == '<Response [443]>':
                print('Проблемы с подключением...')                                
                pass 

            try:              
                soup2 = BeautifulSoup(r.text, "lxml")                
            except Exception as ex:
                # print(ex)
                pass

            #  price /////////////////////
            try:            
                newPrice = soup2.find('span', class_='a-offscreen').get_text().strip()   
                try:
                    for j in range(len(newPrice)):                                        
                        try:                                    
                            match = re.search(r'[$]', newPrice[j])
                            if match:
                                flagPriceAm = True
                                break 
                        except: 
                            continue     
                except:
                    pass
            except Exception as ex:
                # print(f" str 228 {ex}")
                pass
                
            if flagPriceAm == False:           
                try:
                    newPriceContr = soup2.find('div', class_='a-box a-last').find('div', {'id': 'corePrice_feature_div'}).find('span', class_='a-offscreen').get_text().strip()
                    try:
                        for j in range(len(newPriceContr)):                                        
                            try:                                    
                                match = re.search(r'[$]', newPriceContr[j])
                                if match:
                                    flagPriceAm = True
                                    break 
                            except: 
                                continue     
                    except:
                        pass
                except:
                    pass 
                if flagPriceAm == True and newPriceContr != None and newPriceContr != '':
                    newPrice = newPriceContr                
    
            #  delivery price //// 
            try:
                deliveryAmPrice = soup2.find('div', {'id': 'deliveryBlockMessage'}).find('div', class_='a-spacing-base').find('span').get('data-csa-c-delivery-price').strip()
                try:
                    if deliveryAmPrice.lower() == 'free':
                        priceCorrector = 0
                    else:
                        priceCorrector = float(deliveryAmPrice[1:])
                except:
                    pass
                    
            except:
                try:
                    deliveryAmPrice = soup2.find('div', {'id': 'deliveryBlockMessage'}).find('div', class_='a-spacing-base').find('span').get_text().strip()
                    delivArr = deliveryAmPrice.strip().split(' ')
                    try:
                        for j in range(len(delivArr)):                                        
                            try:                                    
                                match = re.search(r'[$]\S', delivArr[j])
                                if match:
                                    priceCorrector = float(delivArr[j][1:])
                                    break 
                            except: 
                                continue     
                    except:
                        pass 
                    try:
                        for j in range(len(delivArr)):                                        
                            try:                                    
                                match = re.search(r'free', delivArr[j].strip().lower())
                                if match:
                                    priceCorrector = 0
                                    break 
                            except: 
                                continue     
                    except:
                        pass                   
                except:
                    pass 
            try:
                newPriceFormated = float(newPrice[1:])
                newPriceFormated = round(newPriceFormated + priceCorrector, 2)                          
            except:
                pass 
            try:                
                newPrice = float(newPriceFormated)
            except:            
                remarksAm2 += 'Price not found' + '\n'
                newPrice = '' 
                
            # category ///////////////////////////////////// 
            try:
                newCategory = soup2.find('span', class_='a-list-item').find('a', attrs={'class': 'a-link-normal', 'class': 'a-color-tertiary'}).get_text().strip().lower()          
                # print(newCategory)
            except Exception as ex:
                pass
                # print(ex) 
            if newCategory == None or newCategory == '':
                newCategory = ''
                remarksAm2 += 'Category not found' + '\n'  
                
            # brand ////////////////////////////////
            try:
                newBrand = soup2.find('a', attrs={'id': 'bylineInfo', 'class': 'a-link-normal'}).get_text().strip().lower()             
            except:
                pass  
            if newBrand != '' and newBrand != None:           
                try:               
                    newArrBrand = newBrand.split(':')               
                    if len(newArrBrand) == 2:
                        newBrand = newArrBrand[1].strip().lower()
                    else:                    
                        newArrBrand2 = newBrand.split(' ')
                        newBrand = ''
                        for br in newArrBrand2[2:-1]:
                            newBrand += br.strip() + ' '
                        newBrand = newBrand.strip().lower()                   
                except:
                    pass           
            try:
                brandAdd = soup2.find('td', class_='a-span9').find('span').get_text().strip().lower()
            except:
                pass 
            if newBrand == None or newBrand == '' or newBrand == ' ':
                newBrand = brandAdd 
            if newBrand == None or newBrand == '' or newBrand == ' ':                
                newBrand = ''
                remarksAm2 += 'Brand not found' + '\n'

            if oldCategoryLOwer != newCategory and newCategory != '' and (oldCategoryLOwer != '' and oldCategoryLOwer != None and oldCategoryLOwer != 'nan'):
                remarksAm2 += 'Category was changed' + '\n'
                
            if oldBrandLower != newBrand and newBrand != '' and (oldBrandLower != '' and oldBrandLower != None and oldBrandLower != 'nan'):
                remarksAm2 += 'Brand was changed' + '\n'
                
            if remarksAm == '':
                remarksAm = remarksAm2
            
            resultAm.append({
                'dataForHandler': dataForHandler,
                'newPriceAm': newPrice,
                'newCategoryAm': newCategory,
                'newBrand': newBrand,
                'remarksAm': remarksAm                            
            })

        except Exception as ex:
            # print(f'362 str {ex}')
            if sesCountt == 1:
                try:                   
                    if remarksAm == '': 
                        remarksAm = remarksAm2 
                    resultAm.append({
                        'dataForHandler': dataForHandler,
                        'newPriceAm': newPrice,
                        'newCategoryAm': newCategory,
                        'newBrand': newBrand,
                        'remarksAm': remarksAm                                    
                    })
                    # print(resultAm) 
                    # return 
                    return resultAm[0]
                except:
                    return 
            else:
                continue                  
        try: 
            # print(resultAm)
            # return
            return resultAm[0]
        except:
            return           
             
# dataForHandler = 'https://www.amazon.com/dp/B08G8SV1BB'           
# dataForHandler = 'https://www.amazon.com/dp/B072MQYNNX'            
# dataForHandler = 'https://www.amazon.com/dp/B01M7TJRVZ' 
# dataForHandler = 'https://www.amazon.com/dp/B07RX8M2BC' 
# dataForHandler = 'https://www.amazon.com/gp/product/B0B3J3LLFP?th=1&psc=1' 
# dataForHandler = 'https://www.amazon.com/dp/B072VVKPMD'
# dataForHandler = 'https://www.amazon.com/dp/B0038JOZ56' 
# dataForHandler = 'https://www.amazon.com/dp/B0015SBPCS'       
# linksHandlerAmazon(dataForHandler)
        
def linksHandlerEbay(dataForHandler):
    global yellowInfo  
    agrForEbey = 'ebay.com'
          
    try:
        arrContent = f"{dataForHandler}".split('SamsonovNik')
        # if len(arrContent) > 1:
        try:
            proxArg = arrContent[0]
            # print(proxArg)
        except:
            proxArg = arrContent[1]
        try:
            urlE = arrContent[8]
        except:
            pass
        try:
            determinantChanell = int(arrContent[-1]) 
        except:
            determinantChanell = 1
        # else:            
        #     determinantChanell = 1
        #     urlE = f"{dataForHandler}".strip()  
    except:
        pass
    
    for sesCountt in range(2):
        resultE = []        
        price = ''
        priceCorrectorE = 0
        quanity = ''
        delivery = []
        delivery_main = ''       
        shippingArr = []
        shipping = ''
        remarksEbay = ''
        remarksEbay2 = ''  

        k = 2 / random.randrange(1, 5)
        m = 1 / random.randrange(1, 11)
        g = random.randrange(1, 5)
        n = round(g + k + m, 2) 
        time.sleep(n)
        try:
            if determinantChanell == 2:           
               r = requests.get(urlE, headers=random_headers(agrForEbey), proxies=proxyGenerator(proxArg), timeout=(9.15, 30.15))             
            else:
               r = requests.get(urlE, headers=random_headers(agrForEbey), timeout=(9.15, 30.15))                
                      
            if str(r) == '<Response [200]>':
                yellowInfo = False      
            if str(r) == '<Response [503]>':                
                if determinantChanell == 2:               
                   print(f'Желтая карточка от Ebay. Прокси: {proxArg} (см файл proxyE.txt)') 
                else: 
                   print('Желтая карточка от Ebay')  
                remarksEbay = '503 err' + '\n'                       
                yellowInfo = True            
                proxArg = arrContent[1] 
                if sesCountt == 1: 
                    pass                  
                else:
                    continue       

            if str(r) == '<Response [403]>':
                print('Ebay отверг запрос') 
                remarksEbay = '403 err' + '\n' 
                if sesCountt == 1: 
                    pass                  
                else:
                    continue                      

            if str(r) == '<Response [504]>':
                pass  
            if str(r) == '<Response [404]>':
                remarksEbay = 'The page not found' + '\n'
         
            if str(r) == '<Response [400]>':
                pass 
            if str(r) == '<Response [443]>':
                pass
            try:            
               soup = BeautifulSoup(r.text, "lxml")
            except:
               pass          
            
            try:          
                price = soup.find('div', class_='x-price-primary').find('span', class_='ux-textspans').get_text().strip()        
            except: 
                pass               
            if price == None:                
                price = ''               
       
            try:
                quanity = soup.find('div', class_='d-quantity__availability').find('span').get_text().strip()                
            except:
                try:
                    quanity = soup.find('span', id='qtySubTxt').find('span').get_text().strip()                    
                except:
                    try:
                        quanity = soup.find('span', id='qtySubTxt').find('span').find('span').get_text().strip() 
                    except:
                        pass                            
            if quanity == None or quanity == '':
                remarksEbay2 += 'Stock not found' + '\n'
                quanity = '' 
                
            try:
                delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans--BOLD')
                delivery_main = f"Estimated between {delivery[0].get_text()} and {delivery[1].get_text()}"
                for dell in delivery[0:-2]:
                    delivery_main += dell.get_text()                    
            except:
                try:
                    delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans')
                    delivery_main = f"Estimated between {delivery[0].get_text()} and {delivery[1].get_text()}"
                    for dell in delivery[0:-2]:
                        delivery_main += dell.get_text() 
                except: 
                    try:
                        delivery = soup.find('div', class_='ux-labels-values--deliverto').find('div', class_='col-9').find('div').find_all('span', class_='ux-textspans')
                        delivery_main = f"{delivery[0].get_text()}"
                    except Exception as ex:
                        # print(ex)                      
                        pass  
            if delivery_main == None:                
                delivery_main = ''
            try:
                shippingArr = soup.find('div', class_='ux-labels-values__values-content').find_all('span')
                for dell2 in shippingArr:
                    shipping += dell2.get_text().strip() + ' '       
            except Exception as ex:
                # print(ex)
                pass 
            if shipping == None:                
                shipping = ''
            
            try:
                delivery_main = delivery_main + '\n' + shipping  
                delivery_main = delivery_main.split('|')[0].strip()         
            except:                
                pass 
            if delivery_main == None or delivery_main  == '' or len(delivery_main) > 300 or len(delivery_main) < 10:
                remarksEbay2 += 'Delivery not found' + '\n' 
                delivery_main = ''
            
            try:                
                deliveryArr = delivery_main.split(' ')
                try:
                    for j in range(len(deliveryArr)):                                        
                        try:                                    
                            match = re.search(r'[$]\S', deliveryArr[j])
                            if match:
                                priceCorrectorE = float(deliveryArr[j][1:])
                                # print(priceCorrectorE)
                                break 
                        except: 
                            continue     
                except:
                    pass 
                
            except:
                pass 
            try:
                newPriceFormated = float(price.split(' ')[1][1:])                                          
            except:
                try:
                    newPriceFormated = float(price.split('/')[0].split(' ')[1][1:]) 
                    remarksEbay2 += 'ea'
                except:
                    pass
            try:
                newPriceFormated = round(newPriceFormated + priceCorrectorE, 2)                
                price = float(newPriceFormated)  
            except:            
                remarksEbay2 += 'Price not found' + '\n'
                price = '' 
            
            if remarksEbay == '': 
                remarksEbay = remarksEbay2  

            resultE.append({
                "dataForHandler": dataForHandler,               
                "price": price,                                
                "quanity": str(quanity),                
                "delivery": str(delivery_main),
                "remarksEbay": remarksEbay,                    
            })           
  
        except Exception as ex:
            # print(f'660 str {ex}')
            if sesCountt == 1:
                try:                    
                    if remarksEbay == '': 
                        remarksEbay = remarksEbay2 
                    resultE.append({
                        "dataForHandler": dataForHandler,               
                        "price": price,                                
                        "quanity": str(quanity),                
                        "delivery": str(delivery_main),
                        "remarksEbay": remarksEbay,                    
                    }) 
                    # print(resultE) 
                    # return 
                    return resultE[0]
                except:
                    return 
            else:
                continue                  
        try: 
            # print(resultE)
            # return
            return resultE[0]
        except:
            return
# dataForHandler = 'https://www.ebay.com/itm/EDM-ROUTER-BITS-SET-35-pc-1-4-inch-Shank-CARBIDE-KIT-ALUMINUM-CASE-SAE/312439681819?hash=item48bedb331b:g:EUwAAOSw-V1cR1L1'         
# dataForHandler = 'https://www.ebay.com/itm/Botanicare-Ebb-Flow-Barbed-Fitting-1-2-Bulkhead-hydroponics-tub-head-in/251313018420?hash=item3a836c5634:g:y8EAAMXQyfFR-F-T'
# dataForHandler = 'https://www.ebay.com/itm/392792144109?epid=2255546870&hash=item5b743c78ed:g:E0sAAOSwaTJetbyG'
# dataForHandler = 'https://www.ebay.com/itm/Createx-Airbrush-Colors-5310-Pearl-White-2oz-water-based-pearlized-paint/262813714995?hash=item3d30eb0a33:g:GusAAOSwnHZYf9P-'
# dataForHandler ='https://www.ebay.com/itm/271763240232?hash=item3f4659f528:g:etkAAOSw-W5U0CFZ&amdata=enc%3AAQAHAAAA4O5rQTyvHnal1FVFr349S%2FYb8kKhf5mn0BDdglbMuWX8%2BhxrYNXB9P230StRF7RD2Et1DWv1KA8uKqw%2BLdutBoAkF4swUkxPv8gefe2F6gdsHcWbFQIBdeAAXItZ%2FYl71NI0Gv%2BpXbC1ERUF0X2t6Jy7w6XKpZJ%2ByItq%2FVkNfyHna331O39p7B2wZxOrUah7IkydThDd1fs6tiULQLSYAo00CO27I8UsQCGuuG3B2gnG7BDJ4zNAxwMPrxPb%2B3I3uQBm%2B5SxvzI2kJ8UDbsIPUBem%2FuEQdKNZoHAhn%2BrUF0o%7Ctkp%3ABk9SR_SB457GYQ'
# dataForHandler = 'https://www.ebay.com/itm/33-207-Olympia-Tools-TURBOFOLD-ORANGE-Turbo-Fold-Folding-Knife-with-5-Blades/233198873913?hash=item364bbc6d39:g:UO4AAOSwwo1Xc~lm'
# dataForHandler = 'https://www.ebay.com/itm/CAP-HORZ-TERM-DIRECT-4/272781125250?hash=item3f8305a682:g:nXgAAOSwpxNfvcXw'
# dataForHandler = 'https://www.ebay.com/itm/GOAT-XING-Funny-Novelty-Crossing-Sign/221946948940?hash=item33ad11ad4c:g:TlEAAOSwSuNaYMmo'
# linksHandlerEbay(dataForHandler)

def matherFunc(dataForHandler): 
    try:
       eBayAnswer = linksHandlerEbay(dataForHandler)
    except:
       eBayAnswer = ''
    try:
       AmAnswer = linksHandlerAmazon(dataForHandler)
    except:
       AmAnswer = ''
    
    try:
        return [eBayAnswer, AmAnswer]
    except:
        return []    

def fatherFunk2(dataForHandler):    
    from mpire import WorkerPool    
    n = 21    
    with WorkerPool(n_jobs = n) as p2:                      
        finRes = p2.map(matherFunc, dataForHandler)          
        writerAndFilter(finRes)
        finRes = [] 
        dataForHandler = []
        
def fatherFunk1(dataForHandler):      
    from mpire import WorkerPool          
    finResArr = [] 
    total = []
    n = 21
    vpnFraction = random.randrange(275,325) 
    
    for i in range(0, len(dataForHandler), vpnFraction):        
        n1 = i 
        n2 = i+vpnFraction
        if n2 > len(dataForHandler):
            n2 = len(dataForHandler)
        if n2 != len(dataForHandler) and i != 0:  
            yellowInput = input('Пожалуйста смените VPN', )
            if yellowInput:
                pass
        with WorkerPool(n_jobs = n) as p2:                      
            finRes = p2.map(matherFunc, dataForHandler[n1:n2])
            finResArr.append(finRes)                     
    for item in finResArr:
        total +=item
    writerAndFilter(total)     
    dataForHandler = [] 
    finRes = []  

def writerAndFilter(total):
    print('Запись результатов')
    total2 = []
    total3 = []
 
    try:
        for item in total:
            if item[0]['dataForHandler'].split('SamsonovNik') != '' and item[0]['dataForHandler'].split('SamsonovNik') != None:
                try:
                  total2 = item[0]['dataForHandler'].split('SamsonovNik') 
                except Exception as ex:
                    print(ex)
            else:
                try:
                   total2 = item[1]['dataForHandler'].split('SamsonovNik') 
                except Exception as ex:
                    print(ex)   
            
            if str(total2[2]).lower() == 'nan':
                total2[2] = ''
            if str(total2[3]).lower() == 'nan':
                total2[3] = '' 
            if str(total2[4]).lower() == 'nan':
                total2[4] = '' 
            if str(total2[5]).lower() == 'nan':
                total2[5] = '' 
            if str(total2[6]).lower() == 'nan':
                total2[6] = '' 
            if str(total2[7]).lower() == 'nan':
                total2[7] = '' 
            if str(total2[8]).lower() == 'nan':
                total2[8] = '' 
            if str(total2[9]).lower() == 'nan':
                total2[9] = ''
            if str(total2[10]).lower() == 'nan':
                total2[10] = ''
            if str(total2[11]).lower() == 'nan':
                total2[11] = '' 
            if str(total2[12]).lower() == 'nan':
                total2[12] = '' 
            if str(total2[13]).lower() == 'nan':
                total2[13] = ''
            if str(total2[14]).lower() == 'nan':
                total2[14] = '' 
            if str(total2[15]).lower() == 'nan':
                total2[15] = '' 
            if str(total2[16]).lower() == 'nan':
                total2[16] = '' 
            if str(total2[17]).lower() == 'nan':
                total2[17] = '' 
            if str(total2[18]).lower() == 'nan':
                total2[18] = ''
                                             
            try:
                total3.append({
                    "Data": str(total2[2]),
                    "SKU": str(total2[3]),
                    "Item": str(total2[4]),
                    "ASIN": str(total2[5]),
                    "Category": str(item[1]['newCategoryAm']),
                    "Brand": str(item[1]['newBrand']),   
                    "Link ebay": str(total2[8]),
                    "Link Amazon": str(total2[9]),
                    "Old price Amazon": total2[10],
                    "New price Amazon": item[1]['newPriceAm'],        
                    "Remarks Amazon": str(item[1]['remarksAm']),
                    "Old price ebay": total2[13],
                    "New price Ebay": item[0]['price'], 
                    "Stock ebay": str(item[0]['quanity']),
                    "Delivery time ebay": str(item[0]['delivery']),                   
                    "Remarks Ebay": str(item[0]["remarksEbay"]),
                    "Рой": str(total2[18]),           
                }) 
            except Exception as ex:
                print(ex) 
                pass
    except Exception as ex:
        pass
        # print('Что-то пошло не так...')
        # print(ex)    
    
    now = datetime.now() 
    curentTimeForFile = now.strftime("%d_%m_%Y__%H_%M") 
    try:       
        with open(f'./resultData/{curentTimeForFile}.json', "a", encoding="utf-8") as file: 
            json.dump(total3, file, indent=4, ensure_ascii=False)       
                        
        with open(f'./resultData/{curentTimeForFile}.csv', 'w', newline='', encoding='cp1251', errors="ignore") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(["Data", "SKU", "Item", "ASIN", "Category", "Brand", "Link ebay", "Link Amazon", "Old price Amazon", "New price Amazon", "Remarks Amazon", "Old price ebay", "New price Ebay", "Stock ebay", "Delivery time ebay", "Remarks Ebay", "Рой"])
            for item in total3:
                writer.writerow([item["Data"], item ["SKU"], item["Item"], item["ASIN"], item["Category"], item["Brand"], item["Link ebay"], item["Link Amazon"], item["Old price Amazon"], item["New price Amazon"], item["Remarks Amazon"], item["Old price ebay"], item["New price Ebay"], item["Stock ebay"], item["Delivery time ebay"], item["Remarks Ebay"], item["Рой"]])
    except:
        pass    
      
    total = []
    total2 = []
    total3 = []

def dataTabl():
    dataTablName = input('Пожалуйста введите название гугл таблицы', )
    dataSheetlName = input('Пожалуйста введите название страницы гугл таблицы', )    
    return [dataTablName, dataSheetlName]    

def main():   
    arrHelpProxyE = [] 
    arrHelpProxyAm = []    
    
    with open("proxyE.txt", encoding="utf-8") as f1:    
        prLiE = ''.join(f1.readlines()).split('\n')
        prLiE = list(i.strip() for i in prLiE)
        prLiE = list(filter(lambda item: item != '', prLiE))
                    
    with open("proxyAm.txt", encoding="utf-8") as f2:    
        prLiAm = ''.join(f2.readlines()).split('\n')
        prLiAm = list(i.strip() for i in prLiAm)
        prLiAm = list(filter(lambda item: item != '', prLiAm))   
    # выбор способа подключения /////////////////////////////////////
    determinantChanell = input('Выберите способ подключения: 1 - VPN; 2 - Proxy', )
    try:
        determinantChanell = int(determinantChanell.strip())
    except:        
        determinantChanell = 1
   
    start_time = time.time()     
    # открытие файла на чтение //////////////////////////////////////    

    try:
        dataTablAnsw = dataTabl()
        xl = pd.ExcelFile(f'./soursData/{dataTablAnsw[0]}.xlsx')
        csvList = xl.parse(f'{dataTablAnsw[1]}') 
        # print(csvList)
    except:
        try:
            csvList = pd.read_csv(f'./soursData/{dataTablAnsw[0]}.csv', sep=';', encoding='cp1251')
            # print(csvList)           
        except:
            try:
                print('Данные таблицы введены некорректно. Пожалуйста попробуйте еще раз')
                dataTablAnsw = dataTabl()
                xl = pd.ExcelFile(f'./soursData/{dataTablAnsw[0]}.xlsx')
                csvList = xl.parse(f'{dataTablAnsw[1]}') 
            except:
                try:
                    csvList = pd.read_csv(f'./soursData/{dataTablAnsw[0]}.csv', sep=';', encoding='cp1251')
                except:
                    print('Программа вынуждена остановить работу')
                    sys.exit() 
            
    print('Старт...')
    # форматирование данных //////////////////////////////////////////////////////
    qCycleE = round(len(csvList['Link ebay']) / len(prLiE)) + 2
    qCycleAm = round(len(csvList['Link ebay']) / len(prLiAm)) + 2
    
    for _ in range(qCycleE):
        random.shuffle(prLiE)
        arrHelpProxyE += prLiE 
    for _ in range(qCycleAm):
        random.shuffle(prLiAm)
        arrHelpProxyAm += prLiAm
    dataForHandler = [f"{arrHelpProxyE[i]}SamsonovNik{arrHelpProxyAm[i]}SamsonovNik{str(csvList['Data'][i])}SamsonovNik{str(csvList['SKU'][i])}SamsonovNik{str(csvList['Item'][i])}SamsonovNik{str(csvList['ASIN'][i])}SamsonovNik{str(csvList['Category'][i])}SamsonovNik{str(csvList['Brand'][i])}SamsonovNik{str(csvList['Link ebay'][i])}SamsonovNik{str(csvList['Link Amazon'][i])}SamsonovNik{str(csvList['Old price Amazon'][i])}SamsonovNik{str(csvList['New price Amazon'][i])}SamsonovNik{str(csvList['Remarks Amazon'][i])}SamsonovNik{str(csvList['Old price ebay'][i])}SamsonovNik{str(csvList['New price Ebay'][i])}SamsonovNik{str(csvList['Stock ebay'][i])}SamsonovNik{str(csvList['Delivery time ebay'][i])}SamsonovNik{str(csvList['Remarks Ebay'][i])}SamsonovNik{str(csvList['Рой'][i])}SamsonovNik{determinantChanell}" for i in range(len(csvList['Link ebay']))]   

    # запуск основной функции /////////////////////////////////////////////////////////////// 
    
    if determinantChanell == 2:
       fatherFunk2(dataForHandler)
    else:
       fatherFunk1(dataForHandler) 
    arrHelpProxyE = [] 
    arrHelpProxyAm = []    
               
    finish_time = time.time() - start_time    
    print(f"Общее время работы парсера:  {math.ceil(finish_time)} сек")

    sys.exit()
    
if __name__ == "__main__":
    main()


# python main.py  ---- запускает работу парсера
 
# python -m venv venv ---- для настройки виртуального окружения
# venv\Scripts\activate ---- второй шаг для настройки вирт окружения, а также если слетело виртуальное окружение. если не помогает - в комбинации с вышеприведенной командой - сперва ту команду, затем эту

# для самой первой настройки виртуального окружения в системе Виндовс:
# - Открываем терминал PowerShell от админа.
# - Вставляем и запускаем - Set-ExecutionPolicy RemoteSigned
# - На вопрос отвечаем - A) 
# выбираем оболочку PowerShell в терминале редактора vs code

# Далее:
# python -m pip install --upgrade pip
# pip install requests_html
# pip install -U pip requests_html
# ... затем устанавл недостоющие библиотеки:
# pip install -r requirements.txt


