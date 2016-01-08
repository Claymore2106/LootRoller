import configparser


config = configparser.ConfigParser()
config.read("state/state.config")

sections = config.sections()


def print_debug():
	for item in sections:
		print(item)
		print("    " + str(config.options(item)))


#print_debug()
