def i_create(d):
	l = []
	name = input('Name of the item: ')
	per = input('Drop rate (do not include %% character): ')
	l.append(per)
	rarity = input('Rarity of %s: ' % name)
	l.append(rarity)
	flavor = input('Flavor text (leave blank for none): ')
	flavor = '"%s"' % flavor  # Add necessary quotation characters
	l.append(flavor)
	d[name] = l
	print("Added %s:%s to table" % (name, l))
	return d

def i_delete(item, d):
    if item in d:
        print("Really delete %s: %s?" % (item, d[item]))
        answer = (input('y/n: ')).lower()
        if answer == 'y':
            del d[item]
            return d
    else:
        print('%s was not found in the table' % item)