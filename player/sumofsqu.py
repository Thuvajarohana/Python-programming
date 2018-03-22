num=int(raw_input())
sum=0
while(num!=0):
  k=num%10
  sum=sum+(k**2)
  num=num/10
print(sum)
