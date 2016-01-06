def divisors (m):
	#m= int(input()) 
	#m+=1
	for i in range(1,m+1):
		if m % i==0:
			print(i)
divisors(10)
