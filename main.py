import requests
import json
#Weatherクラス
class Weather:
    #コンストラクタ
    def __init__(self,telop,celsius):
        self.telop=telop
        self.celsius=celsius
    #予報をCSV文字列にするメソッド
    def toCSV(self):
        return f'{self.telop},{self.celsius}'

URL='https://weather.tsukumijima.net/api/forecast/city/130010'
#通信をしてレスポンスを取得
res = requests.get(URL)
#レスポンスから本文(JSONデータ)を取り出して、パースする
data=json.loads(res.text)
#デバッグプリント
#print(data)

#リスト作成
weather=[]
#天気と最高気温を取り出してWeatherオブジェクトを作成し、リストに追加
weather.append(Weather(data['forecasts'][0]['telop'],data['forecasts'][0]['temperature']['max']['celsius']))
#デバッグプリント
print(weather[0].toCSV())

#result.csvを開いて（無ければ新規に作成される）書き込む
with open('result.csv','w',encoding='utf-8')as file:
    for w in weather:
        file.write(w.toCSV()+'\n')
