# coding=utf-8
list1 = raw_input("请输入数组：")
num = raw_input("请输入待删除的重复的数字")
list1 = list(list1)
num = int(num)
for i in list1:
    if (int(i) == num):
        list1.remove(i)
print len(list1)

