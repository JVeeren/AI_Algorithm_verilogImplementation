import os 
import time
import add as add1
def div(num1,num2):
	a=num1
	b=num2
	#print(a1)
	b1="+CFGTYPE1={}"
	b1=b1.format(b)
	#print(b1)
	w=a
	i=0
	while 1:
		if b > w :
			break
		else:
			i=add1.sum(i,1)
			#print(i)
			newpid=os.fork()
			if newpid == 0:
				w1="+CFGTYPE={}"
				w1=w1.format(w)
				args=['./sub8_tb',w1,b1]
				os.execvp("./sub8_tb",args)
			else:
				os.waitpid(0, 0)
				with open("outputsub.txt","r") as f4:
					x=f4.read()
					f4.close()
					x=x.strip()
					y=int(x)
					w=y	#print("jasho")
					#print("here")
					#print(w)
	
	return i