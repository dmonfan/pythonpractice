from random import choice

lotterylist = ['1','2','3']

#The winning sequence is 1,2,3

input("Try to win!")

tries = 0
flag = 0
while True:
	tries = tries + 1
	first = choice(lotterylist)
	print(first)
	if('1' == first):
		second = choice(lotterylist)
		print(second)
		if('2' == second):
			third = choice(lotterylist)
			print(third)
			if('3' == third):
				flag = 1
				break
	msg = input("Try Again? (press q to quit): ")
	if(msg == 'q'):
		break
if(flag == 1):
	print("You won!")
	print(f"Number of tries: {tries}")
else:
	print("Try again next time.")