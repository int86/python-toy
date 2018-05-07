#coding:utf-8    
#!/usr/bin/env python 
""" 
结巴分词生成中文词云
""" 
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import os
import jieba.analyse

from wordcloud import WordCloud, STOPWORDS 
d = path.dirname(__file__) 
 
# Read the whole text. 
content = open(u"txt.txt").read().decode('utf-8') #读取文本，并解码，需注意是GBK还是utf-8
tags = jieba.analyse.extract_tags(content, topK=100, withWeight=False)
text = " ".join(tags)
mask = np.array(Image.open(path.join(d, "1.png"))) 
# Generate a word cloud image 
wordcloud = WordCloud().generate(text) 
 
# the matplotlib way: 
plt.imshow(wordcloud) 
plt.axis("off") 
 
# lower max_font_size 
font=os.path.join(os.path.dirname(__file__), "FZJinHJW.TTF") #设置字体
wordcloud = WordCloud(font_path=font,
max_font_size=50, 
background_color='white',  # 设置背景颜色
max_words = 100, # 设置最大现实的字数
random_state = 50, # 设置有多少种随机生成状态，即有多少种配色方案
mask = mask, #背景图片设置
).generate(text) 
plt.figure() 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.show()
