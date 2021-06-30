"""A Program that creates a linked list of the alphabet with items of size n"""

class linkedlist:

	def __init__(self, currentitem, nextitem):
		self.currentitem = currentitem
		self.nextitem = nextitem

	def current(self):
		return self.currentitem

	def next(self):
		return self.nextitem

while True:
	try:
		n = int(input("Type an integer between 1 and 26: "))
		if(n < 1 or n > 26):
			continue
		break
	except ValueError:
		pass


tempalpha = alpha = alpha_0 = [chr(ord('a')+x) for x in range(0,n)]
templink = mylink = mylink_0 = linkedlist(alpha_0,None)

while('z' not in alpha):

	alpha = [chr(ord(tempalpha[x])+n) for x in range(n)]
	mylink = linkedlist(alpha,None)

	templink.nextitem = mylink

	templink = mylink
	tempalpha = alpha

while ('z' in alpha):
	del alpha[-1]
alpha.append('z')
mylink = linkedlist(alpha,None)
templink.nextitem = mylink
# Linked list complete

# Print out linked list
print(mylink_0.currentitem)
nextlink = mylink_0.nextitem

while(nextlink.nextitem != None):
	print(nextlink.currentitem)
	nextlink = nextlink.nextitem