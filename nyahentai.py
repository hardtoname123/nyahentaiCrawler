# coding: utf8
# creator: niming 

import urllib2
import platform
import re
_PLATFORM = platform.system()
#使用此header伪装为chrome访问
headersWin = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
headersMac = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'} 
def chromeReq(url):
    if (_PLATFORM == 'Darwin'):
        headers = headersMac
    elif(_PLATFORM == 'Windows'):
        headers = headersWin
    print(_PLATFORM)
    req = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(req)
    print(response.read())
    return response.read()
    

def openTagPage(mTag):
    pass
    #req = chromeReq(url,headers = headers)
    #print(req)
    #mb.showinfo(title = '消息',message = '下载成功')
           
def openIDPage(mID):
    pass

def openArtistPage(mArtist):
    mArtist = mArtist.replace(' ','-')
    url = r'https://nyahentai.cc/artist/'+mArtist+r'/'
    print('open_url: '+url)
    res = chromeReq(url)
    
# def download_img(img_url,totalpage):

#     for index in range(1,totalpage):
#         img_url_tmp = img_url+str(index)+'.jpg'
#         #img_url_tmp = img_url+'list/'+str(index)+'/#pagination-page-top'
#         print(img_url_tmp)
#         res = urllib.urlopen(img_url_tmp).read()
#         path = "C:\\Users\\Mloong\\Desktop\pythonRe\\"+pathName+"\\"+str(index)+".jpg"
#         print(path)
#         f = open(path , "wb")
#         f.write(res)
#         f.close()

def runDebug():
    # chromeReq('https://tool.lu')
    openArtistPage('tamano kedama')

runDebug()
