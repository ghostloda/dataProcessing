#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import random
import pymongo
import requests
from bs4 import BeautifulSoup

# 注意不要写错localhost
client = pymongo.MongoClient('localhost', 27017)
# 注意不要把中括号写成了小括号
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
    'Connection':'keep-alive'
}

# http://cn-proxy.com/
proxy_list = [
    #'http://120.25.105.45:81',
    #'http://218.75.100.114:8080',
    'http://60.194.100.51:80',
    #'http://221.8.9.6:80',

    ]
# 随机获取代理ip
proxy_ip = random.choice(proxy_list) 
proxies = {'http': proxy_ip}

# 获取所有的列表页面链接
def get_links_from(channel, page, who_sell='o'):
    # http://nj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    url = '{}{}{}/'.format(channel, who_sell, page)
    wb_data = requests.get(url, headers=headers,)
    time.sleep(2)
    # 检查页面是否不存在，或者被封ip

    if wb_data.status_code == 200:

        soup = BeautifulSoup(wb_data.text,'lxml')
        #if soup.find('ul','pageLink'): 用来判断是不是最后一页
        if soup.find('td','t')  :

            links = soup.select('td.t > a')
            for link in links:
                link_data=link.get('href').split('?')[0]
                url_list.insert_one({'url':link_data})
                print link_data

        else:
            pass

# 获取指定链接页面详细信息
def get_item_info_from(url, data=None):
    wb_data = requests.get(url, headers=headers,proxies=proxies)
    # 检查页面是否不存在，或者被封ip
    if wb_data.status_code != 200:
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')

        prices = soup.select('div.content  div.price_li > span > i')
        #pub_dates = soup.select('.pr-5')
        areas = soup.select(' div.content  div.palce_li > span > i')
        #cates = soup.select('ul.det-infor > li:nth-of-type(1) > span')

        data = {
            'title': soup.title.text.strip(),
            'price': prices[0].text.strip() if len(prices) > 0 else 0,
            #'pub_date': pub_dates[0].text.strip().split(' ')[0] if len(pub_dates) > 0 else "",
            'area': [area.text.strip() for area in areas if area.text.strip() != "-"],
            #'cates': cates ,#[cates.text.strip() for cate in cates],
            'url':url
        }
        print repr(data).decode("unicode–escape")
        item_info.insert_one(data)
#get_links_from("http://nj.ganji.com/jiaju/",6,)
get_item_info_from("http://zhuanzhuan.ganji.com/detail/799056619115692034z.shtml")
