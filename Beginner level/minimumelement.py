num=int(raw_input())
list=[]
if(1<=num<= 100000):
  for i in range(0,num):
    check=int(raw_input())
    list.append(check)
  for x in range(1,num):
    if(list[0]>list[x]):
      list[0]=list[x]
  print(list[0])
else:
  print('invalid')
