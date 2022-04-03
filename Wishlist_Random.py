import requests as r
import parse as p

def main():
    u = input("Paste the url of your steam wishlist\n")
    wishlist = r.get(u)
    l = list(p.findall('"appid":{appid},', wishlist.text))
    print(l)

main()