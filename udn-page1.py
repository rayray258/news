#udn新聞第一頁
from urllib.request import urlopen
from bs4 import BeautifulSoup
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
        Nresponse = urlopen("https://udn.com"+newsurl["href"])
        Nhtml = BeautifulSoup(Nresponse)
        print(category.text, times.text, title.text, view.text, "https://udn.com" + newsurl["href"])
        for content in Nhtml.find_all("p"):
            print(content.text)
    except TypeError:
        pass
    continue