from paramiko import SSHClient, AutoAddPolicy

def ssh_command(comando):
    server = '10.31.19.111'
    username = 'root'
    password = 'serprospo'

    ssh = SSHClient()

    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(server, username=username, password=password, look_for_keys=False, timeout=0.5)

    # comando = 'python3 /root/scripts/relatorios/teste_ssh.py'
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(comando)
    output = ssh_stdout.readlines()
    return True

def meses():
    meses = [
        {'mes': 'Escolha o Mês'},
        {'mes': 'Janeiro'},
        {'mes': 'Fevereiro'},
        {'mes': 'Março'},
        {'mes': 'Abril'},
        {'mes': 'Maio'},
        {'mes': 'Junho'},
        {'mes': 'Julho'},
        {'mes': 'Agosto'},
        {'mes': 'Setembro'},
        {'mes': 'Outubro'},
        {'mes': 'Novembro'},
        {'mes': 'Dezembro'}
    ]
    return meses

def servicos():
    servicos = [
        {'nome': 'Escolha o Serviço'},
        {'nome': 'WAN'},
        {'nome': 'LAN'}
    ]
    return servicos

def anos():
    anos = [
        {'ano': 'Escolha o Ano'},
        {'ano': '2020'},
        {'ano': '2021'},
        {'ano': '2022'}
    ]
    return anos

def clientes():
    clientes = [
        {'cliente': 'Escolha o Cliente'},
        {'cliente': 'RFB'},
        {'cliente': 'PGFN'},
        {'cliente': 'DNIT'},
    ]
    return clientes

def ciclo(mes, ano):
    meses = {
        'Janeiro': 1,
        'Fevereiro': 2,
        'Março': 3,
        'Abril': 4,
        'Maio': 5,
        'Junho': 6,
        'Julho': 7,
        'Agosto': 8,
        'Setembro': 9,
        'Outubro': 10,
        'Novembro': 11,
        'Dezembro': 12
    }
    if int(meses[mes]) < 10:
        data_ini = f'11/0{meses[mes] - 1}/{ano}'
        data_fim = f'10/0{meses[mes]}/{ano}'
    elif int(meses[mes]) == 10:
        data_ini = f'11/0{meses[mes] - 1}/{ano}'
        data_fim = f'10/{meses[mes]}/{ano}'
    else:
        data_ini = f'11/{meses[mes] - 1}/{ano}'
        data_fim = f'10/{meses[mes]}/{ano}'
    return data_ini, data_fim
