#!/usr/bin/env python
#-*- coding:utf-8 -*-

# author:niming
# version 1.01
import os,sys
import tkinter as tk
import tkinter.messagebox
version = 1.01

mainScene = tk.Tk()
stringVarTag = tk.StringVar()
stringVarID = tk.StringVar()


def startScene():
	print("process run")
	mainScene.geometry('500x300')
	mainScene.title('helloworld')
	frame1 = tk.Frame(mainScene)
	frame2 = tk.Frame(mainScene)


	label1 = tk.Label(frame1, text = '请输入Tag:',bg = 'white', font=('Arial', 12), width=30, height=2)
	label1.pack(side = 'left')
	tagInput = tk.Entry(frame1 ,font = ('Arial',14), textvariable = stringVarTag)
	tagInput.pack()


	label2 = tk.Label(frame2, text = '请输入ID:',bg = 'white', font=('Arial', 12), width=30, height=2)
	label2.pack(side = 'left')
	IDInput = tk.Entry(frame2, font = ('Arial',14), textvariable = stringVarID)
	IDInput.pack()
	frame1.pack()
	frame2.pack()


	btn = tk.Button(mainScene, text='start', command = startPy)
	btn.pack()

	mainScene.mainloop()

def startPy():

	stringTag = stringVarTag.get()
	stringID = stringVarID.get()
	tkinter.messagebox.showinfo(title = '消息',message = '下载成功')

	# label3 = tk.Label(mainScene, text = stringTag,bg = 'white', font=('Arial', 12), width=30, height=2)
	# label3.pack()
	
startScene()



