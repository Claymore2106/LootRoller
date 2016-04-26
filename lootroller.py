import argparse
import dhand
import ihand
import drop
import chand
from os import listdir
from os.path import isfile, join


def printer(location, *var1):
    if location == "main":
        print(
        '\n'
        '----------------------\n'
        'Welcome to LootRoller!\n'
        '----------------------\n'
        '\n'
        'LootRoller is a program designed to create items and loot tables,\n'
        'manage those items and tables, and drop items according to chances\n'
        'defined by you.\n'
        '\n'
        'LootRoller runs in a continuous loop. For help, type "help". To exit, type "exit".\n'
        )  # Print this jazz only one time hopefully.

    elif location == "main help":
        print(
        '\nCurrently Available actions:\n'
        '-------------\n'
        'Items : Enter the item submenu to create, edit and delete items.\n'
        'NPC   : Enter the NPC submenu to create, edit, and delete NPCs and their tables.\n'
        'Drop  : Enter the item drop submenu to drop items from an NPC.\n'
        'Help  : Display this help message.\n'
        'Exit  : Exit the program.\n'
        '-------------\n'
        )  # Help section for main

    elif location == "items":
        print(
            '\nEntering menu >> items...\n'
            '\n'
            '---------------------------\n'
            '\n'
            "Type 'help' for available options.\n"
            "Type 'back' to exit this submenu, or 'exit' to exit program.\n"
            '\n'
            'Loaded ' + str(var1) + ' items from the master table.\n'
            )

    elif location == "items help":
        print(
            '\nCurrently Available actions:\n'
            '---------------\n'
            'Create : Create a new item for use in loot tables.\n'
            'Edit   : Edit an existing item. This will affect items in loot tables.\n'
            'Delete : Remove an item entirely from the master list and all loot tables.\n'
            'List   : List all items in the master table.\n'
            'Save   : Save working changes into the master table.\n'
            'Help   : Display this help message.\n'
            'Back   : Exit the Items submenu and return to the main menu\n'
            'Exit   : Exit the program.\n'
            '---------------\n'
            )


def main():
    printer("main") # Print the Main Section Text

    command = ''  # Initialize an empty command string
    while command != 'exit':
        command = (input('Menu >> Command: ')).lower()  # Keep lowercase, so
                                            # that any combo of caps can be used

        if command == 'help':
            printer("main help")

        if command == 'items':
            master_table = {}
            working_table = {}
            master_table = dhand.d_load('tables/MASTER-LOOT.loot', master_table)
            working_table = dhand.d_load('tables/MASTER-LOOT.loot', working_table)
            master_length = len(master_table)
            delta = 0

            printer("items", str(master_length))  # Print Items Section Text

            while command != 'exit':
                command = (input('Items >> Command: ')).lower()

                if command == 'help':
                    printer("items help")  # Print Items' Help Section

                if command == 'back':
                    break

                if command == 'create':
                    ihand.i_create(working_table)
                    delta += 1

                if command == 'delete':
                    item = input("Exact name of item to delete: ")
                    ihand.i_delete(item, working_table)
                    delta += 1

                if command == 'save':
                    dhand.d_save2('tables/MASTER-LOOT.loot', working_table, delta)

                if command == 'list':
                    i = 1
                    print('\n'
                        'Master Table:\n'
                        '-------------'
                        )
                    for item in sorted(master_table):
                        print('[%i] %s: %s' % (i, item, master_table[item]))
                        i += 1
                    print('')
                    if delta != 0:
                        print(
                            'Working Table: (These changes have not yet been saved):\n'
                            '--------------'
                            )
                        i = 1
                        for item in sorted(working_table):
                            if item not in master_table:
                                print('+ [%i] %s: %s' % (i, item, working_table[item]))
                                i += 1
                        i = 1
                        for item in sorted(master_table):
                            if item not in working_table:
                                print('- [%i] %s: %s' % (i, item, master_table[item]))
                        #i = 1
                        #for item in sorted(working_table):
                        #    if working_table[item] != master_table[item]:
                        #        print('<> [%i] %s: %s' % (i, item, working_table[item]))
                        print('')
        if command == 'npc':
            pass

        if command == 'drop':
            pass


main()


#if args.ACTION == 'list':
#	path = 'tables/'
#	current = chand.get_table()
#	print('Current table: %s\n' % str(current))
#	print("Available loot tables: ")
#	files = [f for f in listdir(path) if isfile(join(path, f))]
#	print(files)


#if args.ACTION == 'select':
#	print('Enter ** to list available tables')
#	path = input("Path to table: ")
#	if path == '**':
#		path = 'tables/'
#		print("Available loot tables: ")
#		files = [f for f in listdir(path) if isfile(join(path, f))]
#		print(files)
#	path = input("Path to table: ")
#	chand.set_config('Roller', 'table', path)


#if args.ACTION == 'show':
#	d = {}
#	table = chand.get_table()
#	d = dhand.d_load(table, d)
#	print('--------------\n')
#	for n in d:
#		string = '%s: %s\n' % (str(n), str(d[n]))
#		print(string)
#	print('--------------')


#if args.ACTION == 'edit':
#	table = chand.get_table()
#	print('Now editing %s -->' % str(table))
#	d = {}
#	nd = {}
#	d = dhand.d_load(table, d)
#	n = len(d)
#	print('--> %s entries in table' % str(n))
#	choice = ""
#	while choice != "exit":
#		action = input("--> create, edit, show, delete, exit: ")
#		print()
#		if action == "create":
#			ihand.i_create(nd)

#		if action == "show":
#			print('--------------\n')
#			print("Current: ")
#			for i in d:
#				print(i)
#			print("\nDelta: ")
#			for i in nd:
#				print(i)
#		print('--------------')

#		if action == "exit":
#			choice = "exit"
#			for i in nd:
#				d[i] = nd[i]
#			print(table)
#			print(d)
#			#delta = len(d) - n
#			#if delta > 0:
#				#print("Added %s entries" % str(delta))
#			#elif delta < 0:
#				#print("Removed %s entries" % str(delta))
#			dhand.d_save(table, d)

#if args.ACTION == 'drop':
#	if args.verboose:
#		print('Creating empty dictionary')
#	d = {}
#	if args.verboose:
#		print('d = %s' % str(d))
#		print('Loading specified file')
#	path = chand.get_table()
#	dhand.d_load(path, d)
#	drop.drop(d)
