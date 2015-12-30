import csv
import dhand


d = {}

dhand.d_load('tables/test.loot', d)

print(d)

for i in d:
	s = ""
	#print(i)
	#print(d[i])
	#print(len(d[i]))
	n = 1
	for v in d[i]:
		if n < len(d[i]):
			s += ("%s," % str(v))
			n += 1
		elif n == len(d[i]):
			s += str(v)
	#print(s)
	with open('tables/save.loot', 'a') as f:
		f.write("%s|%s\n" % (str(i), str(s)))