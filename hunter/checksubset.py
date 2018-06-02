N=int(raw_input())
N1=int(raw_input())
list1=[]
list2=[]
f=0
for i in range(0,N):
  k=int(raw_input())
  list1.append(k)
for i in range(0,N1):
  l=int(raw_input())
  list2.append(l)
for j in list2:
		if j in list1:
			continue
		else:
			f=1
			break
if f==1:
	print('NO')
else :
	print('YES')
