n=raw_input()
k=n.split()
l=[]
for j in k:
  l.append(j[::-1])
str1 = ' '.join(l)
print str1
