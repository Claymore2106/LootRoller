import argparse
import dhand
import ihand
import drop
import chand
from os import listdir
from os.path import isfile, join


parser = argparse.ArgumentParser('LootRoller')

parser.add_argument("ACTION",  choices=['list', 'select', 'show',  'edit', 'drop'])
parser.add_argument("-t", nargs=1, metavar='<Table>', dest="path", help="File path to the table to load")
parser.add_argument("-v", "--verboose", help="Increase verboosity", action="store_true")

args = parser.parse_args()

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

