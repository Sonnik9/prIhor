import asyncio
import photos_func, description_func, faciclities_func, rooms_func, rooms_block_func



def scraper_grendmather(resHtml, hotelid, photoInd, descriptionInd, facilityInd, roomInd):
    flagTest = True
    result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks = '', '', '', '', ''
    # resHtml, hotelid = resHtml, hotelid
    # print('hello')

    async def mather_controller_two(resHtml, hotelid):
        nonlocal flagTest, result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks
        tasks = [
            asyncio.create_task(async_page_scraper_photos(resHtml, hotelid)),
            asyncio.create_task(async_page_scraper_description(resHtml, hotelid)), 
            asyncio.create_task(async_page_scraper_facilities(resHtml, hotelid)),
            asyncio.create_task(async_page_scraper_room(resHtml, hotelid)),
            asyncio.create_task(async_page_scraper_room_block(resHtml, hotelid))
        ]        
        await asyncio.gather(*tasks)

    async def async_page_scraper_photos(resHtml, hotelid):
        nonlocal result_photos_upz        
        # print(resHtml)
        # if (photoInd != "1" and photoInd != 1) or flagTest == True:
        try:
            result_photos_upz = photos_func.page_scraper_photos(resHtml, hotelid)
        except:
            result_photos_upz = None  

    async def async_page_scraper_description(resHtml, hotelid):
        nonlocal result_description_upz
        # if (descriptionInd != "1" and descriptionInd != 1) or flagTest == True:
        try:
            result_description_upz = description_func.page_scraper_description(resHtml, hotelid)
        except:
            result_description_upz = None 

        # return result_description_upz
    async def async_page_scraper_facilities(resHtml, hotelid):
        nonlocal result_facilities_upz
        # if (facilityInd != "1" and facilityInd != 1) or flagTest == True:
        try:
            result_facilities_upz = faciclities_func.page_scraper_facilities(resHtml, hotelid)
        except:
            result_facilities_upz = None
    async def async_page_scraper_room(resHtml, hotelid):
        nonlocal result_rooms_upz
        # if (roomInd != "1" and roomInd != 1) or flagTest == True:
        try:
            result_rooms_upz = rooms_func.page_scraper_room(resHtml, hotelid)
        except:
            result_rooms_upz = None 
    async def async_page_scraper_room_block(resHtml, hotelid):
        nonlocal upz_hotels_rooms_blocks

        try:
            upz_hotels_rooms_blocks = rooms_block_func.page_scraper_room_block(resHtml, hotelid)
        except:
            upz_hotels_rooms_blocks = None

    asyncio.run(mather_controller_two(resHtml, hotelid))

    return result_photos_upz, result_description_upz, result_facilities_upz, result_rooms_upz, upz_hotels_rooms_blocks
