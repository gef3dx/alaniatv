import requests
from bs4 import BeautifulSoup
import requests

url_alania = 'https://alaniatv.ru/novosti/'

header = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
    }

def imgSave(src):
    img = requests.get(src)
    imgname = src.split('/')[7]
    out = open(f"C:\\Users\\PC4\\Desktop\\pars\\{imgname}.jpg", "wb")
    out.write(img.content)
    out.close()
    return True

main = requests.get(url_alania, headers=header)

html_main = main.text

soup = BeautifulSoup(html_main, "lxml")
url = soup.find("div", class_="news-list-item").find("a").get("href")
title = soup.find("div", class_="news-list-item").find("img").get("alt")

main = requests.get(url, headers=header)

html_news = main.text

soup = BeautifulSoup(html_news, "lxml")
img = soup.find("div", class_="content").find("img").get("src")
post = soup.find("div", class_="content").find_all("p")

imgSave(img)

print(post)
