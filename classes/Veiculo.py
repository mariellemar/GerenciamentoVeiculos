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
    
    
    def __str__(self):
        return f'{self.modelo}, {self.ano} - Diaria: R${self.diaria:.2f}'
    
    
    def aluguel(self, dias: int, desconto=0, cupom=0):
        total = self.diaria * dias - desconto
        if cupom > 0:
            total -= cupom
        return total
    
    
    @classmethod
    def exibir_total(cls, veiculos: list):
        if cls.veiculos:
            print(f'{cls.veiculos} Veiculos Alugados: \n')
            for i, veiculo in enumerate(veiculos):
                print(f'{i+1} - {veiculo.__str__()}')
        else:
            print("Sem veiculos alugados")
            
    
    @classmethod
    def aumento(cls, veiculos: list, aumento: float):
        for veiculo in veiculos:
            valor = veiculo.diaria + aumento
            veiculo.diaria = valor
            