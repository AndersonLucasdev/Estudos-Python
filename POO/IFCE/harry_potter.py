import random

class Hogwarts:

    def __init__(self) -> None:
        self.alunos = []
        self.professores = []
    
    def matricular_aluno(self, aluno) -> None:
        self.alunos.append(aluno)
        print(f"{aluno.nome} matriculado em Hogwarts!")

    def contratar_professor(self, professor) -> None:
        self.professores.append(professor)
        print(f"{professor.nome} contratado para lecionar em Hogwarts!")
    
    def listar_alunos(self) -> None:
        print(f"Alunos em {self.nome_escola}:")
        for aluno in self.alunos:
            print(f"- {aluno.nome}")

class Bruxo:

    PATRONOS = ["Lobo", "Dragão", "Cachorro", "Lepre"]

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.casa = Chapeu.escolha_casa()
        self.patrono = Bruxo.escolha_patronos()
    
    @staticmethod
    def escolha_patronos():
        return random.choice(Bruxo.PATRONOS)

class Chapeu:

    CASAS = ["Grifinória", "Sonserina", "Lufa-Lufa", "Corvinal"]

    @staticmethod
    def escolha_casa():
        return random.choice(Chapeu.CASAS)

class Aluno(Bruxo):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.disciplinas = {}
        self.notas = {}

    def adicionar_disciplina(self, disciplina, professor) -> None:
        self.disciplinas[disciplina] = professor
        self.notas[disciplina] = []

    def listar_disciplinas(self) -> None:
        print(f"Disciplinas de {self.nome}:")
        for disciplina, professor in self.disciplinas.items():
            print(f"- {disciplina} com Professor {professor.nome}")

class Aluno(Bruxo):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina) -> None:
        self.disciplinas.append(disciplina)
        print(f"{self.nome} adicionou a disciplina: {disciplina}")

    def listar_disciplinas(self) -> None:
        print(f"Disciplinas de {self.nome}: {', '.join(self.disciplinas)}")

class Professor(Bruxo):

    def __init__(self, nome: str, disciplina: str) -> None:
        super().__init__(nome)
        self.disciplina = disciplina

anderson = Professor("anderson", "diretor")
print(anderson.nome)
