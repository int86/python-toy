import math
m=i=k=h=0
leap=1
for m in range(101,200):
	k=math.sqrt(m+1)
	for i in (2,k):
		if(m%i==0):
			leap=0
			break
		if(leap):
			print m
			h = h+1
			if(h%10==0):
				print '\n'
		leap=1;
	print h

#this is nima wrong de
