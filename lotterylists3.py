from random import choice

#Choose items of lottery
lotterylist = ['1','2','3']

#The winning sequence is 1,2,3
#For each different sequence the numbers need to be changed

input("Try to win!")

r = range(1,4)
print(r)

tries = 0
flag = 0
while True:
	tries = tries + 1
	ticketlist = []
	for num in lotterylist:
		numr = choice(r)
		numr = str(numr)
		ticketlist.append(numr)
		if(numr == num):
			continue
		break
	print(ticketlist)
	if(ticketlist == lotterylist):
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