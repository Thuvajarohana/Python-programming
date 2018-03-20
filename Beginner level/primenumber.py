num=int(raw_input())
j=0
for r in range(1,10000):
	if(num%r==0):
		j=j+1
if(j==2):
	print("yes")
else:
	print("no")
