# 引用相關套件
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time, os

# <!-- For MAC電腦
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# -->

if __name__ == "__main__":
    # 紀錄爬蟲開始時間
    start_time = time.time()

    update_url_list = [] # 紀錄爬回來的各篇新聞網址
    count = 0 # 紀錄爬了幾筆
    page = 1 # 新聞第一頁開始
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
                    # 不紀錄重複的新聞網址
                    if not news_url in update_url_list:
                        update_url_list.append(news_url)
                    count = count + 1
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
                print("應該爬完了")
                break
            for page_news in page_html.find_all("dt"):
                news_url = page_news.find("a")["href"]
                news_url = "https://udn.com" + news_url
                # 不紀錄重複的新聞網址
                if not news_url in update_url_list:
                    update_url_list.append(news_url)
                count = count + 1
        page = page + 1

        # 紀錄爬蟲結束時間
    end_time = time.time()
    print('Get url done, Time cost: %s ' % (end_time - start_time))

    # 紀錄存檔開始時間
    start_time = time.time()

    old_url_list = []  # 紀錄之前爬過的新聞網址
    # 開啟紀錄全部新聞網址的檔案
    if os.path.exists("udn_news_url.txt"):
        with open("udn_news_url.txt", "r", encoding="utf-8") as f:
            old_url_list = f.read().split("\n")
            old_url_list.remove("")

    url_list = []  # 紀錄更新的新聞網址
    # 不記錄重複的新聞網址
    for url in update_url_list:
        if not url in old_url_list:
            url_list.append(url)
    # print(len(url_list))

    ## 如果檔案存在
    if os.path.exists("update_udn_news_url.txt"):
        old_update_url_list = []  # 紀錄之前更新但還沒爬新聞內容的新聞網址
        new_update_url_list = []  # 紀錄此次更新的新聞網址
        new_update_url_list = url_list
        # 開啟之前紀錄更新的新聞網址的檔案
        with open("update_udn_news_url.txt", "r", encoding="utf-8") as f:
            old_update_url_list = f.read().split("\n")
            old_update_url_list.remove("")
            # print(len(old_update_url_list))
            # 將此次更新的新聞網址跟之前更新但還沒爬新聞內容的新聞網址合併
            new_update_url_list.extend(old_update_url_list)
            # print(len(new_update_url_list))
        # 將更新的新聞網址存檔
        with open("update_udn_news_url.txt", "w", encoding="utf-8") as f:
            for url in new_update_url_list:
                f.write(str(url) + "\n")
    ## 如果檔案不存在
    else:
        # 將更新的新聞網址存檔
        with open("update_udn_news_url.txt", "w", encoding="utf-8") as f:
            for url in url_list:
                f.write(str(url)+ "\n")

    # 將更新的新聞網址跟之前紀錄的新聞網址合併
    url_list.extend(old_url_list)
    # 將全部新聞網址存檔
    with open("udn_news_url.txt", "w", encoding="utf-8") as f:
        for url in url_list:
            f.write(str(url) + "\n")

    # 紀錄存檔結束時間
    end_time = time.time()
    print('Save url file done, Time cost: %s ' % (end_time - start_time))

    # 檢查用
    # print(len(update_url_list))
    # print(len(old_url_list))
    # print(len(url_list))
    # print(count)