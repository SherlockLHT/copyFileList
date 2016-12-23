import logging
import time
import os

def logSetting():
	try:
		current_path = os.getcwd()
		current_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
		current_time = current_time + '_myLog.log'
		LOG_FILE = os.path.join(current_path, 'log')
		if not os.path.exists(LOG_FILE):
			os.mkdir(LOG_FILE)
		LOG_FILE = os.path.join(LOG_FILE, current_time)
		logging.basicConfig(level=logging.DEBUG,
							format='[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s :%(message)s',
							datefmt='%Y-%m-%d %H:%M:%S',
							filename=LOG_FILE)
	except Exception as e:
		print e
		raise e
	finally:
		pass