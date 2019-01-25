from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://news.ltn.com.tw/list/breakingnews/sports/1"
response = urlopen(url)
html = BeautifulSoup(response)
# print(html)
for a in html.find("ul",class_="list imm").find_all("li"):
    try:
        title = a.find("p")
        time = a.find("span")
        newsurl = a.find("a",class_="tit")
        print(time.text,title.text,"https:" + newsurl["href"])
        response = urlopen("https:" + newsurl["href"])
        html = BeautifulSoup(response)
        txt=""
        for content in html.find("div",class_="news_p").find_all("p"):
            if content.text =="還想看更多新聞嗎？歡迎下載自由時報APP，現在看新聞還能抽獎，共7萬個中獎機會等著你：":
                break
            txt = txt+content.text
        print(txt)
    except AttributeError:
        pass
    continue

