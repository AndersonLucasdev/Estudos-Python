import json
from coordenador.coordenador import *
from aluno.aluno import *
from professor.professor import *
## copia do projeto SIGTUR com POO

# funções para json
def salvar_dicionarios(dicionario, nome_do_arquivo):
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)
        
def descarregar_dicionario(nome_arquivo):
    with open(f'{nome_arquivo}.json', 'r') as file:
        return json.load(file)

dicionario_turma = descarregar_dicionario('dicionario_turma')
dicionario_professor = descarregar_dicionario('dicionario_professor')
dicionario_aluno = descarregar_dicionario('dicionario_aluno')

def menu_principal():
    print("=-=" * 15)
    print(f"{'Menu Principal':^34}")
    print("=-=" * 15)
    print("[1] - Coordenador \n [2] - Professor \n [3] - Aluno \n [0] - Sair")
    print("Escolha uma opção: ")
    return input(">>> ").strip()

def main():
    while True:
        pass

if __name__ == "__main__":
    main()
    
