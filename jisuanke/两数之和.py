import os
number = [5,75,25]
target = 80
for i in number:
   for j in number:
       if(number.index(i)==number.index(j)):
           pass
       elif(i+j==target):
           print number.index(i)+1,number.index(j)+1
           os._exit(0)
    
       
        
            
