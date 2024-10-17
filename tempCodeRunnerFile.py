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