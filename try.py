# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:29:18 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import imageio
import tkinter as tk
from PIL import ImageTk, Image
import time

PATH = "./output.png"
win=tk.Tk() #建立視窗容器物件
win.title("人工智慧床墊")
win.geometry("1000x500")
label=tk.Label(win, text="翻身結果", font=("Arial", 32)) #建立標籤物件
#label.pack(side="bottom") #顯示元件
label.place(x=200, y=450)

label2=tk.Label(win, text="壓力圖", font=("Arial", 32))
label2.place(x=650, y=450)

production = [0, 0, 0,  0, 878,   0, 0, 0,
              0, 0, 0,  0,   0,   0, 0, 0,
              0, 0, 0,  0,   0,   0, 0, 0,
              0, 0, 0,  0,   0,   0, 0, 0,
              0, 0, 0,  0,   0,   0, 0, 0,
              0, 0, 0,  0,   0,   0, 0, 0,
              0, 0, 0,  0,   0,   0, 0, 0]
width = [23, 41, 46, 51, 55, 60, 65, 83,
          8, 23, 38, 48, 58, 68, 83, 98,
          8, 23, 38, 48, 58, 68, 83, 98,
          8, 23, 38, 48, 58, 68, 83, 98,
          8, 23, 38, 48, 58, 68, 83, 98,
          8, 23, 38, 48, 58, 68, 83, 98,
          8, 23, 38, 48, 58, 68, 83, 98]
length = [173, 173, 173, 173, 173, 173, 173, 173,
          143, 143, 143, 143, 143, 143, 143, 143,
          137, 137, 137, 137, 137, 137, 137, 137,
           84,  84,  84,  84,  84,  84,  84,  84,
           78,  78,  78,  78,  78,  78,  78,  78,
           62,  62,  62,  62,  62,  62,  62,  62,
           21,  21,  21,  21,  21,  21,  21,  21]

colors = np.random.rand(len(production))  # 顏色數組
size = production

cm = plt.cm.get_cmap('OrRd')

ax = plt.axes(xlim = (0, 106), ylim = (0, 190))
img = imageio.imread('直立.jpg')
sc = ax.scatter(width, length, c=production, s=size, alpha=0.6, vmin=0, vmax=1023, cmap=cm)
ax.imshow(img, zorder = 0, extent = [0, 106, 0, 190], aspect = 'auto')
plt.colorbar(sc)

plt.savefig(PATH)#儲存圖片

img_open = Image.open(PATH)
img = ImageTk.PhotoImage(img_open, master=win)
panel = tk.Label(win, image = img)
panel.pack(side = 'right', fill = "both", expand = 1)
panel.place(x=500, y=100)

#win.mainloop()

i=0

while i>=0:
    #print("hello")
    if i==0:
        production = [0, 0, 0, 77, 878,   0, 0, 0,
                      0, 0, 0,  0,   0,   0, 0, 0,
                      0, 0, 0,  0,   0, 409, 0, 0,
                      0, 0, 0,  0, 732, 528, 0, 0,
                      0, 0, 0,  0,   0,   0, 0, 0,
                      0, 0, 1,  0,   0,   0, 0, 0,
                      0, 0, 0,  0,   0,   0, 0, 0]
    if i==1:
        production = [0, 0, 540,   0,   0, 0, 0, 0,
                      0, 0,   0,   0,   0, 0, 0, 0,
                      0, 0, 478,   0,   0, 0, 0, 0,
                      1, 0, 902, 847, 502, 0, 0, 0,
                      0, 0,   0,   0,   0, 0, 0, 0,
                      0, 0,   0,   0,   0, 0, 0, 0,
                      0, 0,   0,   0,   0, 0, 0, 0]
    if i==2:
        production = [  0, 284, 0, 1, 0, 0, 0, 0,
                        0, 779, 0, 0, 0, 0, 0, 0,
                        0,   0, 0, 0, 0, 0, 0, 0,
                      742, 925, 0, 0, 0, 1, 0, 0,
                      698,   0, 1, 0, 0, 0, 0, 0,
                        0,   0, 0, 0, 0, 0, 1, 1,
                        0,   0, 0, 0, 0, 0, 0, 1]
    i=i+1
    if i==3:
        i=-1
    ax.cla()
    img = imageio.imread('直立.jpg')
    size = production
    sc = ax.scatter(width, length, c=production, s=size, alpha=0.6, vmin=0, vmax=1023, cmap=cm)
    ax.imshow(img, zorder = 0, extent = [0, 106, 0, 190], aspect = 'auto')
    plt.savefig(PATH)#儲存圖片
    img_open = Image.open(PATH)
    img = ImageTk.PhotoImage(image=img_open, master=win)
    panel.configure(image=img)
    panel.image=img
    win.update_idletasks()
    time.sleep(1)

win.mainloop()