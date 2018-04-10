val=int(raw_input())
sumofsq=0
while(val!=0):
  m=val%10
  sumofsq+=m**2
  val=val/10
print(sumofsq)
