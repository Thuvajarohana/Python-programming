list=[]
n=int(raw_input())
k=int(raw_input())
for i in range (0,n):
  j=int(raw_input())
  list.append(j)
if(k in list):
  print('yes')
else:
  print('no')
