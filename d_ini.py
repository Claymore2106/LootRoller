import csv


def d_ini():
	with open('lt.csv', 'r') as f:
		reader = csv.reader(f)
		d = {}

		for k, v in reader:
			d[k] = v
		f.close()
	
		return d