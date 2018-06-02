N=int(raw_input())
K=int(raw_input())
l=[]
count=0
f=0
for i in range(0,N):
  m=int(raw_input())
  l.append(m)
for i in range(0,N):
  count=0
  for j in range(i+1,N):
    if(l[i]==l[j]):
      count=count+1
      sum1=l[i]+l[j]
      if(count==1 and sum1==K):
        f=1
        print('yes')
if(f!=1):
  print("no")
