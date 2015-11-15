# coding=utf-8
import re
import urllib
import MySQLdb

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#连接mysql
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='douban',port=3306)
cur=conn.cursor()

listSum =[]
# 收集subjectID方法
def subjectIDCollect(url):
    html = urllib.urlopen(url).read()
    pattern = re.compile(r'movie\..*\/subject\/\d{5,}\/\B')  #匹配页面中所有object
    list1 = set(pattern.findall(html))
    listSum.append(list1)
    for i in list1:
           subjectIDCollect('http://'+i)
           break
    print listSum
    print len(listSum)

#subjectIDCollect('http://movie.douban.com/subject/20513059/')    


# 排除重复object的方法
#def setObject():
    
    


#分析提取字段的方法

def getFields():
    html = "http://movie.douban.com/subject/20513059/";
    p1 = re.compile(r'(?<=dBy">)[^dBy">].*[^</a>](?=</a>)') #匹配导演
    directer = re.match(p1,html)
    print directer
    

getFields()



#插入数据库
#def insertToDB():
    
    
