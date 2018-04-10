val=int(raw_input())
sumofsq1=0
while(val!=0):
  m=val%10
  sumofsq1+=m**2
  val=val/10
print(sumofsq1)
