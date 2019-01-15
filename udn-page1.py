#udn新聞第一頁
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame(columns=["category","times","title","view","URL","content"])
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
        txt = ""
        for content in Nhtml.find("div", id="story_body_content").find_all("p"):
            txt = txt + content.text
            print(content.text)

        s = pd.Series([category.text, times.text, title.text, view.text, "https://udn.com" + newsurl["href"], txt],
                    index=["category","times","title","view","URL","content"])
        df = df.append(s, ignore_index=True)
    except TypeError:
        pass
    continue
df.to_csv("news.csv", encoding="utf-8", index=False)