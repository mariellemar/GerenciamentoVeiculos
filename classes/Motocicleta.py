from .Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo: str, ano: int,
                 diaria: float, cilindrada: int):
        super().__init__(modelo, ano, diaria)
        self.__cilindrada = cilindrada
        
    
    @property
    def cilindrada(self):
        return self.__cilindrada
    
    @cilindrada.setter
    def cilindrada(self, nova_cilindrada):
        self.__cilindrada = nova_cilindrada
        
    
    def __str__(self):
        return f'{super().__str__()} - Cilindrada: {self.cilindrada}'
    
    
    def aluguel(self, dias: int, desconto=0):
        if self.cilindrada >= 200:
            self.diaria += 20
        
        return super().aluguel(dias, desconto)