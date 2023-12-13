import random

class Bruxo:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.casa = Chapeu.escolha()

class Chapeu:

    CASAS = ["Grifinória", "Sonserina", "Lufa-Lufa", "Corvinal"]

    def escolha():
        return random.choice(Chapeu.CASAS)

class Professor(Bruxo):

    def __init__(self, nome: str, disciplina: str) -> None:
        super().__init__(nome)
        self.disciplina = disciplina

anderson = Professor("anderson", "diretor")
print(anderson.nome)
