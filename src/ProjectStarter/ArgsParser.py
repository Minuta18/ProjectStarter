class ArgParser:
	def __init__(self):
		self._search_args = dict()
		self._search_kwargs = dict()
	
	def search_arg(self, arg: str = ..., is_flag: bool = False, default_value = None):
		if is_flag:
			self._search_args[arg] = False
		else:
			self._search_kwargs[arg] = default_value

	def parse(self, args: list[str] = ...) -> dict:
		try:
			result = dict()

			for arg in self._search_args.keys():
				for i, a in enumerate(args):
					print(a, arg)
					if a == arg:
						result[a] = True
						args.pop(i)
				else:
					result[arg] = False
     
			for kwarg in self._search_kwargs.keys():
				for i, arg in enumerate(args):
					if arg == kwarg:
						if not args[i + 1].startswith('-'):
							result[arg] = arg[i + 1]
						else:
							raise ValueError('Unable to parse argument')
						break
				else:
					result[kwarg] = self._search_kwargs[kwarg]
     
			return result
		except IndexError:
			raise ValueError('Unable to parse arguments')