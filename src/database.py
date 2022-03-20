import pandas

def users():
	df = pandas.DataFrame(data = {'username':['nemo', 'doris', 'merlin', 'turtle'], 'password':['123', '123', '123', '123'], 'subscription':['pro', 'basic', 'no-verified', 'pro']})
	df = df.astype(str)
	
	return df

def commands():
	commands_dict = {
		'-h': 'basic'
		,'count': 'basic'
		, 'count character': 'pro'
		, 'enumerate users': 'pro'
		}
	
	return commands_dict
