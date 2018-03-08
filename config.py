from configparser import SafeConfigParser



def getConfig(config_file='config.ini'):
	config = SafeConfigParser()
	config.read(config_file)
	return config
