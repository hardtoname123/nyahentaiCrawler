#!/usr/bin/env python
#-*- coding:utf-8 -*-

# author:niming
# version 1.01
import os,sys
import nyahentai as nht
import Tkinter as tk
import tkMessageBox as mb


version = 1.01

mainScene = tk.Tk()
stringVarTag = tk.StringVar()
stringVarID = tk.StringVar()
stringVarArtist = tk.StringVar()

def startScene():
	print("process run")
	mainScene.geometry('500x300')
	mainScene.title('helloworld')
	frame1 = tk.Frame(mainScene)
	frame2 = tk.Frame(mainScene)
	frame3 = tk.Frame(mainScene)


	label1 = tk.Label(frame1, text = '请输入Tag:', font=('Arial', 12), width=30, height=2)
	label1.pack(side = 'left')
	tagInput = tk.Entry(frame1 ,font = ('Arial',14), textvariable = stringVarTag)
	tagInput.pack()


	label2 = tk.Label(frame2, text = '请输入ID:', font=('Arial', 12), width=30, height=2)
	label2.pack(side = 'left')
	IDInput = tk.Entry(frame2, font = ('Arial',14), textvariable = stringVarID)
	IDInput.pack()

	label3 = tk.Label(frame3, text = '请输入Artist:', font=('Arial', 12), width=30, height=2)
	label3.pack(side = 'left')
	IDInput = tk.Entry(frame3, font = ('Arial',14), textvariable = stringVarArtist)
	IDInput.pack()

	frame1.pack()
	frame2.pack()
	frame3.pack()

	btn = tk.Button(mainScene, text='start', command = startPy)
	btn.pack()

	mainScene.mainloop()

def startPy():
        
	stringTag = stringVarTag.get()
	stringID = stringVarID.get()
	stringArtist = stringVarArtist.get()
	print(stringTag+','+stringID+','+stringArtist)
	# if len(stringID) > 0:
	# 	nht.openIDPage(StringID)
	# elif len(stringTag) > 0:
	# 	nht.openArtistPage(stringTag)
	
	# else:
	# 	pass
	
		
	
startScene()



