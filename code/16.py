def fuck(a,b):
	i = max(a,b)
	j = min(a,b)
	while(j!=0):
		temp = i%j
		i = j
		j = temp
	print "gongyueshu is ",i
	print "gongbeishu is ",a*b/i	
	

fuck(2,11)
