
upperlimit = 100000 #1 Million

for i in range(2,upperlimit) :
	#Assume i to be prime
	prime = True
	
	#loop from 0 to i-1
	for j in range(2,i) :
		
		#Test j divides i and break if it does
		if i % j == 0 :
			break
	
	else :
		print(i)

else :
	print('Upper limit reached')