c_Default = '\033[0m'

c_Garbage = '\033[100m'
c_Common = '\033[01m'
c_Uncommon = '\033[01;32m'
c_Rare = '\033[01;94m'
c_Epic = '\033[01;35m'
c_Legendary = '\033[01;36m'
start = '\033['


def c_Test():
	n = 0
	while n <= 108:  # Stops at 108
		print("%s%sm%s Test Text%s" % (start, str(n), str(n), c_Default))
		n += 1

def c_Assign(r):
	if r == 'g':
		return c_Garbage
	if r == 'c':
		return c_Common
	if r == 'u':
		return c_Uncommon
	if r == 'r':
		return c_Rare
	if r == 'e':
		return c_Epic
	if r == 'l':
		return c_Legendary

#print('%sThunderfury, Blessed Blade of the Windseeker%s: %s+5 Stamina%s, %s+5 Fire Resistance%s, %s"Once weilded by Thunderaan, the Prince of Air. Now it is weilded by you."%s' % (c_Legendary, c_Default, c_Uncommon, c_Default, c_Uncommon, c_Default, test, c_Default))

#c_Test()