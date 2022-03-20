	
class User:
	def __init__(self, username, password, subscription):
		self.username = username
		self.password = password
		self.subscription = subscription
		
	def execute_command(self, cmd):
		def help():
			from database import commands
			com = commands()
			for key in com:
				print(key, ' -- ', com[key])
				
		def count(): 
			string = str(input('String:'))
			count = len(string)
			print(f'The given string has {count} characteres')
			
		def count_character():
			string = str(input('String:'))
			char = str(input('Character to count:'))
			count = string.count(char)
			print(f''''{char}' appears {count} times in the given string''')
			
		def enumerate_users():
			from database import users
			df = users()
			print(f'The users registered are: {df}')
		
		if cmd == '-h':
			help()
		elif cmd == 'count':
			count()
		elif cmd == 'count character':
			count_character()
		elif cmd == 'enumerate users':
			enumerate_users()
		else:
			print(f'''The command '{cmd}' does not exists''')
