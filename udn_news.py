import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

url = "https://udn.com/news/breaknews/1/99#breaknews"
response = urlopen(url)
html = BeautifulSoup(response)
for a in html.find("div",id="breaknews_body").find_all("dt"):
    category = a.find("a",class_="cate")
    title = a.find("h2")
    times = a.find("div",class_="dt")
    view = a.find("div",class_="view")
    newsurl = a.find("a")
    try:
        Nurl = "https://udn.com"+newsurl["href"]
        Nresponse = urlopen(Nurl)
        Nhtml = BeautifulSoup(Nresponse)
        print(category.text, times.text, title.text, view.text, Nurl)

        #內文
        content_txt = ""
        for content in Nhtml.find("div", id="story_body_content").find_all("p"):
            content_txt = content_txt + content.text
        print(content_txt)


        time.sleep(1)
    except TypeError :
        pass
    continue

from udn_more import udnmore
udnmore()

