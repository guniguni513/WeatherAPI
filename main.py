import requests
import json
#Weatherクラス
class Weather:
    #コンストラクタ
    def __init__(self,telop):
        self.telop=telop
    #予報をCSV文字列にするメソッド
    def toCSV(self):
        return f'{self.telop}'

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
weather.append(Weather(data['forecasts'][0]['telop']))
#デバッグプリント
print(weather[0].toCSV())
