num=int(raw_input())
j=0
for x in range(1,10000):
	if(num%x==0):
		j=j+1
if(j==2):
	print("yes")
else:
	print("no")
