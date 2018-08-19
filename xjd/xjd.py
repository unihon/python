#!/bin/python3
# -*- coding: UTF-8 -*-

#=============================================
#author:unihon
#describe:use to tracking the price on jd.com
#version:1
#update:2018-08-19
#---
#blog:https://unihon.github.io
#github:https://github.com/unihon
#E-mail:unihon@outlook.com
#=============================================

import requests
import json
import re
import time
import os

def fun():
    userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

    #商品id
    itemId = '7234518'

    postUrl="http://item.jd.com/"+itemId+".html"
    priceUrl="http://p.3.cn/prices/mgets?skuIds=J_"+itemId

    header = {
    "User-Agent": "userAgent"
    }
    
    resName = requests.get( postUrl , headers = header)
    resPrice = requests.get( priceUrl , headers = header)

    htName = resName.text

    #正则匹配商品名称
    reName = re.search('"sku-name">(.*?)</',htName,re.S) 

    try:
        name = reName.group(1).strip()
    except AttributeError:
        print("no have this item")
        return

    htPrice = json.loads(resPrice.text)
    price = str(htPrice[0]['p'])

    itime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    print('[time]\n')
    print(itime)
    print('-------------------------------')
    print('[name]\n')
    print(name)
    print('-------------------------------')
    print('[price]\n')
    
    #判断是否有货，无货时，价格小于0（一般为-1）
    if float(price) >= 0:
        print(price)
    else:
        print("no stock")
    print('-------------------------------')

    #文件名
    fileN = 'itemId_'+itemId+'.txt'

    #读取最近一次价格
    lastP = os.popen("[ -f %s ] && tail -n 1 %s|cut -d, -f1"%(fileN,fileN)).read()

    #与上一次记录的价格比较，自定义事件
    if lastP == price+'\n':
        print('is same')
    elif lastP != '':
        print('is change')

    #将价格,日期写入文件
    with open(fileN,'a+') as f:
     f.write(price+','+itime+'\n')

if __name__ == "__main__":
    print("===============================")
    fun()
    print("===============================")
