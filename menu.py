from ufc import Campus, CursoGraduacao, CursoPosGraduacao

campi = []


def menu():
    while True:
        print("\n===== Menu Principal =====")
        print("1. Adicionar Campus")
        print("2. Listar Campus")
        print("3. Gerenciar Campus")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Campus: ")
            cidade = input("Cidade (opcional): ")
            campi.append(Campus(nome, cidade))
            print(f"✓ Campus '{nome}' adicionado com sucesso!")

        elif escolha == "2":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                print("\n--- Lista de Campus ---")
                for i, campus in enumerate(campi):
                    print(f"{i + 1}. {campus.exibir_info()}")

        elif escolha == "3":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                for i, campus in enumerate(campi):
                    print(f"{i + 1}. {campus.nome}")
                idx = int(input("Escolha o número do Campus: ")) - 1
                if 0 <= idx < len(campi):
                    gerenciar_campus(campi[idx])
                else:
                    print("Campus inválido!")

        elif escolha == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")


def gerenciar_campus(campus):
    while True:
        print(f"\n--- Gerenciando Cursos do Campus {campus.nome} ---")
        print("1. Adicionar Curso de Graduação")
        print("2. Adicionar Curso de Pós-Graduação")
        print("3. Adicionar Curso Simples")
        print("4. Listar Cursos")
        print("5. Atualizar Curso")
        print("6. Remover Curso")
        print("7. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Curso de Graduação: ")
            carga = int(input("Carga horária (em horas): ") or 0)
            semestres = int(input("Duração em semestres: ") or 8)
            curso = CursoGraduacao(nome, carga, semestres)
            campus.cursos.append(curso)
            print(f"✓ Curso de Graduação '{nome}' adicionado!")

        elif escolha == "2":
            nome = input("Nome do Curso de Pós-Graduação: ")
            carga = int(input("Carga horária (em horas): ") or 0)
            print("Tipo: 1-Especialização | 2-Mestrado | 3-Doutorado")
            tipo_num = input("Escolha o tipo: ")
            tipos = {"1": "Especialização", "2": "Mestrado", "3": "Doutorado"}
            tipo = tipos.get(tipo_num, "Especialização")
            curso = CursoPosGraduacao(nome, carga, tipo)
            campus.cursos.append(curso)
            print(f"✓ Curso de Pós-Graduação '{nome}' adicionado!")

        elif escolha == "3":
            nome = input("Nome do Curso: ")
            campus.adicionar_curso(nome)
            print(f"✓ Curso '{nome}' adicionado!")

        elif escolha == "4":
            if not campus.cursos:
                print("Nenhum curso cadastrado neste campus.")
            else:
                print("\n--- Lista de Cursos ---")
                for i, curso in enumerate(campus.cursos):
                    print(f"{i + 1}. {curso.exibir_info()}")

        elif escolha == "5":
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
            else:
                for i, curso in enumerate(campus.cursos):
                    print(f"{i + 1}. {curso.nome}")
                idx = int(input("Qual curso atualizar? ")) - 1
                if 0 <= idx < len(campus.cursos):
                    novo_nome = input("Novo nome do Curso: ")
                    campus.atualizar_curso(idx, novo_nome)
                    print(f"✓ Curso atualizado!")
                else:
                    print("Curso inválido!")

        elif escolha == "6":
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
            else:
                for i, curso in enumerate(campus.cursos):
                    print(f"{i + 1}. {curso.nome}")
                idx = int(input("Qual curso remover? ")) - 1
                if 0 <= idx < len(campus.cursos):
                    nome_removido = campus.cursos[idx].nome
                    campus.remover_curso(idx)
                    print(f"✓ Curso '{nome_removido}' removido!")
                else:
                    print("Curso inválido!")

        elif escolha == "7":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()