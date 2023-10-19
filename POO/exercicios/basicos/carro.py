class Car():
    def __init__(self, nome: str, velocidade: int):
        self.nome = nome
        self.velocidade = velocidade
    
    def mostrar_tudo(self):
        print(self.nome, self.velocidade)
    
    def acelerar(self, incremento):
        self.velocidade += incremento
    
    def freiar(self, incremento):
        self.velocidade -= incremento

carro = Car('corolla', 40)
carro.mostrar_tudo()
carro.freiar(10)
carro.mostrar_tudo()
carro.acelerar(20)
carro.mostrar_tudo()