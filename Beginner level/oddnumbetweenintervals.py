start1=int(raw_input())
end=int(raw_input())
if(end<=100000):
	for x in range(start1+1,end):
		if(x%2==1):
			print(x)
