def triplet():
	c = 0
	s = 1000
	done = False

	for a in range (1, s/3):
		for b in range (a, s/2):
			c = s - a - b
			if a*a + b*b == c*c:
				done = True
				break
		if done:
			print a
			print b
			print c
			print a*b*c
			break

triplet()