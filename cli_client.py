import cmd
import socket
import colors

welcome_note =  '''Welcome to the cli_py client. Enter your commands in the command line.
To see the list of all commands type '\h' or 'help'

To see list of all commands, type '\?'
To see list of entered comands, type 'history'.
'''

client_specific_commands = ["", "\?", "history"]
server_commands = []

command_list =  {'\q': 'Disconnect from the server and quit cli_py client.',
				 '\?': 'List all commands supported in cli_py.',
				 'history': 'List all previously typed commands.'
				}


bcolors = colors.bcolors()

ip = "localhost"
port = 1999
buffer_size = 1024

class Console(cmd.Cmd):
	cli = None

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = "cli_py>"
		self.intro = welcome_note

	def set_cli(self, cli):
		self.cli = cli

	def emptyline(self):
		self.default("")

	def do_history(self, args):
		print self._history

	def preloop(self):
		cmd.Cmd.preloop(self)
		self._history = []
		self._locals = {}
		self._globals = {}

	def precmd(self, line):
		self._history += [line.strip()]
		return line

	def postcmd(self, stop, line):
		if line in client_specific_commands:
			return
		response = self.cli.Cli_check_response()
		if response == "\q":
			self.cli.set_finished(True)
			return -1
		else:
			print response

	def default(self, line):
		if line == "":
			return
		elif line == "\?":
			self.print_commands()
			return
		line = line.strip()
		self.cli.Cli_send_command(line)

	def print_commands(self):
		print bcolors.YELLOW + "Commands:"
		for k, v in command_list.iteritems():
			print bcolors.OKBLUE +  k + " - " + bcolors.OKGREEN + v + bcolors.ENDC
		print ""
		return


class Cli_client():
	sock = None
	finished = False

	def Cli_client_connect(self, ip, port, buffer_size):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, port))
		self.Cli_check_response()
		c = Console()
		c.set_cli(self)
		while self.finished != True:
			c.cmdloop()
		print "\nAKDB now exiting."

	def Cli_send_command(self, command):
		self.sock.send(command.strip())

	def Cli_check_response(self):
		return self.sock.recv(buffer_size)

	def set_finished(self, val):
		self.finished = val

	def get_finished(self):
		return self.finished

cli = Cli_client()

if __name__ == "__main__":
	cli.Cli_client_connect(ip, port, buffer_size)

