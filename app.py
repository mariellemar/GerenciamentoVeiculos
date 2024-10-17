from flask import Flask, render_template, request

app = Flask(__name__)


def ler_dados():
    with open('veiculos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    motocicletas = []
    carros = []
    for linha in linhas:
        id, modelo, ano, diaria, tipo, combustivel, cilindradas, alugado = linha.strip().split(',')
        
        if tipo == 'Motocicleta':
            
            motocicletas.append({
                'id' : id,
                'modelo' : modelo,
                'ano' : ano,
                'diaria' : diaria,
                'tipo' : tipo,
                'cilindradas' : cilindradas,
                'alugado': alugado == True
            })
            
        if tipo == 'Carro':
            
            carros.append({
                'id' : id,
                'modelo' : modelo,
                'ano' : ano,
                'diaria' : diaria,
                'tipo' : tipo,
                'combustivel' : combustivel,
                'alugado': alugado == True
            })
    
    return motocicletas, carros

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alugar_carros')
def alugar_carros():
    _, carros = ler_dados()
    return render_template('carro.html', carros=carros)


@app.route('/alugar_motocicletas')
def alugar_motocicletas():
    motocicletas, _ = ler_dados()
    return render_template('motocicleta.html', motocicletas=motocicletas)


@app.route('/listar_veiculos')
def listar_veiculos():
    motocicletas, carros = ler_dados()
    return render_template('veiculo.html', motocicletas=motocicletas, carros=carros)


@app.route('/alugar/<int:veiculo_id>', methods=['POST'])
def alugar_veiculo(veiculo_id):
    motocicletas, carros = ler_dados()
    
    with open('veiculos.txt', 'w') as arquivo:
        for moto in motocicletas:
            if int(moto['id']) == veiculo_id:
                moto['alugado'] = True
            arquivo.write(f"{moto['id']},{moto['modelo']},{moto['ano']},{moto['diaria']},Motocicleta,,{moto['cilindradas']},{moto['alugado']}\n")

        for carro in carros:
            if int(carro['id']) == veiculo_id:
                carro['alugado'] = True
            arquivo.write(f"{carro['id']},{carro['modelo']},{carro['ano']},{carro['diaria']},Carro,{carro['combustivel']},,{carro['alugado']}\n")

    return listar_veiculos()


if __name__ == '__main__':
    app.run()
    