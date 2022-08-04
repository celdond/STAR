import requests as r
import json
from bs4 import BeautifulSoup
import parse as p
import re
import time
import sqlite3 as sql3

def steam_database_build():
    u = 'https://store.steampowered.com/search/?sort_by=Released_DESC&ignore_preferences=1'
    
    req = r.Session()
    req_content = req.get(u)
    soup = BeautifulSoup(req_content.text, 'html.parser')
    count_section = soup.find('div', 'search_pagination_left')
    count = p.search("of {} ", count_section.text)
    page = 1
    logged = 0

    steam_database = sql3.connect('steam_database.db')

    while logged < int(count[0]):
        print(page)
        param = {
            'page': page,    
        }
        req_content = req.get(u, params = param)
        page += 1
        soup = BeautifulSoup(req_content.text, 'html.parser')
        
        game_list = soup.find('div', {'id': 'search_resultsRows'}).find_all('a')
        for i in game_list:
            logged += 1

    return

def steam_scrape()->dict:
    u = input("Paste the url of your steam wishlist\n")
    wishlist_data = json.loads(re.findall(r'g_strWishlistBaseURL = (".*?");', r.get(u).text)[0])

    l = r.get(wishlist_data + 'wishlistdata/?p=0').json()
    time.sleep(4)

    index = 1
    while 1:
        to_update = r.get(wishlist_data + 'wishlistdata/?p=' + str(index))
        update = to_update.json()
        if not update:
            break
        l.update(update)
        index += 1
        time.sleep(4)

    print(l)

    return l