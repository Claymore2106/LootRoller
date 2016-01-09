import csv


def d_ini(file_path, d):
	with open(file_path, 'r') as f:
		reader = csv.reader(f, delimiter='|')
		
		for k, v in reader:
			l = []
			s = ""
			for c in v:
				if c != ',':
					s += c
				elif c == ',':
					l.append(s)
					s = ""
			l.append(s)
			d[k] = l
	return d


def d_load(file_path, d):
	d_clear(d)
	with open(file_path, 'r') as f:
		reader = csv.reader(f, delimiter='|', quotechar='"')
		
		for k, v in reader:
			l = []
			s = ""
			n = 0
			q = False
			for c in v:  # Lolly|70,c,"Looks like a lolly, tastes like one too! But its a killing machine!"
				if c == '"':
					q = not q
				elif c != ',':
					s += c
				elif c == ',' and q == True:
					s += c
				elif c == ',' and q == False:
					l.append(s)
					s = ""
			l.append(s)
			d[k] = l
	return d


def d_save(file_path, d):
	for k in d:
		b = False
		f = open(file_path, 'r')
		if k not in f.read():
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
		f.close()


def d_clear(d):
	d.clear()
