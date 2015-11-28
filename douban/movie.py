# coding=utf-8
import re
import urllib
import MySQLdb

head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#连接mysql
conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='douban',port=3306)
cur=conn.cursor()


#模拟登录




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
<<<<<<< HEAD
    url = "http://movie.douban.com/subject/1329562/";
    html = urllib.urlopen(url).read()

    p1 = re.compile(r'(?<=dBy">).*?(?=</a>)') #匹配导演 ok

    # p2 = re.compile(r'(?<=starring">)[^strring">].?[^\</a>](?=\</a>)') #匹配主演  ok
    # p3 = re.compile(r'(?<=c.*/\d{4,}/">)[^c.*/\d{4,}/].*?[^\</a>](?=\</a>)') #匹配编剧
    # p4 = re.compile(r'(?<=content=")[12][0-9]{3}-[0-9]{2}-[0-9]{2}') #匹配年份  ok
    # p5 = re.compile(r'(?<=制片国家/地区:</span>).*(?=<br\/>)') #匹配国家或地区 ok
    # p6 = re.compile(r'(?<=average">).*?(?=</strong>)') #匹配评分 ok
    # p7 = re.compile(r'(?<=<title>\s).*(?=\s</title>)') #匹配电影名字
    # p8 = re.compile(r'(?<=genre">).*?(?=</span>)') #匹配类型  ok
    directer = re.match(p1,html);
    print directer
    
getFields()



#插入数据库
