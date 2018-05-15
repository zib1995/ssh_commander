
import sys
import paramiko
import threading
from PyQt5 import QtWidgets
import dialog_connection
import main_window
import time

class user_interface:
	def __init__(self):
		print('No implemented.')

class remote_host:
	def __init__(self, terminal):
		self.client = paramiko.SSHClient()
		self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.terminal = terminal
		
	def connection(self, host, user, secret, port = 22):
		self.client.connect(hostname = host, username = user, password = secret, port = port)
		self.transport = paramiko.Transport((host, port))
		self.transport.connect(username = user, password = secret)
		self.sftp = paramiko.SFTPClient.from_transport(self.transport)
		
		self.shell = self.client.invoke_shell()
		self.continue_shell_session = True
		self.terminal.append('The connection to host ' + host + ' is established.')
		
	def command(self, request):
		stdin, stdout, stderr = self.client.exec_command(request)
		data = stdout.read() + stderr.read()
		data = data.decode('utf-8')
		return data

	def command_shell(self):
		self.command_shell_thread = threading.Thread(target = self.commands)
		self.shell_output_thread = threading.Thread(target = self.shell_output)
		self.command_shell_thread.daemon = True
		self.shell_output_thread.daemon = True
		self.command_shell_thread.start()
		self.shell_output_thread.start()

	def commands(self):
		while self.continue_shell_session:
			cmd = input()
			self.shell.send(cmd + '\n')
			
	def shell_output(self):
		while self.continue_shell_session:
			data = bytes()
			while self.shell.recv_ready():
				data += self.shell.recv(1024)
			data_text = data.decode('utf-8')[:-1]
			print(data_text, end = '')
			if data_text != '':
				self.terminal.append(data_text)
				time.sleep(1)

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
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui_main_window = main_window.Ui_MainWindow()
	ui_main_window.setupUi(MainWindow)
	MainWindow.show()

	#Test host:

	host = '192.168.33.33'
	user = 'vagrant'
	secret = 'vagrant'
	port = 22

	target_host = remote_host(terminal = ui_main_window.textEdit_terminal)

	target_host.connection(host, user, secret)
	
	target_host.command_shell()
	#target_host.disconnection()

	print('Ok.')
	sys.exit(app.exec_())
