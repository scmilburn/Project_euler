"""
Simon Milburn

Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def largest_prime(n):
	i = 1
	while i < n:
		if n % i == 0:
			n = n / i
		i = i + 1
	return n

print(largest_prime(600851475143))