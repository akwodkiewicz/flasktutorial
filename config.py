class Config(object):
	"""
	Common configurations
	"""
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
	"""
	Development configurations
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True
	EXPLAIN_TEMPLATE_LOADING = True


class ProdConfig(Config):
	"""
	Production configurations
	"""

	DEBUG = False

	
app_config = {
	'development': DevConfig,
	'production': ProdConfig
}
