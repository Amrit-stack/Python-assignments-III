list=[5,4,3,2,1]
print("Before sorting:")
print(list)
for num1 in range(0,len(list)):
	for num2 in range(0,len(list)-1):
		if list[num2]>list[num2+1]:
			temp=list[num2]
			list[num2]=list[num2+1]
			list[num2+1]=temp

print("After sorting:")
print(list)


