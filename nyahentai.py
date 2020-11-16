# coding: utf8
# creator: niming 

import urllib2
import platform
import re
_PLATFORM = platform.system()
#使用此header伪装为chrome访问
headersWin = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
headersMac = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'} 

def chromeReq(url):
    if (_PLATFORM == 'Darwin'):
        headers = headersMac
    elif(_PLATFORM == 'Windows'):
        headers = headersWin

    req = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(req)
    
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
    # url = r'https://nyahentai.cc'
    print('open_url: '+url)
    res = chromeReq(url)
    print(res)
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
