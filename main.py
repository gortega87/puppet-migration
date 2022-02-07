import paramiko
import getpass
import time
import inventory


def cleanCa(id,username,password):
    try:
        ssh_ca = paramiko.SSHClient()
        ssh_ca.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_ca.connect('10.130.32.197', username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('sudo /opt/puppetlabs/bin/puppet cert clean '+id, get_pty= True)
        stdin.write(password + '\n')
        stdin.flush()
        time.sleep(3)
        ssh_ca.close()
        print('DELETING CERT ON CA')
        info = stdout.readlines()
        for msg in info:
            print(msg)
        print('Done')
        time.sleep(3)
    except Exception as err:
        print(err)



username = 'gastonortega'
password = getpass.getpass()
instance = inventory.Inventory.jarvis_account()
for data in instance:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(data['ip'], username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('sudo /opt/puppetlabs/bin/puppet agent -t', get_pty= True)
    stdin.write(password + '\n')
    stdin.flush()
    info = stdout.readlines()
    error = stderr.readlines()
    time.sleep(3)
    for msg in info:
        if 'To fix this,' in msg:
            cleanCa(data['id'], username, password)
    stdin_1, stdout_1, stderr_1 = ssh.exec_command('sudo find /etc/puppetlabs/puppet/ssl -name '+data['id']+'.pem -delete', get_pty= True)
    stdin_1.write(password + '\n')
    stdin_1.flush()
    time.sleep(2)
    print('______________________________'+'\n'+'DELETING CERT ON NODE')
    info = stdout_1.readlines()
    for msg in info:
        print(msg)
    print('______________________________'+'\n'+"RUNNING PUPPET AGENT")
    stdin_2, stdout_2, stderr_2 = ssh.exec_command('sudo /opt/puppetlabs/bin/puppet agent -t', get_pty=True)
    stdin_2.write(password + '\n')
    stdin_2.flush()
    info = stdout_2.readlines()
    for msg in info:
        print(msg)
    time.sleep(3)
    ssh.close()
