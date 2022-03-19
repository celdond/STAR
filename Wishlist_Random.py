from bs4 import BeautifulSoup
import urllib.request

def main():
    u = input("Paste the url of your steam wishlist\n")
    wishlist = urllib.request.urlopen(u)
    s = "g_rgWishlistData"
    return 1

main()