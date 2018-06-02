N=int(raw_input())
l=[]
sum1=0
sum2=0
if(2<=N<=100000):
  for i in range(0,N):
    k=int(raw_input())
    l.append(k)
    s=sum(l)/2
    s1=sum(l)%2
  count=0
  for i in range(0,N):
    sum1+=l[i]
    if(sum1<=s+s1):
      sum2+=l[i]
      count=count+1
      avg1=sum2/count
  final=sum2-sum(l)
  count2=len(l)-count
  if(final<0):
    final=-final
  avg2=final/count2
  if(avg1==avg2):
    print("yes")
  else:
    print("no")
