import requests
import json

URL='https://weather.tsukumijima.net/api/forecast/city/130010'
#通信をしてレスポンスを取得
res = requests.get(URL)
#レスポンスから本文(JSONデータ)を取り出して、パースする
data=json.loads(res.text)
#デバッグプリント
print(data)
