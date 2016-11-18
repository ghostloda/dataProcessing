#!/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# url_ganji = 'http://nj.ganji.com/wu'
# url_host = 'http://nj.ganji.com'
# web_data = requests.get(url_ganji)
# soup = BeautifulSoup(web_data.text,'lxml')
# channel_urls = soup.select('#wrapper > div.content > div > div > dl > dt > a')
# for url in channel_urls:
#     urls=url_host+url.get('href')
#     print urls

channel_list = [
    "http://nj.ganji.com/jiaju/",
    "http://nj.ganji.com/rirongbaihuo/",
    "http://nj.ganji.com/shouji/",
    "http://nj.ganji.com/nongyongpin/",
    "http://nj.ganji.com/jiadian/",
    "http://nj.ganji.com/ershoubijibendiannao/",
    "http://nj.ganji.com/ruanjiantushu/",
    "http://nj.ganji.com/yingyouyunfu/",
    "http://nj.ganji.com/diannao/",
    "http://nj.ganji.com/xianzhilipin/",
    "http://nj.ganji.com/fushixiaobaxuemao/",
    "http://nj.ganji.com/meironghuazhuang/",
    "http://nj.ganji.com/shuma/",
    "http://nj.ganji.com/laonianyongpin/",
    "http://nj.ganji.com/xuniwupin/",

    ]
