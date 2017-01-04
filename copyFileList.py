import ftplib
import myLogging
import logging
import os

host = 'ftp.pegatroncorp.com'
userName = 'FTP_Vendor476_RW'
password = '(3C16vGac'
current_path = 'D:\\log\\BQ'

def loginFTP():
	try:
		myLogging.logSetting()
		ftps = ftplib.FTP(host, timeout=20)
		ftps.set_debuglevel(0)
		ftps.login(userName, password)
		logging.info('Login FTP pass')
	except Exception as e:
		logging.error(e)
		logging.error('Login FTP fail')
		print e
		raise e
	finally:
		return ftps

def logoutFTP(ftps):
	try:
		if ftps:
			ftps.quit()
			logging.info('Logout FTP pass')
	except Exception as e:
		logging.error(e)
		logging.info('Logout FTP fail')
		print e
		raise e
	finally:
		pass

def getLocalFile(ftps,path):
	try:
		line = ''
		project = ''
		buildStage = ''
		stationName = ''
		all_file = os.listdir(path)
		for file in all_file:
			file = os.path.join(path,file)
			if os.path.isdir(file):
				getLocalFile(ftps,file)
			elif '.filelist' == os.path.splitext(file)[1]:
				argv = file.split('\\')
				if 6 < len(argv):
					line = argv[6]
				if 4 < len(argv):
					stationName = argv[4]
				if 3 < len(argv):
					buildStage = argv[3]
				if 2 < len(argv):
					project = argv[2]
				upLoad(ftps,file,line=line,project=project,buildStage=buildStage,stationName=stationName)
	except Exception as e:
		logging.error(e)
		print e
		raise e
	finally:
		pass

def upLoad(ftps,filePath,line='',project='',buildStage='',stationName=''):
	try:
		path = '\\'
		path = os.path.join(path,project)
		current = ftps.pwd().replace('/','\\')
		if not path == current:
			dirDeal(ftps,path)

		path = os.path.join(path, buildStage,)
		current = ftps.pwd().replace('/', '\\')
		if not path == current:
			dirDeal(ftps, path)

		path = os.path.join(path, 'Log_Filelist',)
		current = ftps.pwd().replace('/', '\\')
		if not path == current:
			dirDeal(ftps, path)

		path = os.path.join(path, line)
		current = ftps.pwd().replace('/', '\\')
		if not path == current:
			dirDeal(ftps, path)

		path = os.path.join(path, stationName)
		current = ftps.pwd().replace('/', '\\')
		if not path == current:
			dirDeal(ftps, path)

		logging.info('getin FTP path:%s' % path)
		file_list = ftps.nlst()
		file_name = os.path.split(filePath)[1]
		if not file_name in file_list:
			ftps.storbinary('STOR ' + file_name,open(filePath,'rb'))
			logging.info('upload file: %s pass' % file_name)
	except Exception as e:
		logging.error(filePath)
		logging.error(e)
		print e
		raise e
	finally:
		pass

def downLoad():
	try:
		ftps = ftplib.FTP(host,timeout=20)
		ftps.set_debuglevel(5)
		ftps.login(userName, password)
		#print ftps.getwelcome()
		logging.info(ftps.getwelcome())

		ftps.cwd('\\QV2\\EVT2\\Log_Filelist')
		list = ftps.nlst()
		print list
		#ftps.retrbinary('RETR %s' % file,open(file,'wb').write,2048)
		ftps.set_debuglevel(0)
	except Exception as e:
		logging.error(e)
		print(e)
		raise e
	finally:
		ftps.quit()

def dirDeal(ftps,path):
	try:
		ftps.cwd(path)
	except Exception as e:
		logging.info('Cannot find path,create now,error code:%s' % e)
		try:
			ftps.mkd(path)
			ftps.cwd(path)
		except Exception as e:
			logging.error(e)
			print e
			raise e
		finally:
			pass
	finally:
		pass

def main():
	ftps = loginFTP()
	getLocalFile(ftps, current_path)
	logoutFTP(ftps)


if __name__ == '__main__':
	main()