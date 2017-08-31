def nice(func):

	def wrapper():
		print('--- start ---')
		func()
		print('---  end  ---')

	return wrapper