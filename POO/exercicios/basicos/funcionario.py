class funcionario():
    def __init__(self, nome: str, salario: float) -> None:
        self.nome = nome
        self.salario = salario
    
    def devolve_dinheiro(self):
        print(self.salario)
    
    def devolve_nome(self):
        print(self.nome)
    
    def devolve_tudo(self):
        print(f"Nome: {self.nome}\nSalario: {self.salario}")

anderson = funcionario('anderson', 1000.75)
anderson.devolve_nome()
anderson.devolve_dinheiro()
anderson.devolve_tudo()
