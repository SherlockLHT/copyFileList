host = 'ftp.pegatroncorp.com'
userName = 'FTP_Vendor476_RW'
password = '(3C16vGac'
current_path = 'D:\\log\\BQ'

def sendINFOToUI():
	info = {'path':'D:\\log','project':'BQ','file':'.filelist',
			'username':userName,'password':password,'host':host}
	return info