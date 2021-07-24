numberlist = list(range(0,20))
print(numberlist)

numberlist2 = []
for i in numberlist:
	if(i % 2 != 0):
		numberlist2.append(i)

print(numberlist2)

numberlist3 = []
temp = 0
for i in range(0,len(numberlist2)):
	temp = numberlist2[i] + temp
	numberlist3.append(temp)

print(numberlist3)