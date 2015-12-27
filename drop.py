# define two numbers that are percents
# generate a number between 1 and 100 that represents the drop
# if its equal to or below a percent, drop that item
# if it is greater than a percent, drop the next item


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

