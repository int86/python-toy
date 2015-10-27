# coding=utf-8
import string
str1 = raw_input("请输入字符串(以空格间隔):")
arr = str1.split()
lastWord = arr[-1]
print len(lastWord)

