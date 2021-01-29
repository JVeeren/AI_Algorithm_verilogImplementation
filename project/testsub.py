import os 
import time
def sub(num1,num2):
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
		with open("outputsub.txt","r") as f:
			x=f.read()
			f.close()
			x=x.strip()
			y=int(x)
			return y
	else:
		args=['./sub8_tb',a1,b1]
		os.execvp("./sub8_tb",args)
		os.waitpid(0, 0)


			#print("jasho")
	