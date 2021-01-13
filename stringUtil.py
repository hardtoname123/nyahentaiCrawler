#-*- coding:utf-8 -*-
# creator: niming 

import os
import re

def string_match(des,pat):
	res = re.findall(pat,des)
	# for x in res:
	# 	print(x)
	return res

#获取字符串使用 res.group(0)
def string_search(des,pat):
	res = re.search(pat,des)
	return res

def debug():
	des = '<是abcd是a999你是>'
	pat = r"是.+?"
	res = string_match(des,pat)

		
# debug()
