import requests
import json
from bs4 import BeautifulSoup
from urllib import parse


def keyword_search(keyword, page_count):

    naver_news_links = []
    i = 0
    j = 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    while True:
        r = requests.get(
            "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + parse.quote(keyword) + "&start= " + str(j),
            headers=headers)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        news_list = soup.find_all("a",{"class":"_sp_each_url"})

        for news_link in news_list:
            if news_link.text == "네이버뉴스":
                naver_news_links.append(news_link['href'])
                i = i + 1
                if i == int(page_count):
                    return naver_news_links
        j = j * 10


def get_comments(news_link, user_comment_count):

    comment_count = 0
    comment_list = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'referer': 'http://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=001&aid=0009572260&isYeonhapFlash=Y&rc=N&m_view=1&includeAllCount=true&m_url=%2Fcomment%2Fall.nhn%3FserviceId%3Dnews%26gno%3Dnews001%2C0009572260%26sort%3Dlikability'
    }

    aid = news_link.split("aid=")[1]
    oid = news_link.split("oid=")[1].split("&")[0]

    page = 1
    while True:
        r = requests.get(
            "https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_politics&pool=cbox5&_callback=jQuery17023240944630416482_1506390886908&lang=ko&country=&objectId=news" + oid + "%2C" + aid + "&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&page=" + str(page) + "&sort=FAVORITE&current=1079250985&prev=1079229065&includeAllStatus=true&_=1506390900990",
            headers=headers)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        c_count = int(int(str(soup).split('{"comment":')[1].split(",")[0])/20)

        contents = str(soup).split('"contents":"')
        for i in range(0, len(contents)):
            comment_content = contents[i].split('","userIdNo"')[0]
            comment_count = comment_count + 1

            comment_list.append(comment_content)
            if user_comment_count == comment_count:
                return comment_list

        if c_count < 1 or c_count == page:
            break
        else:
            page = page + 1


if __name__ == '__main__':
    keyword = input("키워드를 입력해주세요 : ")
    news = input("크롤링해올 뉴스 갯수를 입력해주세요 : ")
    comments = input("크롤링해올 덧글 갯수를 입력해주세요 : ")
    news_links = keyword_search(keyword,news)
    for news_link in news_links:
        get_comments(news_link, comments)