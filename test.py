#import dtest
import ihand
import dhand
import dtest
import ctest


d = {}

dhand.d_load('tables/test.loot', d)

print('Current table: %s' % str(d))
for k in d:
	print(k)
	print(d[k])
	for i in d[k]:
		print(i)

ihand.i_create(d)

dtest.d_tsave('tables/test.loot', d)