# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:36:09 2018

@author: lenovo
"""
import urllib.request as r
import json


print("欢迎使用全球天气，1.查看当前城市天气，2.查看其城市，3.保存当前城市")
n = input("请输入菜单：")
if n == '1':
    city_pinyin = input("请输入城市拼音:")
    address = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    info = r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    #print(info)
    data = json.loads(info)
    temp = data["main"]["temp"]
    temp_max = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]
    print("温度："+str(temp))
    print("最高温度："+str(temp_max))
    print("天气："+weather)
    print("气压："+str(pressure))
if n == "2":
    print("2.查看其城市")
if n == "3":
    print("3.保存当前城市")



