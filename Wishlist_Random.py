from bs4 import BeautifulSoup
import urllib.request

def main():
    u = input("Paste the url of your steam wishlist\n")
    wishlist = urllib.request.urlopen(u)
    soup = BeautifulSoup(wishlist, 'html.parser')
    app_ids = soup.find('"appid":')
    print(app_ids)

main()