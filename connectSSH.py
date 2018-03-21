# encoding: UTF-8
import pexpect
PROMPT = ['#','>>>', '>','\$']
def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def connect(user, host, password,port):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh '+'-p'+port+' '+user+'@'+host
    child = pexpect.spawn(connStr)
    try:
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '%s@%s\'s [P|p]assword:' % (user,host)])
    except:
        print "[-] Error Connecting"
        exit(0)
    if ret == 0:
        print '[-] Error Connecting'
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
    if ret== 0:
        print '[-] Error Connecting'
        return
    child.sendline(password)
    child.expect(PROMPT)
    if ret==0:
        print '[-] Error Connecting, maybe password error'
        exit(0)
    return child

def main():
    host = 'localhost'
    user = 'root'
    password=''
    port = '22'
    child = connect(user,host,password,port)
    send_command(child,'ls -la')

if __name__ == '__main__':
    main()
