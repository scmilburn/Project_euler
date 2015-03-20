
#Simon Milburn

#Problem 4:Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome():
	pal = 0
	for i in range (100, 999):
		for j in range (100, 999):
			if palindrome_check(i * j) and i * j > pal:
				pal = i * j
		j = j - 1
	i = i - 1
	return pal

def palindrome_check(n):
	return str(n) == str(n)[::-1]

print(largest_palindrome())