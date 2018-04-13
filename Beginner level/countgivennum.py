list=[]
n=int(raw_input())
k=int(raw_input())
count=0
for i in range (0,n):
  j=int(raw_input())
  list.append(j)
for x in range(0,n):
  if(k==list[x]):
    count=count+1
print(count)
