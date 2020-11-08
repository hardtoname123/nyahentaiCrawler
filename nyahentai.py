# coding: utf8
# creator: niming 

import urllib


pathName = 'dora'
mID = '1697712'
totalpage = 0
img_url = r"https://search.pstatic.net/common?src=https://mi.404cdn.com/galleries/"+mID+'/'

#使用此header伪装为chrome访问
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
def chromeReq(url):
    req = request.Request(url,headers = headers)
    return request.urlopen(req)

def openTagPage(mTag):
    pass
    #req = chromeReq(url,headers = headers)
    #print(req)
    #mb.showinfo(title = '消息',message = '下载成功')
           
def openIDPage(mID):
    pass

def openArtistPage(mArtist):    
    url = r'https://nyahentai.cc/Artist/'+mArtist
    print('mArtist:'+url)

def download_img(img_url,totalpage):

    for index in range(1,totalpage):
        img_url_tmp = img_url+str(index)+'.jpg'
        #img_url_tmp = img_url+'list/'+str(index)+'/#pagination-page-top'
        print(img_url_tmp)
        res = urllib.urlopen(img_url_tmp).read()
        path = "C:\\Users\\Mloong\\Desktop\pythonRe\\"+pathName+"\\"+str(index)+".jpg"
        print(path)
        f = open(path , "wb")
        f.write(res)
        f.close()



