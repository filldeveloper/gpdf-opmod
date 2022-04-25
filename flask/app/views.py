from app import app
from flask import render_template, request
from app.functions import *

@app.route('/')
def home():
    global lista_servicos, lista_meses, lista_anos, lista_clientes
    lista_servicos = servicos()
    lista_meses = meses()
    lista_anos = anos()
    lista_clientes = clientes()
    return render_template('index.html',
                            servicos=lista_servicos,
                            meses=lista_meses,
                            anos=lista_anos,
                            clientes=lista_clientes)

@app.route("/gerar_pdf", methods=['GET', 'POST'])
def gerar_pdf():
    input_data = list(request.form.values())
    servico = input_data[0]
    cliente = input_data[1]
    periodo = ciclo(input_data[2], input_data[3])
    data_ini = periodo[0]
    data_fim = periodo[1]
    path_env = '/root/scripts/relatorios/venv/bin/python3'
    path_script = '/root/scripts/relatorios/wan/relatorio_pdf.py'
    comando = f'{path_env} {path_script} {servico} {cliente} {data_ini} {data_fim}'

    # print(comando)
    # Chamar função que executa o script remotamente
    # Descomentar depois para gerar o PDF
    # ssh_command(comando)

    # Test
    mensagem = f'PDF {servico}/{cliente} gerado com sucesso!'
    return render_template('gerado.html',
                            texto_aviso=mensagem)

@app.route('/logout')
def logout():
    return render_template()