
import sys
import paramiko
import threading
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import dialog_connection
import main_window
import time

class UserInterface:
	def __init__(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.MainWindow = QtWidgets.QMainWindow()
		self.ui_main_window = main_window.Ui_MainWindow()
		self.ui_main_window.setupUi(self.MainWindow)
		self.ui_main_window.statusbar.showMessage('Start.')
		self.define_reactions()
		self.MainWindow.show()
		self.reaction_to_menu_connect()
		self.command = ''

	def start(self):
		sys.exit(self.app.exec_())

	def get_terminal(self):
		return self.ui_main_window.textEdit_terminal

	def define_reactions(self):
		self.ui_main_window.actionConnect.triggered.connect(self.reaction_to_menu_connect)
		self.ui_main_window.actionQuit.triggered.connect(self.app.quit)
		self.ui_main_window.textEdit_terminal.cursorPositionChanged.connect(self.reaction_to_enter)

	def reaction_to_menu_connect(self):
		self.DialogConnection = QtWidgets.QDialog()
		self.ui_dialog_connection = dialog_connection.Ui_Dialog_connection()
		self.ui_dialog_connection.setupUi(self.DialogConnection)
		self.ui_dialog_connection.pushButton_connect.clicked.connect(self.reaction_to_dialog_connection_connect)
		self.ui_dialog_connection.pushButton_cancel.clicked.connect(self.DialogConnection.close)
		self.DialogConnection.exec_()

	def reaction_to_dialog_connection_connect(self):
		host = self.ui_dialog_connection.lineEdit_host.text()
		user = self.ui_dialog_connection.lineEdit_user.text()
		secret = self.ui_dialog_connection.lineEdit_password.text()

		self.target_host = RemoteHost(terminal = self.get_terminal())

		# Test host:
		#host = '192.168.33.33'
		#user = 'vagrant'
		#secret = 'vagrant'

		self.target_host.connection(host, user, secret)
		self.target_host.command_shell()
		#target_host.disconnection()

		self.DialogConnection.close()

	def reaction_to_enter(self):
		text = self.ui_main_window.textEdit_terminal.toPlainText()
		line = text.split('\n')[-1]
		#print(line)
		if line == '':
			command = self.command.split('$')[1]
			self.target_host.shell.send(command + '\n')
		self.command = line




class RemoteHost:
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
		#self.command_shell_thread = threading.Thread(target = self.commands)
		self.shell_output_thread = threading.Thread(target = self.shell_output)
		#self.command_shell_thread.daemon = True
		self.shell_output_thread.daemon = True
		#self.command_shell_thread.start()
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
			#print(data_text, end = '')
			if data_text != '':
				self.terminal.append(data_text)
				time.sleep(1)

	def get_file(self, remotepath, localpath):
		self.sftp.get(remotepath, localpath)
	def put_file(self, remotepath, localpath):
		self.sftp.put(remotepath, localpath)
	def disconnection(self):
		self.sftp.close()
		self.transport.close()
		self.client.close()

class FileManager:
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
	user_interface = UserInterface()
	user_interface.start()
