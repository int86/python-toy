def f(a):
	list1 = []
	for i in range(1,200):
		if((i%2!=0)and(i%3!=0)and(i%5!=0)and(i%7!=0)and(i%11!=0)and(i%13!=0)):
				list1.append(i)
			
	del list1[0]
	list2 = [2,3,5,7,11,13,1]
	list1 = list2+list1

	for i in list1:
		for j in list1:
			for k in list1:
				for l in list1:
					for m in list1:
						if(i*j==a):
							print i,'x',j
							return
						if(i*j*k==a):
							print i,'x',j,'x',k
							return
						if(i*j*k*l==a):
							print i,'x',j,'x',k,'x',l
							return
						if(i*j*k*l*m==a):
							print i,'x',j,'x',k,'x',l,'x',m
							return
							



f(90)







			




