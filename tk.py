import tkinter as tk
import requests
import json
import csv


root=tk.Tk()
root.title(u"今日のお天気")
root.geometry('400x300')
root.resizable(width=False,height=False)

def CreateCVS():
    URL='https://weather.tsukumijima.net/api/forecast/city/130010'
    data=requests.get(URL).json()
    weather=[[data['forecasts'][0]['telop'],data['forecasts'][0]['temperature']['max']['celsius'],data['forecasts'][0]['temperature']['min']['celsius']]]
    with open('result.csv','w',encoding='utf-8')as file:
        for w in weather:
            file.write(f'{w[0]},{w[1]},{w[2]}\n')

def showinfo():
    filename = 'result.csv'
    with open(filename,encoding='utf8',newline='')as f:
        csvreader = csv.reader(f)
        for row in csvreader:
           msg=tk.Label(
                   text=row,
                   font=('',20)
                   )
           msg.place(x=50,y=65)

#画像用のキャンバス作成
canvas = tk.Canvas(width=400,height=300)
#キャンバスを設置
canvas.pack()
#画像を用意
photo1 = tk.PhotoImage(file='sky.png')
#画像を描画(中点x,中点y,画像)
canvas.create_image(200,150,image=photo1)

#CVS作成
CreateCVS()

#東京の天気
msg2 = tk.Label(
        text='最高気温と最低気温',
        font=('',20),
        bg = 'Aquamarine'
        )
msg2.place(x=50,y=30)

#ボタン
Button = tk.Button(text=u'東京のお天気は？',height =2,command=showinfo).place(x=150,y=160)
root.mainloop()
