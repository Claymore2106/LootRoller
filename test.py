import dhand
import ihand
import ctest
import drop


d = {}

dhand.d_load('tables/BOSS_Spider.loot', d)
#print(d)
#for k in d:
#	print(k)
#	print(d[k])
#	print(d[k][0])

def droptest():
	n = 0
	fang = 0
	silk = 0
	stone = 0
	scraps = 0
	blade = 0
	static = 0
	while n < 10:
		print('-----------------')
		r = str(drop.drop(d))
		if 'error-01-bad-value' in r:
			break
		if "Spider's Fang" in r:
			fang += 1
		if "Spider Silk" in r:
			silk += 1
		if "The Saurstone" in r:
			stone += 1
		if "Armor Scraps" in r:
			scraps += 1
		if "Dragonslayer's Blade" in r:
			blade += 1
		if "Static" in r:
			static += 1
		n += 1
	
	print('\n\n\n')
	print('Fang dropped %s times: %s%%' % (fang, (fang / static) * 100))
	print('Silk dropped %s times: %s%%' % (silk, (silk / static) * 100))
	print('Stone dropped %s times: %s%%' % (stone, (stone / static) * 100))
	print('Scraps dropped %s times: %s%%' % (scraps, (scraps / static) * 100))
	print('Blade dropped %s times: %s%%' % (blade, (blade / static) * 100))
	print('Static dropped %s times: %s%%' % (static, (static / static) * 100))


droptest()

#print(drop.drop(d))