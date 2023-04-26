# from lxml import etree
# from lxml import html 


# from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get('https://example.com')

# # Рендерим JavaScript
# response.html.render()

# # Ищем все заголовки на странице
# headers = response.html.xpath('//h1/text()')

# print(headers)












# soup22 = BeautifulSoup(r.content, "html.parser")           
# dom = etree.HTML(str(soup22))
# imgBlock2 = dom.xpath('//*[@id="hotel_main_content"]/div/div[1]')
# print(imgBlock2)



# tree = html.fromstring(r.content)
# imgBlock3 = tree.xpath('//*[@id="hotel_main_content"]')[0]
# imgBlock4 = etree.tostring(imgBlock3)
# soup31 = BeautifulSoup(imgBlock4, "lxml")
# links = soup31.find_all('a') 
# print(len(links)) 




            # session = HTMLSession()
            # r = session.get(link, headers=random_headers())
            # print(r.status_code)
            # r.html.render(timeout=21)
            # img_block = r.html.xpath('//*[@id="hotel_main_content"]/div/div[3]/div[2]/div[1]')[0]
            # print(img_block)
            # imgBlock4 = etree.tostring(img_block)
            # soup31 = BeautifulSoup(imgBlock4, "lxml")
            # links = soup31.find_all('a') 
            # print(len(links))



            # session = HTMLSession()
            # r = session.get(link, headers=random_headers())
            # print(r.status_code)
            # r.html.render(timeout=21)
            # img_block = r.html.xpath('//*[@id="hotel_main_content"]/div/div[3]/div[2]/div[1]')[0]
            # links = img_block.xpath('.//a')
            # print(len(links))
            # for link in links:
            #     print(link.attrs['href']) 

            # session = HTMLSession()
            # r = session.get(link, headers=random_headers())
            # print(r.status_code)
            # r.html.render(timeout=21)
            # img_block = r.html.xpath('//*[@id="hotel_main_content"]/div/div[3]/div[2]/div[1]')[0]
            # print(img_block)
            # img_block_html = img_block.html  # get HTML content as string
            # print(img_block_html)
            # soup = BeautifulSoup(img_block_html, "lxml")
            # links = soup.find_all('a')
            # print(len(links))


            # session = HTMLSession()
            # r = session.get(link, headers=random_headers())
            # print(r.status_code)
            # r.html.render(timeout=21)


        # from requests_html import HTMLSession

        # # Create a new session
        #     session = HTMLSession()

        #     # Send a GET request to the URL
        #     r = session.get(link, headers=random_headers())
        #     print(r)

        #     # Render the JavaScript on the page
        #     r.html.render(timeout=21)

        #     # Get the HTML code of the rendered page
        #     html = r.html.html

            # Save the HTML code to a file
            # with open("rendered_page2.html", "w") as f:
            #     f.write(html)




            # with open("file2.txt", "w") as file:
            #     file.write(str(r.text))
            # r.html.render(timeout=21)
            # img_block = r.html.xpath('//*[@id="hotel_main_content"]/div/div[3]/div[2]/div[1]')[0]
            # print(img_block)
            # imgBlock4 = etree.tostring(img_block)
            # print(imgBlock4)
            # soup31 = BeautifulSoup(imgBlock4, "lxml")
            # links = soup31.find_all('a') 
            # print(len(links)) 





            # https://www.booking.com/hotel/cg/pefaco-maya-maya.ru.html?hapos=1&req_adults=2&group_adults=2&room1=A%2CA&hpos=1&aid=304142&ucfs=1&sr_order=popularity&req_children=0&srpvid=9d007762ad3501d6&sid=52c12d695260d02d8a98fb123e5b9e1e&activeTab=photosGallery&dist=0&label=gen173nr-1FCBcoggI46AdIM1gEaOkBiAEBmAEhuAEHyAEN2AEB6AEB-AECiAIBqAIDuALEmPuhBsACAdICJDdlOGUzNzdlLWYyYmMtNDkxMi05NjYyLWNjNmZhZmIyZGExYtgCBeACAQ&type=total&no_rooms=1&sb_price_type=total&group_children=0&srepoch=1681837125 

 

            # tree = html.fromstring(r.content)
            # imgBlock1 = tree.xpath('//*[@id="hotel_main_content"]')[0]
            # imgBlock4 = etree.tostring(imgBlock1)
            # soup41 = BeautifulSoup(imgBlock4, "lxml")
            # links = soup41.find_all('a') 
            # print(len(links))







            # print(f"str 129________ {imgBlock2}")

            # Рендерим JavaScript
            # response.html.render()

            # Ищем все заголовки на странице
            # headers = response.html.xpath('//h1/text()')

            # print(headers)



            # r = requests.get(link, headers=random_headers(), timeout=(9.15, 30.15))
            # print(r)
            # //*[@id="hotel_main_content"]/div/div[1]
            # imgBlock = soup2.find('div', attrs={'class': 'gallery-side-reviews-wrapper'})
            # imgBlock = dom.xpath('//*[@id="hotel_main_content"]/div/div[1]/div[3]//text()')
            # print(imgBlock)
            # reviewFloater 






# import re 
# # str_element = ''
# str_element = 'Парам особенно нравится расположение — они оценили проживание в этом районе для поездки вдвоем на <strong>9,3</strong>.'
# clean_str = re.sub(r'<.*?>', '', str_element)
# print(clean_str)

def handler_manager(arg):
    sum  = []
    sum.append(arg)
    return sum


def testt():
    from mpire import WorkerPool 

    total = []
    scraping_result = [1,2,3,4,45,56]

    finResArr = []

    # print(scraping_result)
    data_upz_hotels = ['1sff',True,3,4,45,587656]
    vpnFraction = len(data_upz_hotels)
    # print(data_upz_hotels)
    n = 21
    for i in range(0, len(data_upz_hotels), vpnFraction):        
        n1 = i 
        n2 = i+vpnFraction
        if n2 > len(data_upz_hotels):
           n2 = len(data_upz_hotels)
        # if n2 != len(data_upz_hotels) and i != 0:  
        #     yellowInput = input('Пожалуйста смените VPN', )
        #     if yellowInput:
        #         pass
        with WorkerPool(n_jobs = n) as p2:                      
            finRes = p2.map(handler_manager, data_upz_hotels[n1:n2])
            finResArr.append(finRes)           
            # time.sleep(random.randrange(63,79))            
    for item in finResArr:
        total +=item

    print(f"208 str____{total}")  



    # return print([scraping_result, data_upz_hotels])

testt() 

# python test1.py