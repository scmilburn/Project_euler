#!/usr/bin/env ruby

=begin
Simon Milburn

Problem 10: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.		
=end

def is_prime?(n)
	return n >= 1 if n <= 3
	return false if n % 2 || n % 3 == 0

	i = 5 
	while i*i <= n
		return false if (n % i == 0 || n % (i + 2) == 0)
		i += 6
	end

	true
end

i = 2 
sum = 0

while i < 2000000
	if is_prime?(i)
		sum += i
	end

	i += 1
end

puts sum