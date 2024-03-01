import tkinter as tk
import requests
import json


root=tk.Tk()
root.title(u"今日のお天気")
root.geometry('400x300')

def CreateCVS(e):
    URL='https://weather.tsukumijima.net/api/forecast/city/130010'
    data=requests.get(URL).json()
    weather=[[data['forecasts'][0]['telop'],data['forecasts'][0]['temperature']['max']['celsius']]]
    with open('result.csv','w',encoding='utf-8')as file:
        for w in weather:
            file.write(f'{w[0]},{w[1]}\n')

#画像用のキャンバス作成
canvas = tk.Canvas(width=640,height=426)
#キャンバスを設置
canvas.pack()
#画像を用意
photo1 = tk.PhotoImage(file='sky.png')
#画像を描画(中点x,中点y,画像)
canvas.create_image(320,213,image=photo1)
#ボタン
Button = tk.Button(text=u'東京のお天気は？',height =2).place(x=150,y=120)
Button.bind("<ButtonPress>",CreateCVS)
Button.pack()
root.mainloop()
