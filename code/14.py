def f(a):
	list1 = [2,3,5,7,11,13,1,17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
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
			


f(101)

