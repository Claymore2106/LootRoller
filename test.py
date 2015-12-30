#import dtest
import ihand
import dhand
import ctest


d = {}

print('%sTable should be empty:%s %s' % (ctest.c_Uncommon, ctest.c_Default, str(d)))
print('%sLoading lt.loot as fodder...%s' % (ctest.c_Uncommon, ctest.c_Default))

dhand.d_load('tables/lt.loot', d)

print('%sTable should now have shit loot in it: %s%s' % (ctest.c_Uncommon, ctest.c_Default, str(d)))
print('%sLoading the actual table...%s' % (ctest.c_Uncommon, ctest.c_Default))

dhand.d_load('tables/test.loot', d)

print('%sTable should now be different: %s%s' % (ctest.c_Uncommon, ctest.c_Default, str(d)))
print('%sNow creating a new item:%s' % (ctest.c_Rare, ctest.c_Default))

ihand.i_create(d)

print('%sTable should have the new item!%s' % (ctest.c_Rare, ctest.c_Default))

print(d)

print('%sSaving the new item in save.loot...%s' % (ctest.c_Epic, ctest.c_Default))

dhand.d_save('tables/save.loot', d)