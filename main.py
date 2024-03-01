import requests
import json

URL='https://weather.tsukumijima.net/api/forecast/city/130010'
data=requests.get(URL).json()
weather=[[data['forecasts'][0]['telop'],data['forecasts'][0]['temperature']['max']['celsius']]]
with open('result.csv','w',encoding='utf-8')as file:
    for w in weather:
        file.write(f'{w[0]},{w[1]}\n')
