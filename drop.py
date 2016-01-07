import random
import ctest


def drop(d):
	dropstring = ""
	for k in d:
		#print(k)
		#print(d[k])
		percent = d[k][0]
		
		c = ctest.c_Assign(d[k][1])
		r = random.uniform(0.01, 100)
	
		if r <= float(percent):
			print("Dropped %s%s%s!" % (c, k, ctest.c_Default))
			dropstring += k + " "
	return dropstring