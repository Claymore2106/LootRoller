import argparse
import dhand
import drop
import cfgtest
from os import listdir
from os.path import isfile, join


parser = argparse.ArgumentParser('lootroller')
parser.add_argument("ACTION",  choices=['list', 'select', 'drop'])
parser.add_argument("-t", nargs=1, metavar='<Table>', dest="path", help="File path to the table to load")
parser.add_argument("-v", "--verboose", help="Increase verboosity", action="store_true")
args = parser.parse_args()
if args.ACTION == 'select':
	path = input("Path to table: ")
	cfgtest.set_config('Roller', 'table', path)


if args.ACTION == 'list':
	path = 'tables/'
	print("Available loot tables: ")
	files = [f for f in listdir(path) if isfile(join(path, f))]
	print(files)


if args.ACTION == 'drop':
	if args.verboose:
		print('Creating empty dictionary')
	d = {}
	if args.verboose:
		print('Loading specified file')
	path = cfgtest.get_table()
	dhand.d_load(path, d)
	drop.drop(d)

