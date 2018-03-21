# encoding: UTF-8
from pexpect import pxssh

"""
构建一个ssh网络
依赖库：pexpect
"""

def send_cmd(s,cmd):
	s.sendline(cmd)
	s.prompt()
	print s.before

def connect(host,user,passwd,p):
	try:
		s = pxssh.pxssh()
		s.login(host,user,passwd,port=p)
		return s
	except:
		print '[-] Error connecting'
		exit(0)


if __name__ == '__main__':
	host = 'localhost'
	user = 'root'
	passwd = ''
	port = '22'
	s = connect(host,user,passwd,port)
	send_cmd(s,'ls -la')

