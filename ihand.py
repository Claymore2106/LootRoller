def i_create(d):
	l = []
	name = input('Name of the item: ')
	per = input('Drop rate (do not include %% character): ')
	l.append(per)
	rarity = input('Rarity of %s: ' % name)
	l.append(rarity)
	flavor = input('Flavor text (leave blank for none): ')
	flavor = '"%s"' % flavor
	l.append(flavor)
	d[name] = l
	return d

