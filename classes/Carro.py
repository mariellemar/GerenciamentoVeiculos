from .Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo: str, ano: int,
                 diaria: float, combustivel: float):
        super().__init__(modelo, ano, diaria)
        self.__combustivel = combustivel
        
    
    @property
    def combustivel(self):
        return self.__combustivel
    
    @combustivel.setter
    def combustivel(self, novo_combustivel):
        self.__combustivel = novo_combustivel
        
    
    def __str__(self):
        return f'{super().__str__()} - Combustivel: {self.combustivel}'
    
    
    def aluguel(self, dias: int, desconto=0):
        if dias > 7:
            desconto = 70
        
        return super().aluguel(dias, desconto)