import urllib.request
import urllib.parse
import sys
from bs4 import BeautifulSoup

def crawling():
    with open('source.txt', 'r', encoding='utf8') as f:
        date = f.read()  # 메모장을 불러오는 기능

    plusUrl = urllib.parse.quote_plus(date)

    pageNum = 1
    count = 1

    i = 1  # 1페이지로 고정

    sys.stdout = open('output.txt', 'a', encoding='UTF-8') # 메모장에 출력해주는 기능

    lastPage = int(i) * 10 - 9
    while pageNum < lastPage + 1:
        url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}' 
        # 네이버는 위의 URL을 기본으로 찾는 검색어의 HTML값을 더해준다.
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')  # HTML로 변환

        title = soup.find_all(class_='sh_blog_title')

        print(f'-----{plusUrl}의 {count}페이지 결과 입니다.-----')
        for i in title:
            print(i.attrs['title'])
            print(i.attrs['href'])

        print()

        pageNum += 10
        count += 1


crawling()
