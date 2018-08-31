# coding:utf-8
from bs4 import BeautifulSoup
from PIL import Image
from tkinter import *
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import urllib.request
import json
import jsonpath


time = urllib.request.urlopen('http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json')
time_text = time.read()
#time_text = time_text.decode('utf-8')
#soup = BeautifulSoup(time_text,"html.parser")
#html.parser
jsonobj = json.loads(time_text)
date = jsonpath.jsonpath(jsonobj,'$..date')
content = json.dumps(date, ensure_ascii=False)
print(content)
url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/thumbnail/550/"+content.replace("[\"", "").replace("\"]", "").replace("-", "/").replace(" ", "/").replace(":", "")+"_0_0.png"
print(url);

import os, stat
import urllib.request

img_url = url
file_path = 'E:/test/img'
file_name = "pyt"

try:
    # 是否有这个路径
    if not os.path.exists(file_path):
        # 创建路径
        os.makedirs(file_path)
        # 获得图片后缀
    file_suffix = os.path.splitext(img_url)[1]
    print(file_suffix)
    # 拼接图片名（包含路径）
    filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
    print(filename)
    # 下载图片，并保存到文件夹中
    urllib.request.urlretrieve(img_url, filename=filename)

except IOError as e:
    print("IOError")
except Exception as e:
    print("Exception")



#image = wx.Image("E:/test/img/pyt.png", wx.BITMAP_TYPE_PNG)




window = tk.Tk()
window.title("Japan向日葵八号 - 地球实时图")
window.geometry("550x550")
window.resizable(width=False, height=False)

canvas = tk.Canvas(window, bg="black", height=550, width=550)
photo = PhotoImage(format="png", file=r"E:/test/img/pyt.png")
imgLabel = Label(window, image=photo, height=550, width=550)
imgLabel.pack()

canvas.pack()




def fun_timer():
    from bs4 import BeautifulSoup
    from PIL import Image
    import matplotlib.pyplot as plt
    import tkinter as tk
    from tkinter import messagebox
    import urllib.request
    import json
    import jsonpath

    time = urllib.request.urlopen('http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json')
    time_text = time.read()
    # time_text = time_text.decode('utf-8')
    # soup = BeautifulSoup(time_text,"html.parser")
    # html.parser
    jsonobj = json.loads(time_text)
    date = jsonpath.jsonpath(jsonobj, '$..date')
    content = json.dumps(date, ensure_ascii=False)
    print(content)
    url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/thumbnail/550/" + content.replace("[\"", "").replace(
        "\"]", "").replace("-", "/").replace(" ", "/").replace(":", "") + "_0_0.png"
    print(url)

    import os, stat

    img_url = url
    file_path = 'E:/test/img'
    file_name = "pyt"

    try:
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
            # 获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        print(file_suffix)
        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        print(filename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filename=filename)

    except IOError as e:
        print("IOError")
    except Exception as e:
        print("Exception")
    global imgLabel,new_photo

    # image = wx.Image("E:/test/img/pyt.png", wx.BITMAP_TYPE_PNG)
    new_photo = PhotoImage(file=r"E:/test/img/pyt.png")
    imgLabel.configure(image=new_photo)


    global timer
    timer = threading.Timer(300, fun_timer)
    timer.start()


import threading
timer = threading.Timer(300, fun_timer)
timer.start()



window.mainloop()