# 引用相關套件

from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading, queue, time, datetime, os, json



if __name__ == "__main__":
    # 紀錄爬蟲開始時間
    start_time = time.time()

    update_url_list = [] # 紀錄爬回來的各篇新聞網址
    page = 1 # 新聞第一頁開始
    view_list = []
    ## 開始爬蟲
    while True:
        if page ==1:
            url = "https://udn.com/news/breaknews/1/99#breaknews"
            print("處理頁面：", url)
            page_response = urlopen(url)
            page_html = BeautifulSoup(page_response)
            for page_news in page_html.find("div", id="breaknews_body").find_all("dt"):
                try:
                    news_url = page_news.find("a")["href"]
                    news_url ="https://udn.com"+news_url
                    news_view = page_news.find("div",class_="view")
                    view_list.append  ({"news_link": news_url,
                                        "view": news_view.text,
                                        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})

                    # 不紀錄重複的新聞網址
                    # if not news_url in update_url_list:
                    #     update_url_list.append(news_url)
                except TypeError:
                    pass
                continue
        else :
            url = "https://udn.com/news/get_breaks_article/" + str(page) + "/1/99?_=" + str(1547385778401 + page)
            print("處理頁面：", url)
            page_response = urlopen(url)
            page_html = BeautifulSoup(page_response)
            # 結束爬蟲
            if len(page_html.text) == 0:
                print("爬完了")
                break
            for page_news in page_html.find_all("dt"):
                news_url = page_news.find("a")["href"]
                news_url = "https://udn.com" + news_url
                news_view = page_news.find("div",class_="view")
                view_list.append  ({"news_link": news_url,
                                    "view": news_view.text,
                                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})

        page = page +1


    date_list = []  # 紀錄爬取觀看數的日期
    count = 0  # 紀錄爬了幾筆
        ## 不紀錄重複的爬取觀看數的日期
    for view in view_list:
        # print(view)
        if not view["time"].split(" ")[0] in date_list:
            date_list.append(view["time"].split(" ")[0])
        count = count + 1


    ## 將每筆觀看數依照爬取日期分類
    for date in date_list:
        date_view_list = []  # 紀錄分類過的新聞觀看數
        for view in view_list:
            if view["time"].split(" ")[0] == date:
                date_view_list.append(view)
        view_dict = {"date": date, "views": date_view_list}
        ## 如果檔案存在
        if os.path.exists(date + "_udn_news_view.json"):
            # 開啟之前紀錄新聞觀看數的檔案
            with open(date + "_udn_news_view.json", "r", encoding="utf-8") as f:
                file_content = json.load(f)
            # 將依照爬取日期分類的新聞觀看數存檔
            with open(date + "_udn_news_view.json", "w", encoding="utf-8") as f:
                # 將每筆新的新聞觀看數加入之前的紀錄
                for view in date_view_list:
                    file_content["views"].append(view)
                json.dump(file_content, f)
        ## 如果檔案不存在
        else:
            # 將依照爬取日期分類的新聞觀看數存檔
            with open(date + "_udn_news_view.json", "w", encoding="utf-8") as f:
                json.dump(view_dict, f)

    end_time = time.time()
    print("花了多久:%s" % (end_time - start_time))
    #
    # # 紀錄存檔結束時間
    # end_time = time.time()
    # print('Done, Time cost: %s ' % (end_time - start_time))
