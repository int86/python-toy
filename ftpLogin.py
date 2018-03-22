# encoding: UTF-8
import ftplib

"""
登录Ftp服务器
"""

def ftpLogin(hostName,username,passwd):
	try:
		ftp = ftplib.FTP(hostName)
		ftp.login(username,passwd)
		print '\n[*]'+str(hostName)+':FTP login suceeded'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-]'+str(hostName)+':FTP login Failed'
		print e

if __name__ == '__main__':
	host = '0.0.0.0'
	user = 'anonymous'
	passwd = 'anonymous@domain.com'
	ftpLogin(host,user,passwd)
