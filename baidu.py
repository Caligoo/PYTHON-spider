#!/usr/bin/python2.7
#-*- coding: UTF-8 -*-
import requests

data = requests.get('https://www.baidu.com/')
data.encoding='utf-8'

print(data.text)

