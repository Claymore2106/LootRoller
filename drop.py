# Test file for random numbers and ensuring drop percentages match real drop percentages.


import random


def percentage_test(x, y):
	r = random.uniform(0.01, x + y)
	print("r is %f" % r)
	
	if r <= y:
		print("Dropped good sword.")
		return 'g'
	elif r > y and r <= (y + x):
		print("Dropped shitty sword.")
		return 's'


def start():
	x = 3
	xc = 0
	
	y = 1
	yc = 0
	
	d = 0
	
	while d < 10000:
		result = percentage_test(x, y)
		if result == 'g':
			yc += 1
			d += 1
		elif result == 's':
			xc += 1
			d += 1
	print("Drops: %i" % d)
	print("X (%i) drops: %i; %f" % (x, xc, (xc / d) * 100))
	print("Y (%i) drops: %i; %f" % (y, yc, (yc / d) * 100))

