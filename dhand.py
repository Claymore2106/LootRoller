# Testing if the initialization worked. This file will eventually handle all dictionary functions,
# including initialization, addition, subtraction, and writing.


import csv


def d_ini(file_path, d):
	with open(file_path, 'r') as f:
		reader = csv.reader(f, delimiter = '|')
		
		for k, v in reader:
			d[k] = v
		print('k is: ' + str(k))
		print('v is: ' + str(v))
		f.close()
		return d


def d_load(file_path, d):
	d_clear(d)
	with open(file_path, 'r') as f:
		reader = csv.reader(f, delimiter = '|')
		
		for k, v in reader:
			l = []
			s = ""
			n = 0
			for c in v:
				if c != ',':
					s += c
				elif c == ',':
					l.append(s)
					s = ""
			l.append(s)
			d[k] = l
	return d


def d_save(file_path, d):
	for k in d:
		s = ""
		n = 1
		for v in d[k]:
			if n < len(d[k]):
				s += ("%s," % str(v))
				n += 1
			elif n == len(d[k]):
				s += str(v)
		with open(file_path, 'a') as f:
			f.write("%s|%s\n" % (str(k), str(s)))


def d_clear(d):
	d.clear()
