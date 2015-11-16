# coding=utf-8
import re
import urllib
import threading
import time
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

#获取图片url数组
def getUrl(url,k,j):
    i = k
    list2=[]
    for num in range(0,3):
        url = url+str(i)
        html = urllib.urlopen(url).read()
        pattern = re.compile(r'http:\/\/img\d{0,}\..*\/thumb\/.*\.jpg')
        try:
            list1 = pattern.findall(html)
            list2.append(list1)
            time.sleep(3)
            i= i+j
        except BaseException, e:
            print e
    downLoadImg(list2)

#下载图片
def downLoadImg(list1):
    for i in list1:
        for ImgUrl in i:
            ImgUrl = ImgUrl.replace('thumb','photo')
            filename = r'./'+str(time.time())+'.jpg'
            data = urllib.urlopen(ImgUrl).read()
            print filename
            f = open(filename,'wb').write(data)
            
    

def f1():
    getUrl("http://www.douban.com/photos/album/120893724/?start=",0,18)
def f2():
    getUrl("http://www.douban.com/photos/album/120893724/?start=",36,18)
def f3():
    getUrl("http://www.douban.com/photos/album/120893724/?start=",72,18)
def f4():
    getUrl("http://www.douban.com/photos/album/120893724/?start=",108,18)
def f5():
    getUrl("http://www.douban.com/photos/album/120893724/?start=",126,18)
def f6():
    getUrl("http://www.douban.com/photos/album/120893724/?start=",144,0)
#执行多线程    
threads = []
t1 = threading.Thread(target=f1)
threads.append(t1)
t2 = threading.Thread(target=f2)
threads.append(t2)
t3 = threading.Thread(target=f3)
threads.append(t3)
t4 = threading.Thread(target=f4)
threads.append(t4)
t5 = threading.Thread(target=f5)
threads.append(t5)
t6 = threading.Thread(target=f6)
threads.append(t6)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()
