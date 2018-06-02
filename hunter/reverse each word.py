S=raw_input()
N=len(S)
if(1<=N<=100000):
  k=S.split()
  l=[]
  for j in k:
    l.append(j[::-1])
  str1 = ' '.join(l)
  print str1

