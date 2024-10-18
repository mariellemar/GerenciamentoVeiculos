from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

import random

from navegacao import Navegacao
from gerenciador_veiculo import GerenciadorVeiculos
from aluguel import Aluguel

BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("http://127.0.0.1:5000")
    
    # caminho = r"C:\Users\matutino\Desktop\COO com Python\GerenciamentoVeiculos\veiculos.txt"
    caminho = r"C:\Users\marie\OneDrive\Área de Trabalho\Projetos\GerenciamentoVeiculos\veiculos_inserir.txt"
        
    navegacao = Navegacao(bot)
    gerenciador = GerenciadorVeiculos(bot)
    aluguel = Aluguel(bot)
    
    
    # # Adicionar Veiculos
    bot.wait(1000)
    navegacao.navegar_listagem()
    veiculos = gerenciador.ler_veiculos_inserir()
    for i in range(len(veiculos)):
        for veiculo in veiculos:
            navegacao.navegar_adicionar()
            gerenciador.adicionar_veiculo(veiculo)
            bot.wait(500)
        break
    

    # Alugar Carro
    
    bot.browse("http://127.0.0.1:5000")
    bot.wait(1000)
    navegacao.navegar_alugar_carro()
    
    carros_teste = ['774', '400']
    dias_desconto_carros = [[21], [6, 30]]
    
    for i in range(len(dias_desconto_carros)):
        
        id_carro = carros_teste[i]
        aluguel.alugar_carro_id(id_carro)
        
        if len(dias_desconto_carros[i]) == 2:
            aluguel.preencher_campos(dias_desconto_carros[i][0], dias_desconto_carros[i][1])
        else:
            aluguel.preencher_campos(dias_desconto_carros[i][0])
            
        aluguel.confirmar_aluguel()
        navegacao.navegar_alugar_carro()
    
    # Alugar Moto

    navegacao.navegar_home()
    navegacao.navegar_alugar_moto()
    
    motos_teste = ['712', '229']
    dias_desconto_motos = [[9], [14, 45]]
    
    for i in range(len(dias_desconto_motos)):
        id_moto = motos_teste[i]
        aluguel.alugar_moto_id(id_moto)
        
        if len(dias_desconto_motos[i]) == 2:
            aluguel.preencher_campos(dias_desconto_motos[i][0], dias_desconto_motos[i][1])
        else:
            aluguel.preencher_campos(dias_desconto_motos[i][0])
            
        aluguel.confirmar_aluguel()
        navegacao.navegar_alugar_moto()
    
    navegacao.navegar_home()
    navegacao.navegar_listagem()
    
    bot.wait(3000)

    bot.stop_browser()



def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
