

class user_interface:
	def __init__(self):
		print('No implemented.')

class ssh_client:
	def connection(self, host, user, password):
		print('No implemented.')
	def command(self, request):
		print('No implemented.')

class file_manager:
	def get_view(self, source):
		file_list = []
		print('No implemented.')
		return file_list
	def command_copy(self, source, target):
		print('No implemented.')
	def command_move(self, source, target):
		print('No implemented.')
	def command_delete(self, target):
		print('No implemented.')
	def command_create_dir(self, target):
		print('No implemented.')

if __name__ == '__main__':
	print('Ok.')
