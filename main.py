import func


biblioteca=func.carregar_dados()

while True:

    func.menu()

    try:

        op=int(input("Selecione uma das opções:"))

    except ValueError:

        print("Digite apena dados compátiveis")

        continue

    match op:

        case 1:

            try:

                escolha=int(input("Digite 1 para livro digital e Digite 2 para livro físico:"))

            except ValueError:

                func.mensagem_de_erro()
                continue

            if escolha == 1:

                if func.cadastrar_digital(biblioteca):
                    func.salvar_dados(biblioteca)
                    print("livro cadastado com sucesso")
                else:
                    print("Erro ao cadastrar livro")
                    continue

            if escolha == 2:
                if func.cadastrar_fisico(biblioteca):
                    func.salvar_dados(biblioteca)
                    print("Livro cadastrado com sucesso ")
                else:
                    print("Erro ao cadastrar livro")
                    continue
        case 2:

            try:

                busca_1=int(input("Digite o isbn do livro:"))

            except ValueError:
                func.mensagem_de_erro()
                continue

            if busca_1:

                encontrado_1=func.consultar_livro(biblioteca,busca_1)

                if encontrado_1:
                    encontrado_1.exibir()
            else:
                print("Erro ao consultar")
                continue



        case 3:

            try:

                busca_2 = int(input("Digite o isbn do livro:"))

            except ValueError:
                func.mensagem_de_erro()
                continue

            if busca_2:

                if func.remover_livro(biblioteca,busca_2):
                    func.salvar_dados(biblioteca)
                    print("livro removido")


        case 4:
            try:

                busca_3 = int(input("Digite o isbn do livro:"))

            except ValueError:
                func.mensagem_de_erro()
                continue

            if func.editar(biblioteca, busca_3):
                func.salvar_dados(biblioteca)
                print("Livro editado")

            else:

                print("Erro")
                continue

        case 5:
            func.listar_todos(biblioteca)

        case 6:
            print("Encerrando programa")
            func.salvar_dados(biblioteca)
            break