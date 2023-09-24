def menu_professor():
    print("=-=" * 15)
    print(f"{'Menu Professor':^34}")
    print("=-=" * 15)
    print('[1] - Cadastrar novo professor\n[2] - Editar professor cadastrado \n[3] - Ver dados de um professor cadastrado \n[4] - Excluir um professor cadastrado \n[5] - Visualizar as turmas de um professor específico \n[6] - Visualizar os alunos da turma de um professor específico \n[0] - Voltar')
    print("Escolha uma opção: ")
    return input(">>> ").strip()