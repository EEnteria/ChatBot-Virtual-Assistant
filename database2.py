import speech_recognition as sr

#Database, first layer

class database():
	#the main interface for all subclasses
	def __init__(self, list_of_object_types = [], name = 'default'):

		self._name = name
		self._list = list_of_object_types

		"""
		print(self)
		print(self._name)
		print(self._list)
		"""

	def run(self, m=sr.Microphone(), r=sr.Recognizer()):
		print("Hello! Press <ENTER> to begin!")
		input()

		self.execute(self.translate(self.listen_for_input(m, r)))
		

	def execute(self, command_list):
		'''
		takes list of commands in any order
		iterate through until object appropriate to acting layer is found
		execute target
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

	def listen_for_input(self, m=sr.Microphone(), r=sr.Recognizer()):
		
		answer = 'N'

		while answer == 'N' or answer == 'n':
			print("Listening...")
			with m as source: audio=r.listen(source, 7, 5)

			print("Houndify recognized:")
			recognized_audio_string = r.recognize_houndify(audio, "vObDPB9syIEOKJn4ZT8XNw==", "kRgINvNQvmpnNYun5tG0NitvlN4SahAXAXaq2IhcLq1OX2HW_jLmvUfJxC-lt9wM5dX3kC0rtGPGrrAL0yEajw==")
			print(recognized_audio_string)

			print()
			print("Is this correct? <Y/N>")

			answer = input()

			while answer != 'N' and answer != 'n' and answer != 'Y' and answer != 'y':
				print("Invalid response... Houndify recognized:")
				print(recognized_audio_string)
				print()
				print("Is this correct? <Y/N>")
				answer = input()

			if answer == 'Y' or answer == 'y': return recognized_audio_string



	def translate(self, audio_string):
		translated_command_list = ['']

		for i in range(len(audio_string)):
			if audio_string[i] == ' ':
				translated_command_list.append('')
			else: translated_command_list[-1]+=audio_string[i]

		return translated_command_list

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
	def __init__(self, name = 'default'):
		self._name = name
		self._list = None

	def execute(self):
		print("Hello!")

if __name__ == "__main__":
	
	example_database = database()

	example_database.create_object_type('test')

	#print(example_database._list)

	#example_database._list[0].create_object(test_object())

	example_database.create_object(test_object(), 'test')

	for i in range(5): print()
	print('display test:')
	print()

	example_database.display()

	for i in range(5): print()
	print('execution test:')
	print()
	
	cmdlist = ['test', 'default']
	example_database.execute(cmdlist)

	for i in range(5): print()
	'''
	print('translation test:')
	print()

	print(example_database.translate(example_database.listen_for_input()))

	for i in range(5): print()
	print('F I N A L   T E S T :')
	print()
	'''


	example_database.run()
