import requests
from bs4 import BeautifulSoup
from urllib import parse
import nltk
from konlpy.tag import Twitter
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="/Library/Fonts/AppleGothic.ttf").get_name()
rc('font', family=font_name)
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def get_comments(news_link, comment_count, comments):
    print("a")

def keyword_search(keywrod, page_count):
    naver_news_links = []

    i=0
    j=1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    while True:

        r = requests.get('https://search.naver.com/search.naver?ie=utf8&where=news&query=' + parse.quote(keyword) + '&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=19&start=' + str(j) + '&refresh_start=0',headers=headers)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")

        news_list = soup.find_all('a',{"class":"_sp_each_url"})
        for n in news_list:
            if n.text == "네이버뉴스":
                naver_news_links.append(n['href'])
                i = i + 1
                if i == int(page_count):
                    return naver_news_links

        j = j + 10



if __name__ == '__main__':

    keyword = input("$ 키워드를 입력해주세요 : ")
    news = input("$ 크롤링해올 뉴스의 갯수를 입력해주세요 : ")
    comments = input("$ 크롤링해올 덧글의 갯수를 입력주세요 : ")

    news_links = keyword_search(keyword, news)
    print(news_links)
    print(len(news_links))


    comment_count = 0 # 누적된 크롤링한 덧글의 수
    comment_list = []


    # for news_link in news_links:
    #     l, flag = get_comments(news_link, comment_count, comments)
    #     comment_list.extend(l)
    #     comment_count = int(comment_count + len(l))
    #
    #     if flag is True:
    #         break
    #
    # analzye(comment_list, keyword)







