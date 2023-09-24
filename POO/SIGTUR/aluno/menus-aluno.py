def menu_aluno():
    print("=-=" * 15)
    print(f"{'Menu Aluno':^34}")
    print("=-=" * 15)
    print('[1] - Cadastrar novo aluno \n[2] - Editar aluno cadastrado \n[3] - Visualizar alunos cadastrados cadastrados \n[4] - Apagar aluno cadastrado \n[0] - Voltar')
    print("Escolha uma opção: ")
    return input(">>> ").strip()