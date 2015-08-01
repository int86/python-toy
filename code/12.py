list1 = []
for i in range(101,201):
	if((i%2!=0)and(i%3!=0)and(i%5!=0)and(i%7!=0)and(i%11!=0)and(i%13!=0)):
		list1.append(i)

print list1
print len(list1)
