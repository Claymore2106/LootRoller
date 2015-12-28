# This function allows the dictionary to be initialized with what is already in the csv file


import csv


def d_ini():
	with open('lt.csv', 'r') as f:
		reader = csv.reader(f)
		d = {}

		for k, v in reader: # 'k' 'v' are for clarity. Just 'k' would work just as well
			d[k] = v
		f.close()
	
		return d