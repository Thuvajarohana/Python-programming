num11get=int(raw_input())
num22get=int(raw_input())
num33get=int(raw_input())
if(num11get>=num22get and num11get>=num33get):
	print(num11get)
elif(num22get>=num33get):
	print(num22get)
else:
	print(num33get)
