# Database, first layer

class database():
	#the main interface for all subclasses
	'''
	Represents the entire database as an object.
	Comes as one object w/ a name and a list built to work as an interface
        for all incoming commands, running them with the execute method below.
	'''
	def __init__(self, list_of_object_types = [], name = 'default'):

		self._name = name
		self._list = list_of_object_types

		"""
		print(self)
		print(self._name)
		print(self._list)
		"""

	def execute(self, command_list):
		'''
		Process:
                1. takes list of commands in any order
                2. iterate through until object appropriate to acting
                layer is found
                3. execute target
		'''

		i = 0
		command_found = False
		while command_list != []:
			for j in range(len(self._list)):
				if command_list[i] == self._list[j]._name:
					#print('word ' + command_list[i] + ' recognized!')
					command_found = True
					command_list.pop(i)
					if command_list == []: self._list[j].execute()
					else: self._list[j].execute(command_list)
			if command_found == False: command_list.pop(i)
			i+=1
		if not command_found: raise Exception("Command not found, sorry...")

	def create_object_type(self, name):
		'''
		given name, create new object_type object and place in database list
		'''
		self._list.append(object_type(name))

	def create_object(self, object, object_type):
		'''
		given object and str object_type name; place object in object_type list
		'''

		for i in range(len(self._list)):
			if self._list[i]._name == object_type:
				self._list[i].create_object(object)

	def display(self, beginning = None, indent = ''):
		'''
		given object to begin iterating from (user should usually input database)
		iterate through each layer returning the names of each object
		'''
		if beginning == None: beginning = self

		for i in range(len(beginning._list)):
			print(indent + beginning._list[i]._name)
			if beginning._list[i]._list: self.display(beginning._list[i], indent+' ')
		

# Object Type Superclass, second layer

class object_type(database):
	#abstract class holding pointers to the actual objects
	def __init__(self, name, list_of_objects = []):
		database.__init__(self, list_of_objects, name)

	def create_object(self, object):
		self._list.append(object)


# Object Types, third layer

class test_object(object_type):
	#example object type for testing, do not use
	def __init__(self, name = 'default_name'):
		self._name = name
		self._list = None

	def execute(self):
		print("Hello!")

if __name__ == "__main__":
	
	example_database = database()

	example_database.create_object_type('test')

	print(example_database._list)

	#example_database._list[0].create_object(test_object())

	example_database.create_object(test_object(), 'test')

	for i in range(5): print()
	print('display test:')
	print()

	example_database.display()

	for i in range(5): print()
	print('execution test:')
	print()
	
	cmdlist = ['test', 'default_name']
	example_database.execute(cmdlist)
