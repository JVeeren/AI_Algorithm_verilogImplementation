import os 
import time
def sum(num1,num2):
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
		with open("output.txt","r") as f:
			x=f.read()
			f.close()
			x=x.strip()
			y=int(x)
			return y
	else:
		args=['./eight_tb',a1,b1]
		os.execvp("./eight_tb",args)
		os.waitpid(0, 0)
			#print("jasho")

	


#print(sum(3,4))