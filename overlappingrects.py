"""A Simple Class that makes a Rectangle"""

class Rectangle:

	def __init__(self, corner1x, corner1y, corner2x, corner2y):
		self.corner1x = corner1x
		self.corner1y = corner1y
		self.corner2x = corner2x
		self.corner2y = corner2y

	def spacesfilled(self):
		spaces = []
		for x in range(self.corner1x, self.corner2x+1):
			for y in range(self.corner1y, self.corner2y+1):
				spaces.append((x,y))
		return spaces

def overlapping(spaces1,spaces2):
	for space in spaces1:
		if space in spaces2:
			return True
	return False

rect1 = Rectangle(1,1,5,5)
print(rect1.spacesfilled())

rect2 = Rectangle(2,3,6,8)
print(rect2.spacesfilled())

rect3 = Rectangle(6,6,9,9)
print(rect3.spacesfilled())

print(overlapping(rect1.spacesfilled(),rect2.spacesfilled()))
print(overlapping(rect2.spacesfilled(),rect3.spacesfilled()))
print(overlapping(rect1.spacesfilled(),rect3.spacesfilled()))