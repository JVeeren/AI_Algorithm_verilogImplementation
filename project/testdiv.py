import os 
import time
def div(num1,num2):
	a=num1
	b=num2
	w=a
	i=0
	while 1:
		if b > w :
			break

		else:
			i+=1
			w=w-b
	return i

x=div(5,4)
print(x)