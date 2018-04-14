num=int(raw_input())
c=list()
import os
for i in range(0,num):
  b=raw_input()
  c.append(str(b))
d=os.path.commonprefix(c)
print(d)
