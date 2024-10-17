class Veiculo():
    veiculos = 0
    
    def __init__(self, modelo: str, ano:int, diaria: float):
        self.__modelo = modelo
        self.__ano = ano
        self.__diaria = diaria
        Veiculo.veiculos += 1
        
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo 
    
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano (self, novo_ano):
        self.__ano = novo_ano
        
        
    @property
    def diaria(self):
        return self.__diaria
    
    @diaria.setter
    def diaria(self, nova_diaria):
        self.__diaria = nova_diaria       
        