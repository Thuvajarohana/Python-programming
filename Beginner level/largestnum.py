num1get=int(raw_input())
num2get=int(raw_input())
num3get=int(raw_input())
if(num1get>num2get and num1get>num3get):
	print(num1get)
elif(num2get>num3get):
	print(num2get)
else:
	print(num3get)
