
import importlib.util
import sys

import database as d

import weather_command
import date_time_command

import search_google_command

def check_imports():
	'''
	pip install python-weather
	pip install googlesearch-python
	'''

	print()
	
	import_names = ['itertools', 'sys', 'database', 'weather_command', 'date_time_command', 'search_google_command']

	for i in range(len(import_names)):

		name = import_names[i]
		if name in sys.modules: print("The file, "+name+", is already in sys.modules.")
		elif (importlib.util.find_spec(name)) is not None:
			module = importlib.util.module_from_spec(spec)
			sys.modules[name] = module
			spec.loader.exec_module(module)
			print("The file, "+name+", has already been imported.")
		else: print("Sorry, I can't find "+name+".")

	for i in range(5): print()




if __name__ == "__main__":

	check_imports()

	va = d.database([], 'assistant')

	va.add_to_list(weather_command.weather_command())

	va.add_to_list(date_time_command.date_time_command())

	va.add_to_list(search_google_command.google_search_command())




	va.begin()