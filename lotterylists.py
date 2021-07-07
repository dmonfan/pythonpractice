from random import choice

def islistonegreater(numstr, numlist):
	num = ord(numstr)
	print(num)
	numstr2 = choice(numlist)
	numc = ord(numstr2)
	print(numc)
	num = num - 48
	numc = numc - 48 #Adjust so that can loop around 3
	print(num)
	print(numc)
	if((numc%3) == (num+1)%3):
		print('1')
		return True
	else:
		print('0')
		return False

lottery_lists = {
	'1': ['1','2','3'],
	'2': ['2','3','1'],
	'3': ['3','1','2'],
}

print (lottery_lists['1'])
print (choice(lottery_lists['1']))
print (lottery_lists[choice(lottery_lists['1'])])

flag = 0
while True:
	com = input()
	if (islistonegreater('1',lottery_lists['1'])):
		com = input()
		if (islistonegreater('2',lottery_lists['2'])):
			com = input()
			if (islistonegreater('3',lottery_lists['3'])):
				flag = 1
				break
	if(com == 'q'):
		break
	print("Try Again")

if(flag == 1):
	print("Lottery found!")
else:
	print("Exit")