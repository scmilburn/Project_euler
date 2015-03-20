"""
Simon Milburn

Problem 6
"""


def sqrofsum():
	sqr = 0
	for x in range (1, 101):
		sqr = sqr + x
	return sqr * sqr
def sumofsqr():
	sum = 0
	for x in range (1, 101):
		sum = sum + (x * x)
	return sum

print sqrofsum() - sumofsqr()