total=int(raw_input())
req=int(raw_input())
m=[]
sum=0
for i in range(0,total):
	k=int(raw_input())
	m.append(k)
for j in range(0,req):
	sum+=m[j]
print(sum)
