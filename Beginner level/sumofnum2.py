k=int(raw_input())
if(k<0):
  k=-k
j=0
while(k!=0):
  m=k%10
  j+=m
  k=k/10
print j
