def d_tsave(file_path, d):
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