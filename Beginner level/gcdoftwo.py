n1=int(raw_input())
k=int(raw_input())
if(n1>k):
  for i in range(1,n1+1):
    if(n1%i==0 and k%i==0):
      gcd=i
else:
  for j in range(1,k+1):
    if(n1%j==0 and k%j==0):
      gcd=j
print(gcd)
