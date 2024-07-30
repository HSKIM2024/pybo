#BEAUTIFULSOUP.py
from bs4 import BeautifulSoup
import requests

#웹페이지 가져오기
response = requests.get("http://localhost:8000/pybo")
data = response.text

#BeautifulSoup 객체생성
soup = BeautifulSoup(data,"html.parser")

#타이틀태그찾기
title = soup.find("title")
print("Page Title:","게시판[BOARD]")

#모든 하이퍼링크찾기
for link in soup.find_all("a"):
    print("Hyperlink:",link.get("href"))

