def menu_coordenador():
    print("=-=" * 15)
    print(f"{'Menu Principal':^34}")
    print("=-=" * 15)
    print('[1] - Criar turma \n[2] - Editar turma \n[3] - Ver turma \n[4] - Ver todas as turmas \n[5] - Apagar turma \n[0] - Voltar')
    print("Escolha uma opção: ")
    return input(">>> ").strip()