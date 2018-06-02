a=raw_input().split()
b=raw_input().split()
c=raw_input().split()
d=raw_input().split()
l=[]
for i in range(0,2):
  l.append(a[i])
for i in range(0,2):
  l.append(b[i])
for i in range(0,2):
  l.append(c[i])
for i in range(0,2):
  l.append(d[i])
for i in range(0,len(l)):
  for j in range(i+1,len(l)):
    if(l[i]==l[j]):
      l[i]=0
      l[j]=0
if all(v==0 for v in l):
  print("yes")
else:
  print("no")
