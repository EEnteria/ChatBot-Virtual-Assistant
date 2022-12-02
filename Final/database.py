import speech_recognition as sr

#Database, first layer

class database():
	#the main interface for all subclasses, commands, etc. Run everything through this object.
	def __init__(self, list_of_object_types = [], name = ['default']):
		'''
		Create database object, should generally have no arguments.
		'''

		self._name = name
		self._list = list_of_object_types

		"""
		print(self)
		print(self._name)
		print(self._list)
		"""

	def begin(self, m=sr.Microphone(), r=sr.Recognizer()):
		'''
		THIS IS THE PRIMARY COMMAND. RUN THIS TO BEGIN THE PROGRAM.
		Takes microphone and recognizer object arguments as specified in speech_recognition library. Not necessary to give.
		Waits for user input, then begins.
		Runs listen_for_input(microphone, recognizer), then passes its returned audio_string to
		translate(audio_string) which converts the string to a list formatted ['word1', 'word2', 'etc'], which is then passed to 
		execute(command_list)
		'''
		print("Hello! Press <ENTER> to begin!")
		input()
		for a in range(5): print()

		self.execute(self.translate(self.listen_for_input(m, r)))
		

	def execute(self, command_list):
		'''
		This method takes list of commands in any order to be executed.
		It iterates through the command_list until an object appropriate to acting layer is found. (database --> object_type --> object)
		It finally passes the target object to execute. (This is a recursive function.)
		(Objects will have unique execute methods dependent on their object_type. See test_object class for an example.)
		'''
		
		for i in range(len(command_list)):
			for j in range(len(self._list)):
				if command_list[i] in self._list[j]._name:
					print('word ' + command_list[i] + ' recognized!')
					for a in range(5): print()
					command_list.pop(i)
					self._list[j].execute(command_list)
					return None
					
		print("Sorry, I don't understand...")
		print()
		print("Please try again.")
		for i in range(3): print()
		self.begin()

	def listen_for_input(self, m=sr.Microphone(), r=sr.Recognizer()):
		'''
		This method takes microphone and recognizer objects as specified in the speech_recognition library, and returns a string of decoded audio.
		The User must provide input to confirm that the recognized_audio_string is accurate to what was spoken.
		'''
		
		answer = 'N'

		while answer == 'N' or answer == 'n':
			print("Listening...")
			with m as source: audio=r.listen(source, 7, 5)

			print("Houndify recognized:")
			recognized_audio_string = r.recognize_houndify(audio, "vObDPB9syIEOKJn4ZT8XNw==", "kRgINvNQvmpnNYun5tG0NitvlN4SahAXAXaq2IhcLq1OX2HW_jLmvUfJxC-lt9wM5dX3kC0rtGPGrrAL0yEajw==")
			print(recognized_audio_string)

			print()
			print("Is this correct?")
			print()

			print("Listening...")
			with m as source: confirmation_audio=r.listen(source, 7, 5)
			confirmation = r.recognize_houndify(confirmation_audio, "vObDPB9syIEOKJn4ZT8XNw==", "kRgINvNQvmpnNYun5tG0NitvlN4SahAXAXaq2IhcLq1OX2HW_jLmvUfJxC-lt9wM5dX3kC0rtGPGrrAL0yEajw==")
			print("You said: "+confirmation)

			if confirmation == "yes": return recognized_audio_string

			elif confirmation == "no": print("I'm sorry, please try again:")

			else: 
				print("Sorry, I didn't understand that...")
				print()
				print("You said <"+recognized_audio_string+">.")
				print()

				print("Is this correct? <Y/N>")
	
				answer = input()
				for a in range(5): print()

				while answer != 'N' and answer != 'n' and answer != 'Y' and answer != 'y':
					print("Invalid response... Houndify recognized:")
					print(recognized_audio_string)
					print()
					print("Is this correct? <Y/N>")
					answer = input()
	
				if answer == 'Y' or answer == 'y': return recognized_audio_string



	def translate(self, audio_string):
		'''
		This method takes an audio_string (from listen_for_input method) and translates it to a list of words to be returned (and later passed to execute method.)
		'''
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

	def add_to_list(self, object, path = []):
		'''
		takes some object and a path list of objects to move through until the given object is placed in the list of the final object in the path list
		'''
		current_list = self._list
		for a in range(len(path)):
			for b in range(len(current_list)):
				if path[a] == current_list[b]._name:
					current_list = current_list[b]._list
					break
		current_list.append(object)

	def display(self, beginning = None, indent = ''):
		'''
		given object to begin iterating from (user should usually input database)
		iterate through each layer returning the names of each object
		'''
		if beginning == None: beginning = self

		for i in range(len(beginning._list)):
			print(indent + beginning._list[i]._name)
			if beginning._list[i]._list: self.display(beginning._list[i], indent+' ')
				
	def get_help(self):
		'''
		Return documentation on methods of all object_type objects in the database for User convenience.
		'''
		for i in range(len(self._list)):
			help(self._list[i]._list[i])
		

# Object Type Superclass, second layer

class object_type(database):
	#abstract class holding pointers to the actual objects
	def __init__(self, name, list_of_objects = []):
		'''
		Initialize a new object_type object with given name.
		'''
		database.__init__(self, list_of_objects, name)

	def create_object(self, object):
		'''
		Place a given object of object_type into object_type's list. Mandatory for execution.
		'''
		self._list.append(object)


# Object Types, third layer

class test_object(object_type):
	#example object type for testing, do not use
	def __init__(self, name = 'default'):
		self._name = name
		self._list = None

	def execute(self, command_list):
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


	example_database.begin()

	for i in range(5): print()
	print('Test help function.')
	print()

	example_database.get_help()