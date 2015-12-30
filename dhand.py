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
	with open(file_path, 'r') as f:
		d = {}
		reader = csv.reader(f)
		
		for k, v in reader:
			d[k] = v
		f.close()
		
		return d


def d_save(file_path, d):
    with open(file_path, 'w') as f:
        for i in d:
            f.write("%s, %s\n" % (i, str(d[i])))