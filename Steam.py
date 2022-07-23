import requests as r
import json
from bs4 import BeautifulSoup
import re
import time

def steam_database_build()->dict:
    u = 'https://store.steampowered.com/search/?sort_by=Released_DESC&ignore_preferences=1'
    req = r.get(u)
    soup = BeautifulSoup(req.text, 'html.parser')
    count = soup.find('div', 'search_pagination_left')
    
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

    return l