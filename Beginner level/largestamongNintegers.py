num=int(raw_input())
list=[]
for i in range(0,num):
  check=int(raw_input())
  list.append(check)
for x in range(1,num):
  if(list[0]<list[x]):
    list[0]=list[x]
print(list[0])
