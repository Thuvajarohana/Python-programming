N=int(raw_input())
l=[]
if(1<= N <= 1000):
  for i in range(0,N):
    k=int(raw_input())
    l.append(k)
  for i in range(0,N):
    for j in range(i+1,N):
      if(l[i]>l[j]):
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
  print l
  k=(len(l)/2)
  print l[k]
else:
  print("invalid")
