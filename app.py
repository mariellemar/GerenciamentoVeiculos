from flask import Flask, render_template, request, redirect, url_for

import random

from classes.Veiculo import Veiculo
from classes.Carro import Carro
from classes.Motocicleta import Motocicleta

app = Flask(__name__)


def ler_dados():
    with open(r'C:\Users\marie\OneDrive\Área de Trabalho\Projetos\GerenciamentoVeiculos\veiculos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    motocicletas = []
    carros = []
    veiculos = []
    for linha in linhas:
        id, modelo, ano, diaria, tipo, combustivel, cilindradas, alugado = linha.strip().split(',')
        alugado_status = alugado == 'True'

        if tipo == 'Motocicleta':
            
            moto = Motocicleta(modelo, int(ano), float(diaria), int(cilindradas))
            motocicletas.append({'veiculo': moto, 'alugado': alugado_status, 'id': id})

        elif tipo == 'Carro':
            carro = Carro(modelo, int(ano), float(diaria), combustivel)
            carros.append({'veiculo': carro, 'alugado': alugado_status, 'id': id})
    
    veiculos.append({'veiculo': moto if tipo == 'Motocicleta' else carro, 'alugado': alugado_status, 'id': id})
    return veiculos, motocicletas, carros


def atualizar_status_veiculo(veiculo_id, alugado_status):
    with open(r'C:\Users\marie\OneDrive\Área de Trabalho\Projetos\GerenciamentoVeiculos\veiculos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    with open(r'C:\Users\marie\OneDrive\Área de Trabalho\Projetos\GerenciamentoVeiculos\veiculos.txt', 'w') as arquivo:
        for linha in linhas:
            id, modelo, ano, diaria, tipo, combustivel, cilindradas, alugado = linha.strip().split(',')
            if int(id) == veiculo_id:
                alugado = 'True' if alugado_status else 'False'
            arquivo.write(f'{id},{modelo},{ano},{diaria},{tipo},{combustivel},{cilindradas},{alugado}\n')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alugar_carros')
def alugar_carros():
    _, _, carros = ler_dados()
    return render_template('carro.html', carros=carros)


@app.route('/alugar_motocicletas')
def alugar_motocicletas():
    _, motocicletas, _ = ler_dados()
    return render_template('motocicleta.html', motocicletas=motocicletas)


@app.route('/listar_veiculos')
def listar_veiculos():
    _, motocicletas, carros = ler_dados()
    for carro in carros:
        carro['diaria_formatada'] = f"{carro['veiculo'].diaria:.2f}"
        
    for moto in motocicletas:
        moto['diaria_formatada'] = f"{moto['veiculo'].diaria:.2f}"
    return render_template('veiculo.html', motocicletas=motocicletas, carros=carros)


@app.route('/calculo_diaria/<int:veiculo_id>', methods=['GET', 'POST'])
def calculo_diaria(veiculo_id):
    _, motocicletas, carros = ler_dados()

    veiculo_dict = next((vc for vc in motocicletas + carros if int(vc['id']) == veiculo_id), None)

    if request.method == 'POST':
        dias = int(request.form.get('dias', '0'))
        desconto_str = request.form.get('desconto', '').strip()

        desconto = float(desconto_str) if desconto_str else 0.0

        if veiculo_dict:
            veiculo = veiculo_dict['veiculo']

            total = veiculo.aluguel(dias=dias, desconto=desconto)
            atualizar_status_veiculo(veiculo_id, alugado_status=True)

            return render_template('confirmacao.html', veiculo=veiculo, dias=dias, desconto=desconto, total=total)

    return render_template('calculo_diaria.html', veiculo_id=veiculo_id, veiculo_dict=veiculo_dict)


@app.route('/alugar/<int:veiculo_id>', methods=['POST'])
def alugar_veiculo(veiculo_id):
    _, motocicletas, carros = ler_dados()
    
    veiculo_dict = next((vc for vc in motocicletas + carros if int(vc['id']) == veiculo_id), None)

    if veiculo_dict and not veiculo_dict['alugado']:
        return redirect(url_for('calculo_diaria', veiculo_id=veiculo_id))
    else:
        return redirect(url_for('index'))
    
def gerar_id_unico():
    veiculos, _, _ = ler_dados()
    veiculos_existentes = {veiculo['id'] for veiculo in veiculos}
    novo_id = random.randint(100, 999)
    while novo_id in veiculos_existentes:
        novo_id = random.randint(100, 999)
    return novo_id

@app.route('/adicionar_veiculo', methods=['GET', 'POST'])
def adicionar_veiculo():
    if request.method == 'POST':
        tipo_veiculo = request.form['tipo_veiculo']

        modelo = request.form['modelo']
        ano = request.form['ano']
        diaria = request.form['diaria']

        if tipo_veiculo == 'Motocicleta':
            cilindrada = request.form['cilindrada']
            combustivel = None
        else:
            combustivel =  request.form['combustivel']
            cilindrada = None

        novo_id = gerar_id_unico()

        with open(r'C:\Users\marie\OneDrive\Área de Trabalho\Projetos\GerenciamentoVeiculos\veiculos.txt', 'a') as arquivo:  # Use 'a' to append
            if tipo_veiculo == 'moto':
                arquivo.write(f'{novo_id},{modelo},{ano},{diaria},Motocicleta,,{cilindrada},False\n')
            else:
                arquivo.write(f'{novo_id},{modelo},{ano},{diaria},Carro,{combustivel},,False\n')

        return redirect(url_for('listar_veiculos'))
    return render_template('adicionar_veiculo.html')
        
if __name__ == '__main__':
    app.run()
    