n=int(raw_input())
lis=[]
dup=[]
final=[]
for i in range(0,n):
  q=int(raw_input())
  lis.append(q)
  dup.append(-1)
for i in range(0,n):
  count=1
  for j in range(i+1,n):
    if(lis[i]==lis[j]):
      count=count+1
      dup[j]=0
  if(dup[i]!=0):
    dup[i]=count
for i in range(0,n):
  if(dup[i]>1):
    final.append(lis[i])
for i in range(0,len(final)):
  for j in range(i+1,len(final)):
    if(final[i]>final[j]):
      temp=final[i]
      final[i]=final[j]
      final[j]=temp
if(final==[]):
  print("unique")
else:
  print final
