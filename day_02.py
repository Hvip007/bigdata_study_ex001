# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:47:37 2018

@author: lenovo
"""
import urllib.request as r
import json
from xpinyin import Pinyin
from prettytable import PrettyTable 


p= Pinyin()
while 1:
    print("欢迎使用全球天气，1.查看当天天气情况，2.查看未来5天天气情况，3.退出本系统")
    n = input("请输入你的选择：")
    if n == '1':
        city = input("请输入城市:")
        city_pinyin = p.get_pinyin(city,'')
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
        print('-------------------------------------------')
    if n == "2":
        url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
        city = input("请输入城市:")
        city_pinyin = p.get_pinyin(city,'')
        info = r.urlopen(url.format(city_pinyin)).read().decode('utf-8','ignore')
        table = PrettyTable(["时间", "温度", "最高温度","最低温度","天气",'气压'])
        for i in range(38):
            w = json.loads(info)
            time = w['list'][i]['dt_txt']
            temp = w['list'][i]['main']['temp']
            temp_max =  w['list'][i]['main']['temp_max']
            temp_min =  w['list'][i]['main']['temp_min']
            weather =  w['list'][i]['weather'][0]['description']
            pressure = w['list'][i]['main']['pressure'] 
            table.add_row([time,temp, temp_max,temp_min,weather,pressure])
        print(table)
    if n =='3':
        print('再见，欢迎再次使用本系统！')
        break