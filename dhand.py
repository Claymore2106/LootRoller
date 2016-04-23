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


def d_save2(file_path, table, delta):
	with open(file_path, 'w') as savefile:
		for item in table:
			values = table[item]
			string_value = ""
			index = 1
			while index <= len(values):
				if index < len(values):
					string_value += "%s," % values[index - 1]
					index += 1
				elif index == len(values):
					string_value += "%s" % values[index - 1]
					index += 1
			savefile.write("%s|%s\n" % (item, string_value))


def d_save(file_path, table, delta):  # FIX THIS
    #with open(file_path, 'w') as f:
    #    for key in d:
    #        f.write("%s|%s\n" % (str(k), str(s)))
    for item in table:
        #b = False
        readfile = open(file_path, 'r')
        if item not in readfile.read():
            string = ""
            position = 1
            for value in table[item]:
                if position < len(table[item]):
                    string += ("%s," % str(value))
                    n += 1
                elif n == len(d[k]):
                    s += str(v)
            with open(file_path, 'w') as f:
                f.write("%s|%s\n" % (str(k), str(s)))
        f.close()
    #print('Wrote %i changes to MASTER-LOOT.loot' % delta)


def d_clear(d):
	d.clear()
