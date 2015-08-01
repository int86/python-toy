def shit(a):
	list1 = []
	list2 = []
	list3 = []
	list4 = []
	for i in a:
		if i>='a' and i<='z':
			list1.append(i)
			a = len(list1)
		elif i>='A' and i<='Z':
			list2.append(i)
			b = len(list2)
		elif i>='0' and i<='9':
			list3.append(i)
			c = len(list3)
		elif i == ' ':
			list4.append(i)
			d = len(list4)
	print "lower word is",a	
	print "upper word is",b
	print "nuber is" ,c
	print "space is ",d
shit('askfjsdf 54HJGBasff sd JKGVB')
