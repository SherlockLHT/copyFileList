host = 'ftp.pegatroncorp.com'
userName = 'FTP_Vendor476_RW'
password = '(3C16vGac'
current_path = 'D:\\log\\QV2'

def sendINFOToUI():
	info = {'path':'D:\\log','project':'QV2','file':'.filelist',
			'username':userName,'password':password,'host':host}
	return info