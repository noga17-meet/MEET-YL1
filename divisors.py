def divisors (m):
	#m= int(input()) 
	#m+=1
	for i in range(1,m+1):
		if m % i==0:
			print(i)
divisors(10)


#EXERCISE B
m= input()
for i in m:
    if m[0]==m[-1]:
        print ("TRUE")
    #elif m[1]==m[-2]: (cant be because if there is word with 3 letters but it doesnt pakindrome)
        #print ("TRUE")
    else :
        print ("FALSE")
