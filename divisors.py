def divisors (m):
	#m= int(input()) 
	#m+=1
	for i in range(1,m+1):
		if m % i==0:
			print(i)



def EXERCISEB ():
	m = input()
	x = int(len(m)/2)
	i = 0
	j = len(m)-1

	while i<x:
		i+=1
		j-=1
		if i==j:
			print ("True")
		else:
			print ("False")
			break

EXERCISEB()
