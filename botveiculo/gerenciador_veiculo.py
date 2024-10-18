from botcity.web import WebBot, By
from botcity.web.util import element_as_select

class GerenciadorVeiculos():
    def __init__(self, bot:WebBot):
        self.bot = bot


    def ler_veiculos_inserir(self):
        # caminho = r"C:\Users\matutino\Desktop\COO com Python\GerenciamentoVeiculos\veiculos.txt"
        caminho = r"C:\Users\marie\OneDrive\Área de Trabalho\Projetos\GerenciamentoVeiculos\veiculos_inserir.txt"
        
        with open(caminho, 'r') as arquivo:
            veiculos = arquivo.readlines()
            veiculos = [linha.strip() for linha in veiculos]

            return veiculos
            

    def adicionar_veiculo(self, veiculo:str):
        partes = veiculo.split(',')

        modelo, ano, diaria, tipo, combustivel, cilindrada = partes
        self.selecionar_tipo(tipo)
        self.preencher_campos(modelo, ano, diaria, tipo, combustivel, cilindrada)
        self.confirmar_adicao()
    
    
    def selecionar_tipo(self, tipo:str):
        elemento_select_tipo = self.bot.find_element(selector='tipo_veiculo', by=By.ID)
        select_tipo = element_as_select(elemento_select_tipo)
        select_tipo.select_by_value(f'{tipo}')

        self.bot.wait(500)
        
        
    def preencher_campos(self, modelo:str, ano:str, diaria:str,
                         tipo:str, combustivel:str, cilindrada:str):

        campo_modelo = self.bot.find_element('//*[@id="modelo"]', By.XPATH).send_keys(modelo)
        self.bot.wait(500)

        campo_ano = self.bot.find_element('/html/body/form/input[2]', By.XPATH).send_keys(ano)
        self.bot.wait(500)

        campo_diaria = self.bot.find_element('/html/body/form/input[3]', By.XPATH).send_keys(diaria)
        self.bot.wait(500)

        if tipo == 'Carro':
            elemento_select_combustivel = self.bot.find_element(selector='combustivel', by=By.ID)
            select_tipo = element_as_select(elemento_select_combustivel)
            select_tipo.select_by_value(f'{combustivel}')

            self.bot.wait(500)

        else:
             campo_cilindrada = self.bot.find_element('//*[@id="cilindrada"]', By.XPATH).send_keys(cilindrada)
             self.bot.wait(500)


    def confirmar_adicao(self):
        self.bot.find_element('/html/body/form/input[5]', By.XPATH).click()
