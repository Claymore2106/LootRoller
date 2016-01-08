import configparser


config = configparser.ConfigParser()
config.read("state/state.config")

sections = config.sections()


def print_debug():
	print("DEBUG")
	for item in sections:
		print(item)
		print("    " + str(config.options(item)))
	print("END DEBUG")


def set_config(section, option, value):
	with open("state/state.config", 'w') as cfgfile:
		value = 'tables/' + value
		config.set(section, option, value)
		config.write(cfgfile)


def get_table():
	setting = config.get('Roller', 'table')
	return setting


# print_debug()
