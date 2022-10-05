class keyword():
	def __init__(self, command, ncommand=None, clist_head=None):
		self._command = command
		self._ncommand = ncommand
		self._clist_head = clist_head

	def check_command(self, input):
		return input == self._command

	def run(self):
		print("Hello! You're trying to run the command '"+self._command+"'!")
		print("Obviously, something has gone terribly wrong.")
		print("This is likely an abstraction error, but frankly you shouldn't be seeing this...")

class keyword_database():
	def __init__(self, keyword):
		self._head = keyword
	
	def read_command(self, input, node=None):
		if node==None: node=self._head
		while not node.check_command(input) and node._ncommand != None:
			node = node._ncommand
		if node.check_command(input): return node

	def execute_command(self, input_list, node=None):
		if node==None: node=self._head
		for i in range(len(input_list)):
			node = self.read_command(input_list[i], node)
			if i != len(input_list)-1: node = node._clist_head
			else: node.run()

		return node

	def display(self, node=None, indent=0):
		if node==None: node=self._head
		while node != None:
			string=""
			for i in range(indent): string+=" "
			string+=node._command
			print(string)
			if node._clist_head != None: self.display(node._clist_head, indent+1)
			node = node._ncommand

if __name__=="__main__":
	print("Testing Display method:")

	example_database = keyword_database(keyword('what', keyword('when', keyword('where',None, keyword('filea', keyword('fileb'))), keyword('appointment')), keyword('time', keyword('temperature', keyword('example')))))
	example_database._head._clist_head._clist_head = keyword('appointment')
	example_database.display()

	print()

	print("Testing Read Command method:")
	
	print(example_database.read_command("when")._command)

	print()

	print("Testing Execute Command method:")

	print(example_database.execute_command(['what','time','appointment'])._command)



























