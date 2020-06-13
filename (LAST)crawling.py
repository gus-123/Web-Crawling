# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import sys
from bs4 import BeautifulSoup
import codecs
# baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
# plusUrl = input('검색어를 입력하세요:')
# url = baseUrl + urllib.parse.quote_plus(plusUrl)
#
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# title = soup.find_all(class_='sh_blog_title')
#
# for i in title:
#     print(i.attrs['title'])
#     print(i.attrs['href'])
#     print()

plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요:'))

pageNum = 1
count = 1

i = input('몇페이지를 크롤링 할까요? : ')

file_name = "크롤링.txt"
sys.stdout = open(file_name, "w", encoding="utf-8")


lastPage = int(i) * 10 - 9
while pageNum < lastPage + 1:
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusUrl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pageNum}'

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find_all(class_='sh_blog_title')

    print(f'-----{plusUrl}의 {count}페이지 결과 입니다.-----')
    for i in title:
        print(i.attrs['title'])
        print(i.attrs['href'])

    print()

    pageNum += 10
    count +=1
