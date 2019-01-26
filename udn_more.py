from urllib.request import urlopen
from bs4 import BeautifulSoup

#udn第二頁之後
def udnmore():
    page = 2
    while True:
        url = "https://udn.com/news/get_breaks_article/"+str(page)+"/1/99?_="+str(1547385778401+page)
        print("處理第", page , "頁")
        response = urlopen(url)
        html = BeautifulSoup(response)
        if len(html.text) == 0:
            print("應該爬完了")
            break
        page = page + 1
        for a in html.find_all("dt"):
            category = a.find("a",class_="cate")
            title = a.find("h2")
            times = a.find("div",class_="dt")
            view = a.find("div",class_="view")
            newsurl = a.find("a")
            Nresponse = urlopen("https://udn.com"+newsurl["href"])
            Nhtml = BeautifulSoup(Nresponse)
            print(category.text, times.text, title.text, view.text, "https://udn.com" + newsurl["href"])
            txt = ""
            for content in Nhtml.find("div", id="story_body_content").find_all("p"):
                txt = txt + content.text
            print(txt)

