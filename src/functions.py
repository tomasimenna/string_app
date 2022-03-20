from classes import User

def validate_account(users_df):
	
	def validate_username(username):
		if username in users_df['username'].to_list():
			return 'ok'
		else:
			return 'nok'

	def validate_password(username, password):
		if password == users_df.loc[users_df['username'] == username, 'password'].iloc[0]:
			return 'ok'
		else:
			return 'nok'
			
	username = str(input('Username:'))
	
	if validate_username(username = username) == 'ok':
		password = str(input('Password:'))
		if validate_password(username = username, password = password) == 'ok':			
			credentials = {
			'username': username
			, 'password': password
			, 'subscription': str(users_df.loc[users_df['username'] == username, 'subscription'].iloc[0])
			}
			user = User(username = credentials['username'], password = credentials['password'], subscription = credentials['subscription'])
			print('Welcome! you can now execute commands.')
			
			return user
		else:
			print('Password is incorrect!')
			
			return 'none'
	else:
		print('The username does not exists in our database')
		
		return 'none'
