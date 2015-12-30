from drop import *
from dhand import *


table = {}

table = d_load('tables/test.csv', table)


def dropItem(t):
	for i in t:
		if drop(i, table[i]):
			print("Dropped %s!" % i)
		else:
			print("Dropped nothing.")


def testDrop(t):
	iR = 0
	iL = 0
	count = 0
	while count < 10000:
		for i in t:
			if drop(table[i]):
				print("Dropped %s!" % i)
				if i == "Rare Sword":
					iR += 1
				elif i == "Legendary Sword":
					iL += 1
			else:
				print("Dropped nothing.")
		count += 1
	print('Drops: %i' % count)
	print('Rare: %i; %f%%' % (iR, (iR / count) * 100))
	print('Legendary: %i; %f%%' % (iL, (iL / count) * 100))


testDrop(table)