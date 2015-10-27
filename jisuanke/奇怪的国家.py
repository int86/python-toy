s1 = list(raw_input("first:"))
s2 = list(raw_input("second:"))
s3 = []
for i in range(0,len(s1)):
    if(s1[i]==s2[i]):
        s3.append('1')
    else:
        s3.append('0')
s3 = ''.join(list(s3))
print s3
