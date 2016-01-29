import argparse
import dhand
import ihand
import drop
import chand
from os import listdir
from os.path import isfile, join


print(
'\nWelcome to LootRoller!\n'
'\n'
'\n'
'LootRoller is a program designed to create items and loot tables,\n'
'manage those items and tables, and drop items according to chances\n'
'defined by you.\n'
'\n'
'LootRoller runs in a continuous loop. For help, type "help". To exit, type "exit".\n'
'\n'
)


def main_loop():
    command = (input('Command: ')).lower()  # Keep lowercase, so that any combo of caps can be used.
    while command != 'exit':
        
        if command == 'help':
            print(
                '\nCurrently Available actions:\n'
                '-------------\n'
                'Items : Enter the item submenu to create, edit and delete items.\n'
                'NPC   : Enter the NPC submenu to create, edit, and delete NPCs and their tables.\n'
                'Drop  : Enter the item drop submenu to drop items from an NPC.\n'
                'Help  : Display this help message.\n'
                'Exit  : Exit the program.\n'
                '-------------\n'
                )
            command = (input('Command: ')).lower()  # Keep the loop going.

        if command == 'items':
            pass

        if command == 'npc':
            pass

        if command == 'drop':
            pass


main_loop()

"""
if args.ACTION == 'list':
	path = 'tables/'
	current = chand.get_table()
	print('Current table: %s\n' % str(current))
	print("Available loot tables: ")
	files = [f for f in listdir(path) if isfile(join(path, f))]
	print(files)


if args.ACTION == 'select':
	print('Enter ** to list available tables')
	path = input("Path to table: ")
	if path == '**':
		path = 'tables/'
		print("Available loot tables: ")
		files = [f for f in listdir(path) if isfile(join(path, f))]
		print(files)
	path = input("Path to table: ")
	chand.set_config('Roller', 'table', path)


if args.ACTION == 'show':
	d = {}
	table = chand.get_table()
	d = dhand.d_load(table, d)
	print('--------------\n')
	for n in d:
		string = '%s: %s\n' % (str(n), str(d[n]))
		print(string)
	print('--------------')


if args.ACTION == 'edit':
	table = chand.get_table()
	print('Now editing %s -->' % str(table))
	d = {}
	nd = {}
	d = dhand.d_load(table, d)
	n = len(d)
	print('--> %s entries in table' % str(n))
	choice = ""
	while choice != "exit":
		action = input("--> create, edit, show, delete, exit: ")
		print()
		if action == "create":
			ihand.i_create(nd)

		if action == "show":
			print('--------------\n')
			print("Current: ")
			for i in d:
				print(i)
			print("\nDelta: ")
			for i in nd:
				print(i)
		print('--------------')

		if action == "exit":
			choice = "exit"
			for i in nd:
				d[i] = nd[i]
			print(table)
			print(d)
			#delta = len(d) - n
			#if delta > 0:
				#print("Added %s entries" % str(delta))
			#elif delta < 0:
				#print("Removed %s entries" % str(delta))
			dhand.d_save(table, d)

if args.ACTION == 'drop':
	if args.verboose:
		print('Creating empty dictionary')
	d = {}
	if args.verboose:
		print('d = %s' % str(d))
		print('Loading specified file')
	path = chand.get_table()
	dhand.d_load(path, d)
	drop.drop(d)

"""