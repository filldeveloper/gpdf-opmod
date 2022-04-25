from paramiko import SSHClient, AutoAddPolicy

def ssh_command(comando):
    server = '10.31.19.111'
    username = 'root'
    password = 'serprospo'

    ssh = SSHClient()

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(server, username=username, password=password, look_for_keys=False)

    # comando = 'python3 /root/scripts/relatorios/teste_ssh.py'
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comando)
    output = ssh_stdout.readlines()
    print(output)
    return True

ssh_command("python3 /root/scripts/relatorios/teste_ssh.py")