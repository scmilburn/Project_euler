"""
Simon Milburn

Problem 12:

What is the value of the first triangle number to have over five hundred divisors?
18 
"""

import prime

for i in range(1, 1000000000):
	x = i *(i+1) / 2
	if prime.num_factors(x) > 500:
		print x
		break