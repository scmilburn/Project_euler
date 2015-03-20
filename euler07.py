import math

def isprime(n):
	if n <= 1:
		return False
	if n == 2:
		return True
	if n%2 == 0:
		return False
	for x in range (3, int(math.sqrt(n)) + 1):
		if n%x == 0:
			return False
	return True

def getprime(n):
	x = 0
	count = 0
	while count != n:
		x = x + 1
		if isprime(x) == True:
			count = count + 1
	print x

getprime(10001)