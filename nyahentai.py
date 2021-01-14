# coding: utf8
# creator: niming 

import urllib2
import platform
import re,os
import stringUtil as su
_PLATFORM = platform.system()
#使用此header伪装为chrome访问
headersWin = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
headersMac = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'} 
target_url = r'https://nhentai.to/'
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
    path = r'/Users/mingni/Documents/myCrawler/nyahentaiCrawler'
    url = target_url+r'artist/'+mArtist+r'/'
    # url = r'https://nhentai.to'
    # print('openUrl: '+url)
    regs = r'<a href=.+?class="cover"'
    print("获取"+mArtist+"页面:"+url)
    res = chromeReq(url)
    print("进行Artist页面解析")
    matchRes = su.string_match(res,regs)
    urlregs = r'g/(\w)+?/'
    onceFlag = 1
    suffname = ""
    for x in matchRes:
        search = su.string_search(x,urlregs)
        dirname = su.string_search(x,r'[0-9]+').group(0)
        openUrl = target_url+search.group(0)
        if (onceFlag <= 2):
            workRes = getWorkResUrl(openUrl)
            suffname = getImgType(workRes[0])
            onceFlag = onceFlag + 1
            downloadImg(path,workRes,dirname,suffname)

def getWorkResUrl(url):
    print("获取作品内容页面:"+url)
    res = chromeReq(url)
    regs = r'data-src="https.+?"'
    print("进行数据页面解析")
    matchRes = su.string_match(res,regs)
    urlregs = r'https:.+?(png|jpg)'
    dataList = []
    for x in matchRes:
        matchData = su.string_search(x,urlregs)
        dataList.append(matchData.group(0))
    return dataList

def getImgType(imgUrl):
    if imgUrl[-3] == 'p':
        return r"png"
    elif imgUrl[-3] == 'j':
        return r"jpg"
# def downloadImg(img_url,totalpage):
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

def downloadImg(path,urlList,dirname,suffname):
    newPath = path+r'/'+dirname+r'/'
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    picCount = 1
    for x in urlList:
        if True:
            res = chromeReq(x)
            filePath = newPath+str(picCount)+r'.'+suffname
            print("获取图片数据:"+filePath)
            f = open(filePath , "wb")
            f.write(res)
            f.close
            print("图片获取成功")
            picCount = picCount + 1

def runDebug():
    # chromeReq('https://tool.lu')
    openArtistPage('tamano kedama')

runDebug()
