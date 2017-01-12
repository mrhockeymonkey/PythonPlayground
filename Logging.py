import logging

# Logging levels lowest to highest
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL

# You can optionally specify filename to log to file,otherwise it will log to console. 
logging.basicConfig(filename='MyLog.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

for i in range(0,5): 
	logging.debug('i is ' + str(i))
	print('Hello world')

logging.debug('End of program')