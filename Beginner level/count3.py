num=int(raw_input())
count=0
if(num<0):
  num=-num
while(num!=0):
  num=num/10
  count=count+1
print(count)
