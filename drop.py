import random
import colors


def drop(d):
	dropstring = ""
	for k in d:
		#print(k)
		#print(d[k])
		percent = d[k][0]
		
		c = colors.c_assign(d[k][1])
		r = random.uniform(0.01, 100)
	
		if r <= float(percent):
			print("Dropped %s%s%s!" % (c, k, colors.c_Default))
			dropstring += k + " "
	return dropstring
