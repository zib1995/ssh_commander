
import paramiko

class user_interface:
	def __init__(self):
		print('No implemented.')

class remote_host:
	def __init__(self):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	def connection(self, host, user, secret, port = 22):
		self.client.connect(hostname = host, username = user, password = secret, port = port)
		self.transport = paramiko.Transport((host, port))
		self.transport.connect(username = user, password = secret)
		self.sftp = paramiko.SFTPClient.from_transport(self.transport)
	def command(self, request):
		stdin, stdout, stderr = self.client.exec_command(request)
		data = stdout.read() + stderr.read()
		return data
	def get_file(self, remotepath, localpath):
		sftp.get(remotepath, localpath)
	def put_file(self, remotepath, localpath):
		sftp.put(remotepath, localpath)
	def disconnection(self):
		self.sftp.close()
		self.transport.close()
		self.client.close()

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

	#Test host:

	host = '192.168.33.33'
	user = 'vagrant'
	secret = 'vagrant'
	port = 22
	
	target_host = remote_host()
	target_host.connection(host, user, secret)
	print(target_host.command('pwd'))
	target_host.disconnection()
	

	print('Ok.')
