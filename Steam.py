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
    cur_steam = steam_database.cursor()

    cur_steam.execute( " CREATE TABLE IF NOT EXISTS status (latest text(255) PRIMARY KEY, latest_id int); ")
    param = {
            'page': page,    
        }
    req_content = req.get(u, params = param)
    soup = BeautifulSoup(req_content.text, 'html.parser')
    game_list = soup.find('div', {'id': 'search_resultsRows'}).find_all('a')
    game_id = game_list[0]["data-ds-appid"]
    
    cur_steam.execute( " INSERT INTO status(latest, latest_id) SELECT ?, ?", ("latest", game_id,))
    cur_steam.execute( " CREATE TABLE IF NOT EXISTS steam_store (app_id int PRIMARY KEY, name text(255), price real); ")

    while logged < int(count[0]):
        price = 0
        for i in game_list:
            game_id = i["data-ds-appid"]
            game_name = i.find('div', 'col search_name ellipsis').text.strip().replace('\n', ' ')

            try: 
                game_price = i.find('div', 'col search_price responsive_secondrow').text.strip()
            except Exception:
                game_price = i.find('span', {'style': 'color: #888888;'}).text
            if '$' in game_price:
                price = float(game_price.replace('$', ''))
            else:
                price = 0
            try:
                cur_steam.execute("INSERT INTO steam_store(app_id, name, price) SELECT ?, ?, ?", (int(game_id), game_name, price))
                logged += 1
                print(game_name)
            except Exception:
                pass
        param = {
            'page': page,    
        }
        req_content = req.get(u, params = param)
        page += 1
        soup = BeautifulSoup(req_content.text, 'html.parser')
        game_list = soup.find('div', {'id': 'search_resultsRows'}).find_all('a')

    return

def steam_database_update():
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