from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.web.util import element_as_select
from webdriver_manager.chrome import ChromeDriverManager

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def navegar_adicionar(bot:WebBot):
    bot.browse("http://127.0.0.1:5000")

    pagina_listagem = bot.find_element('/html/body/ul/li[3]/a/button', By.XPATH)
    pagina_listagem.click()

    bot.wait(1000)

    pagina_adicionar = bot.find_element('/html/body/a/button', By.XPATH)
    pagina_adicionar.click()



def ler_veiculos_inserir(bot:WebBot):
    caminho = r"C:\Users\matutino\Desktop\COO com Python\GerenciamentoVeiculos\veiculos.txt"
    with open(caminho, 'r') as arquivo:
        veiculos = arquivo.readlines()
        veiculos = [linha.strip() for linha in veiculos]

        return veiculos
            

def adicionar_veiculo(bot:WebBot, veiculo):
        partes = veiculo.split(',')

        modelo = partes[0]
        ano = partes[1]
        diaria = partes[2]
        tipo = partes[3]
        combustivel = partes [4]
        cilindrada = partes[5]

        elemento_select_tipo = bot.find_element(selector='tipo_veiculo', by=By.ID)
        select_tipo = element_as_select(elemento_select_tipo)
        select_tipo.select_by_value(f'{tipo}')

        bot.wait(500)

        campo_modelo = bot.find_element('//*[@id="modelo"]', By.XPATH)
        campo_modelo.click()
        campo_modelo.send_keys(modelo)

        bot.wait(500)

        campo_ano = bot.find_element('/html/body/form/input[2]', By.XPATH)
        campo_ano.click()
        campo_ano.send_keys(ano)

        bot.wait(500)

        campo_diaria = bot.find_element('/html/body/form/input[3]', By.XPATH)
        campo_diaria.click()
        campo_diaria.send_keys(diaria)

        bot.wait(500)

        if tipo == 'Carro':
            elemento_select_combustivel = bot.find_element(selector='combustivel', by=By.ID)
            select_tipo = element_as_select(elemento_select_combustivel)
            select_tipo.select_by_value(f'{combustivel}')

            bot.wait(500)

        else:
             campo_cilindrada = bot.find_element('//*[@id="cilindrada"]', By.XPATH)
             campo_cilindrada.click()
             campo_cilindrada.send_keys(cilindrada)

             bot.wait(500)

        botao_adicionar = bot.find_element('/html/body/form/input[5]', By.XPATH)
        botao_adicionar.click()


def navegar_alugar_carro(bot:WebBot):
     pass



def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager

    # Adicionar Veiculos

    navegar_adicionar(bot)
    veiculos = ler_veiculos_inserir(bot)
    for veiculo in veiculos:
            adicionar_veiculo(bot, veiculo)


    # Alugar Carro
    navegar_alugar_carro(bot)

    bot.wait(3000)

    bot.stop_browser()



def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
