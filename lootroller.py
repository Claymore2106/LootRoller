import argparse
import dhand
import drop


parser = argparse.ArgumentParser('lootroller')
parser.add_argument("COMMAND", choices=['drop', 'list'], required=False)
parser.add_argument("-t", nargs=1, metavar=('<table>'), dest="path", help="File path to the table to load")
parser.add_argument("-v", "--verboose", help="Increase verboosity", action="store_true")
args = parser.parse_args()
if args.COMMAND == drop:
	pass
if args.path:
	if args.verboose:
		print('Creating empty dictionary')
	d = {}
	if args.verboose:
		print('Loading specified file')
	dhand.d_load(args.path[0], d)
	drop.drop(d)

