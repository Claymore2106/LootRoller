import random


def drop(percent):
	r = random.uniform(0.01, 100)
	
	if r <= float(percent):
		return True
	else:
		return False