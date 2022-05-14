#!/usr/bin/env python
# -*- coding: shift_jis -*-

import sys
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pyper
import csv
import time

root = Tk()
root.title(u"いきもの占い")
root.geometry("600x400")

val1 = 0
val2 = 0
val3 = 0
val4 = 0
val5 = 0
val6 = 0
val7 = 0
val8 = 0
val9 = 0
val10 = 0

def check(event):
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    text = ""

    if q1.get() == True:
        val1 = 1
    else:
        val1 = 0

    if q2.get() == True:
        val2 = 1
    else:
        val2 = 0

    if q3.get() == True:
        val3 = 1
    else:
        val3 = 0

    if q4.get() == True:
        val4 = 1
    else:
        val4 = 0

    if q5.get() == True:
        val5 = 1
    else:
        val5 = 0

    if q6.get() == True:
        val6 = 1
    else:
        val6 = 0

    if q7.get() == True:
        val7 = 1
    else:
        val7 = 0

    if q8.get() == True:
        val8 = 1
    else:
        val8 = 0

    if q9.get() == True:
        val9 = 1
    else:
        val9 = 0

    if q10.get() == True:
        val10 = 1
    else:
        val10 = 0

    csvfile = 'DCA.csv'
    csvwfile = 'DCAw.csv'
    f = open(csvfile, "r")
    ff = open(csvwfile, "w")
    reader = csv.reader(f)
    datewriter = csv.writer(ff)
    listdata = ['you', val1, val2, val3, val4, val5, val6, val7, val8, val9, val10]
    print(listdata)
    for row in reader:
              #print row
              datewriter.writerow(row)
    f.close()
    datewriter.writerow(listdata)
    ff.close()
    r = pyper.R(use_pandas='True')
    r("source(file='PCAcode.R')")


    time.sleep(3.0)


    top = Toplevel()
    image = Image.open('plot1.png')
    display = ImageTk.PhotoImage(image)
    c0 = Canvas(top, width = 700, height = 700)
    label = Label(top, image = display)
    label.pack()

    top.mainloop()
    

q1 = BooleanVar()
q2 = BooleanVar()
q3 = BooleanVar()
q4 = BooleanVar()
q5 = BooleanVar()
q6 = BooleanVar()
q7 = BooleanVar()
q8 = BooleanVar()
q9 = BooleanVar()
q10 = BooleanVar()

q1.set(False)
q2.set(False)
q3.set(False)
q4.set(False)
q5.set(False)
q6.set(False)
q7.set(False)
q8.set(False)
q9.set(False)
q10.set(False)

Static1 = Label(text=u"合っているという項目にチェックを付けてね")
Static1.pack()
CheckBox1 = Checkbutton(text=u"Q1:旅が好き", variable=q1)
CheckBox1.pack()
CheckBox2 = Checkbutton(text=u"Q2:派手な服装が好き", variable=q2)
CheckBox2.pack()
CheckBox3 = Checkbutton(text=u"Q3:野菜が好き", variable=q3)
CheckBox3.pack()
CheckBox4 = Checkbutton(text=u"Q4:肉が好き", variable=q4)
CheckBox4.pack()
CheckBox5 = Checkbutton(text=u"Q5:日中に活動する", variable=q5)
CheckBox5.pack()
CheckBox6 = Checkbutton(text=u"Q6:夜中に活動する", variable=q6)
CheckBox6.pack()
CheckBox7 = Checkbutton(text=u"Q7:暑さに強い", variable=q7)
CheckBox7.pack()
CheckBox8 = Checkbutton(text=u"Q8:インドア派である", variable=q8)
CheckBox8.pack()
CheckBox9 = Checkbutton(text=u"Q9:少数で活動する方が好き", variable=q9)
CheckBox9.pack()
CheckBox10 = Checkbutton(text=u"Q10:寒さに強い", variable=q10)
CheckBox10.pack()

button1 = Button(root, text=u'OK',width=30)
button1.bind("<Button-1>",check)
button1.pack()

root.mainloop()
