import os 
import time
def mult(num1,num2):
	a=num1
	b=num2
	a1="+CFGTYPE={}"
	a1=a1.format(a)
	#print(a1)
	b1="+CFGTYPE1={}"
	b1=b1.format(b)
	#print(b1)
	newpid=os.fork()
	if newpid == 0:
		args=['./wallace_tb',a1,b1]
		os.execvp("./wallace_tb",args)
	else:
		os.waitpid(0, 0)
		with open("outputmult.txt","r") as f1:
			x=f1.read()
			f1.close()
			x=x.strip()
			y=int(x)
			#print("jasho")

	return y
