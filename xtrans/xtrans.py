#!/bin/python3
# -*- coding: UTF-8 -*-

#=============================================
#author:unihon
#describe:an en to zh and zh to en translater
#version:1
#update:2018-08-19
#---
#blog:https://unihon.github.io
#github:https://github.com/unihon
#E-mail:unihon@outlook.com
#=============================================

import requests
import json

def trans():
    userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    
    header = {
            "Host": "fanyi.baidu.com",
            "Origin": "http://fanyi.baidu.com",
            "User-Agent": userAgent
            }

    postUrl="http://fanyi.baidu.com/basetrans"

    wd = input("please input a word: ")
    print('-------------------------------')
    if wd == '':
        trans()
        return
    
    for c in wd:
        if c < u'\u4e00' or c > u'\u9fa5':
            print('[en to zh]\n')
            mdata = {
                    "from":"en",
                    "to":"zh",
                    "query" : wd
                    }
            break
        elif c == wd[-1]:
            print('[zh to en]\n')
            mdata = {
                    "from":"zh",
                    "to":"en",
                    "query" : wd
                    }
    try:
        response = requests.post(postUrl, data = mdata, headers = header)
    except:
        print('connect error!')
        return 1

    result = response.text
    result=json.loads(result)
    
    if len(result["dict"]) == 0:
        print('is null')
    else:
        try:
            for i in result["dict"]["word_means"]:
                print('> '+ i)
        except KeyError:
            print('key is null')

if __name__ == "__main__":
    print("===============================")
    trans()
    print("===============================")
