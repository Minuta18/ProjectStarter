import abc

class Command:
	def __init__(self):
		...

	@abc.abstractmethod
	def help(self):
		raise NotImplementedError

	@abc.abstractmethod
	def version(self):
		raise NotImplementedError
	
	@abc.abstractmethod
	def run(self, args):
		raise NotImplementedError