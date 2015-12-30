from dhand import *


d = {}


def create_item(d):
    print(d)
    name = input("Name of object: ")
    value = input("Drop percentage (whole number): ")
    print("%s: %s%%" % (name, value))
    d[name] = [value]
    print(d)
    rarity = input('Rarity (g, c, u, r, e, l): ')
    d[name].append(rarity)
    print(d)
    print("Writing object to test.csv...")
    
    d_save('tables/test.csv', d)


#create_item(d)

print(d)
print('Loading test/csv...')
d_ini('tables/test.csv', d)
print('Table looks like ' + str(d))
print('Attempting to access variables:')
print("James's Sword should be: " + str(d["James's Sword"]))
print("Rarity is: " + str(d["James's Sword"][1]))