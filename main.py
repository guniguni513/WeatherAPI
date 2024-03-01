import requests
import json

URL='https://weather.tsukumijima.net/api/forecast/city/130010'
#レスポンスから本文(JSONデータ)を取り出して、パースする
data=requests.get(URL).json()
weather=[[data['forecasts'][0]['telop'],data['forecasts'][0]['temperature']['max']['celsius']]]
#result.csvを開いて（無ければ新規に作成される）書き込む
with open('result.csv','w',encoding='utf-8')as file:
    for w in weather:
        file.write(f'{w[0]},{w[1]}\n')
