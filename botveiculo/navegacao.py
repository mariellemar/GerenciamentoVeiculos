from botcity.web import WebBot, By
#navegacao.py

class Navegacao():
    def __init__(self, bot:WebBot) -> None:
        self.bot = bot

    def clicar_elemento(self, xpath):
        elemento = self.bot.find_element(xpath, By.XPATH)
        if elemento:
            elemento.click()
            self.bot.wait(1000)
        
        
    def navegar_home(self, from_listagem=False):
        if from_listagem:
            self.clicar_elemento('/html/body/a[2]/button')
        else:
            self.clicar_elemento('/html/body/a/button')
    
    def navegar_alugar_carro(self):
        self.clicar_elemento('/html/body/ul/li[1]/a/button')
        
        
    def navegar_alugar_moto(self):
        self.clicar_elemento('/html/body/ul/li[2]/a/button')
        
    
    def navegar_listagem(self):
        self.clicar_elemento('/html/body/ul/li[3]/a/button')
        
        
    def navegar_adicionar(self):
        self.clicar_elemento('/html/body/a/button')