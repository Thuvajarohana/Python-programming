st=raw_input()
li=[]
for i in st:
  if i not in li and i.isalpha():
    li.append(i.lower())
if len(li)==26:
  print("yes")
else:
  print("no")
