import strcharcount as scc
import math

def power(a,b):
	if b==1:
		return a
	else:
		return (a*power(a,b-1))

n = power(10,5)
nl = math.ceil(math.log2(n))
print(nl)

u_digits = []

for i in range(n):
	if(scc.strcharuniq(str(i))):
		u_digits.append(i)

# print(u_digits)

mn_digits = [0,1]

for i in range(2,n):
	for j in range(2,nl):
		ij = power(i,j)
		if(ij < n):
			mn_digits.append(ij)
		else:
			continue

# print(mn_digits)

umn_digits_set = set(u_digits).intersection(set(mn_digits))

umn_digits = list(umn_digits_set)
umn_digits.sort()

print(umn_digits)