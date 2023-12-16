import random

class Hogwarts:
    pass

class Bruxo:

    PATRONOS = ["Lobo", "Dragão", "Cachorro", "Lepre"]

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.casa = Chapeu.escolha_casa()
        self.patrono = Bruxo.escolha_patronos()
    
    def escolha_patronos():
        return random.choice(Bruxo.PATRONOS)

class Chapeu:

    CASAS = ["Grifinória", "Sonserina", "Lufa-Lufa", "Corvinal"]

    def escolha_casa():
        return random.choice(Chapeu.CASAS)

class Aluno(Bruxo):

    def __init__(self, nome: str) -> None:
        pass


class Professor(Bruxo):

    def __init__(self, nome: str, disciplina: str) -> None:
        super().__init__(nome)
        self.disciplina = disciplina

anderson = Professor("anderson", "diretor")
print(anderson.nome)
