N=int(raw_input())
list1=[]
if(1<= N <= 100000):
  for i in range(0,N):
    k=int(raw_input())
    list1.append(k)
  for i in range(0,N):
    for j in range(i+1,N):
      if(list1[i]<list1[j]):
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp
  x = int("".join(map(str, list1)))
  print x
