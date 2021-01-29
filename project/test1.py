
def largest(arr): 
	n = len(arr)
	max = arr[0]
	maxi=0
	# Traverse array elements from second 
	# and compare every element with 
	# current max 
	for i in range(0, n): 
			if arr[i] > max:
				maxi=i 
				max = arr[i] 
	return maxi
 
#arr = [[10, 324, 45, 90, 9808],[20, 124, 55, 60, 10808],[19, 325, 42, 80, 808]]
#n = len(arr)
#print(n)
#m = len(arr[0])
#print(m)
#Ans = largest(arr,n,m) 
#print ("Largest in given array is",Ans) 
 

			 
	
