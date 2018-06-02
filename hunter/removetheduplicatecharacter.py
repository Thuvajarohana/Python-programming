s=raw_input()
k=[]
final=[]
for letter in s:
  k.append(letter)
final=[]
for i in k:
  if i not in final:
    final.append(i)
print ''.join(final)
