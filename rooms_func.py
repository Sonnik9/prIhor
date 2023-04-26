# import main
from bs4 import BeautifulSoup
import re

def page_scraper_roomFather(data_upz_hotels, soup1):
    room_total = []
    roomFather_res = []

    room_total.append(page_scraper_roomSon())
    room_total.append(page_scraper_rooms_blocksSon())
    room_total.append(page_scraper_rooms_highlightsSon())
    return room_total
def page_scraper_roomSon():
    return None
def page_scraper_rooms_blocksSon():
    return None

def page_scraper_rooms_highlightsSon():
    return None