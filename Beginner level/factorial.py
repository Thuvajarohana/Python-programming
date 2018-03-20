numpos=int(raw_input())
fac=1
if(numpos>=0):
	for i in range(1,numpos+1):
		fac*=i
	print(fac)
