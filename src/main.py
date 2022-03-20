import pandas
from database import users
from database import commands
from functions import validate_account
commands = commands()

def main():
	users_df = users()
	User = validate_account(users_df = users_df)

	if User != 'none':
		print(f'your subscription is {User.subscription}')
		cmd = 'cmd'
		while cmd != 'exit':
			cmd = str(input('Command:'))
			if User.subscription == 'no-verified':
				print('You are still not verified. You cannot use commands until you finish the verification')
			elif User.subscription == 'basic' and commands[cmd] == 'pro':
				print('Upgrade your version to use this command')
			else:
				User.execute_command(cmd)
			
		print('Thanks for using this tool')

	else:
		print('Please register and come back!')

if __name__ == '__main__':
	main()
