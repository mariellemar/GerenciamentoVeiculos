from botcity.web import WebBot, By

class Aluguel():
    
    def __init__(self, bot:WebBot):
        self.bot = bot
        
        
    def alugar_carro_id(self, carro_id):
        xpath_button = f"//form[@action='/alugar/{carro_id}']/button"
        
        botao_alugar = self.bot.find_element(xpath_button, By.XPATH)
        botao_alugar.click()

        self.bot.wait(500)
        
    
    def alugar_moto_id(self, moto_id):
        xpath_button = f"//form[@action='/alugar/{moto_id}']/button"
        
        botao_alugar = self.bot.find_element(xpath_button, By.XPATH)
        botao_alugar.click()

        self.bot.wait(500)
        
        
    def preencher_campos(self, dias, desconto=None):
        
        self.bot.find_element("dias", By.ID).send_keys(dias)
        if desconto:
            self.bot.find_element("desconto").send_keys(desconto)
            
        self.bot.find_element('/html/body/form/input[3]', By.XPATH).click()
        
        self.bot.wait(2000)
        
    
    def confirmar_aluguel(self):
        self.bot.find_element('/html/body/form/input').click()
        
        
