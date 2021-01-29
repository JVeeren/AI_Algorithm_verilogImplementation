COMPILATION:
install python3
$python3 testqlearn1.py  

//compilation takes 1000iterations(i.e nearly 1min to give output)

 *folder project contains all the codes  required for the project 

 	*testqlearn1.py is the main code of the project
 		we made out own functions
 		*add.py for addition
 			*add.py calls the already compiled FullAddertb16.v with two inputs
 		*mult.py for multiplication
 			*mult.py calls the already compiled wallace_tb.v with two inputs


for compilation you need to  first excute  $iverilog FullAddertb16.v -o FullAddertb16 
										   $iverilog wallace_tb.v -o wallace_tb
										   $python3 testqlearn1.py
//these codes are to remove warnings on ubuntu(i am using different version of linux)
  


