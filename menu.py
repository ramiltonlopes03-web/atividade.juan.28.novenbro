from ufc import Campus, CursoGraduacao, CursoPosGraduacao, Curso

campi = []


def menu():
    while True:
        print("\n===== Menu Principal =====")
        print("1. Adicionar Campus")
        print("2. Listar Campus")
        print("3. Gerenciar Campus")
        print("4. Estatísticas (Verificação Dinâmica)")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            try:
                nome = input("Nome do Campus: ")
                cidade = input("Cidade (opcional): ")
                
                # VERIFICAÇÃO DINÂMICA: Valida antes de criar
                if not nome.strip():
                    print(" Nome do campus não pode ser vazio!")
                    continue
                
                campus = Campus(nome, cidade)
                campi.append(campus)
                print(f"✓ Campus '{nome}' adicionado com sucesso!")
                
            except (TypeError, ValueError) as e:
                print(f" Erro ao criar campus: {e}")

        elif escolha == "2":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                print("\n--- Lista de Campus ---")
                for i, campus in enumerate(campi):
                    # VERIFICAÇÃO DINÂMICA: Confirma que é realmente um Campus
                    if isinstance(campus, Campus):
                        print(f"{i + 1}. {campus.exibir_info()}")
                    else:
                        print(f"{i + 1}. ⚠ Objeto inválido: {type(campus).__name__}")

        elif escolha == "3":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                for i, campus in enumerate(campi):
                    print(f"{i + 1}. {campus.nome}")
                
                try:
                    idx = int(input("Escolha o número do Campus: ")) - 1
                    
                    # VERIFICAÇÃO DINÂMICA: Valida índice e tipo
                    if not 0 <= idx < len(campi):
                        print(" Campus inválido!")
                    elif not isinstance(campi[idx], Campus):
                        print(" Objeto não é um Campus válido!")
                    else:
                        gerenciar_campus(campi[idx])
                        
                except ValueError:
                    print(" Digite um número válido!")

        elif escolha == "4":
            exibir_estatisticas()

        elif escolha == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")


def gerenciar_campus(campus):
    """
    VERIFICAÇÃO DINÂMICA NO INÍCIO:
    Garante que estamos trabalhando com um objeto Campus válido
    """
    if not isinstance(campus, Campus):
        print(" Erro: objeto fornecido não é um Campus!")
        return
    
    while True:
        print(f"\n--- Gerenciando Cursos do Campus {campus.nome} ---")
        print("1. Adicionar Curso de Graduação")
        print("2. Adicionar Curso de Pós-Graduação")
        print("3. Adicionar Curso Simples")
        print("4. Listar Cursos")
        print("5. Atualizar Curso")
        print("6. Remover Curso")
        print("7. Filtrar por Tipo (Verificação Dinâmica)")
        print("8. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            try:
                nome = input("Nome do Curso de Graduação: ")
                if not nome.strip():
                    print(" Nome não pode ser vazio!")
                    continue
                
                # VERIFICAÇÃO DINÂMICA: Valida entrada antes de converter
                carga_input = input("Carga horária (em horas): ")
                carga = int(carga_input) if carga_input else 0
                
                semestres_input = input("Duração em semestres: ")
                semestres = int(semestres_input) if semestres_input else 8
                
                # Cria o curso (validações dinâmicas acontecem no construtor)
                curso = CursoGraduacao(nome, carga, semestres)
                
                # VERIFICAÇÃO DINÂMICA: Confirma tipo antes de adicionar
                if isinstance(curso, Curso):
                    campus.adicionar_curso(curso)
                else:
                    print(" Erro: objeto criado não é um Curso válido!")
                    
            except ValueError as e:
                print(f" Erro: valores numéricos inválidos! {e}")
            except (TypeError, Exception) as e:
                print(f" Erro ao criar curso: {e}")

        elif escolha == "2":
            try:
                nome = input("Nome do Curso de Pós-Graduação: ")
                if not nome.strip():
                    print(" Nome não pode ser vazio!")
                    continue
                
                carga_input = input("Carga horária (em horas): ")
                carga = int(carga_input) if carga_input else 0
                
                print("Tipo: 1-Especialização | 2-Mestrado | 3-Doutorado")
                tipo_num = input("Escolha o tipo: ")
                tipos = {"1": "Especialização", "2": "Mestrado", "3": "Doutorado"}
                tipo = tipos.get(tipo_num, "Especialização")
                
                curso = CursoPosGraduacao(nome, carga, tipo)
                
                # VERIFICAÇÃO DINÂMICA
                if isinstance(curso, Curso):
                    campus.adicionar_curso(curso)
                else:
                    print(" Erro: objeto criado não é um Curso válido!")
                    
            except ValueError:
                print(" Erro: carga horária deve ser um número!")
            except (TypeError, Exception) as e:
                print(f" Erro ao criar curso: {e}")

        elif escolha == "3":
            try:
                nome = input("Nome do Curso: ")
                if not nome.strip():
                    print(" Nome não pode ser vazio!")
                    continue
                
                carga_input = input("Carga horária (opcional): ")
                carga = int(carga_input) if carga_input else 0
                
                curso = Curso(nome, carga)
                campus.adicionar_curso(curso)
                
            except ValueError:
                print(" Erro: carga horária deve ser um número!")
            except (TypeError, Exception) as e:
                print(f" Erro ao criar curso: {e}")

        elif escolha == "4":
            if not campus.cursos:
                print("Nenhum curso cadastrado neste campus.")
            else:
                print("\n--- Lista de Cursos ---")
                for i, curso in enumerate(campus.cursos):
                    # VERIFICAÇÃO DINÂMICA: Mostra tipo real do objeto
                    tipo_classe = type(curso).__name__
                    print(f"{i + 1}. [{tipo_classe}] {curso.exibir_info()}")

        elif escolha == "5":
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
            else:
                for i, curso in enumerate(campus.cursos):
                    print(f"{i + 1}. {curso.nome}")
                
                try:
                    idx = int(input("Qual curso atualizar? ")) - 1
                    
                    if not 0 <= idx < len(campus.cursos):
                        print(" Curso inválido!")
                    else:
                        novo_nome = input("Novo nome do Curso: ")
                        if not novo_nome.strip():
                            print(" Nome não pode ser vazio!")
                            continue
                        
                        # Tenta atualizar (verificação dinâmica no método)
                        campus.atualizar_curso(idx, novo_nome)
                        print(f" Curso atualizado!")
                        
                except ValueError:
                    print(" Digite um número válido!")
                except (TypeError, IndexError) as e:
                    print(f" Erro ao atualizar: {e}")

        elif escolha == "6":
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
            else:
                for i, curso in enumerate(campus.cursos):
                    print(f"{i + 1}. {curso.nome}")
                
                try:
                    idx = int(input("Qual curso remover? ")) - 1
                    
                    if 0 <= idx < len(campus.cursos):
                        nome_removido = campus.cursos[idx].nome
                        campus.remover_curso(idx)
                        print(f" Curso '{nome_removido}' removido!")
                    else:
                        print(" Curso inválido!")
                        
                except ValueError:
                    print(" Digite um número válido!")
                except (TypeError, IndexError) as e:
                    print(f" Erro ao remover: {e}")

        elif escolha == "7":
            """
            DEMONSTRAÇÃO DE VERIFICAÇÃO DINÂMICA:
            Filtra cursos por tipo usando isinstance()
            """
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
            else:
                print("\n--- Filtrar por Tipo ---")
                print("1. Cursos de Graduação")
                print("2. Cursos de Pós-Graduação")
                print("3. Cursos Simples")
                
                filtro = input("Escolha o tipo: ")
                
                if filtro == "1":
                    cursos_filtrados = campus.listar_cursos_por_tipo(CursoGraduacao)
                    print("\n Cursos de Graduação:")
                elif filtro == "2":
                    cursos_filtrados = campus.listar_cursos_por_tipo(CursoPosGraduacao)
                    print("\n Cursos de Pós-Graduação:")
                elif filtro == "3":
                    # Filtra cursos que são Curso mas não são subclasses
                    cursos_filtrados = [c for c in campus.cursos 
                                       if type(c) == Curso]
                    print("\n Cursos Simples:")
                else:
                    print(" Opção inválida!")
                    continue
                
                if cursos_filtrados:
                    for c in cursos_filtrados:
                        print(f"  • {c.exibir_info()}")
                else:
                    print("  Nenhum curso deste tipo encontrado.")

        elif escolha == "8":
            break
        else:
            print("Opção inválida.")


def exibir_estatisticas():
    """
    DEMONSTRAÇÃO COMPLETA DE VERIFICAÇÃO DINÂMICA:
    Analisa todos os objetos e mostra estatísticas por tipo
    """
    print("\n=== ESTATÍSTICAS DO SISTEMA ===")
    print(f"Total de Campus: {len(campi)}")
    
    if not campi:
        print("Nenhum campus cadastrado.")
        return
    
    total_cursos = 0
    total_por_tipo = {}
    
    for campus in campi:
        # VERIFICAÇÃO DINÂMICA: Confirma tipo
        if not isinstance(campus, Campus):
            print(f" Aviso: objeto inválido detectado!")
            continue
        
        print(f"\n {campus.nome} ({campus.cidade or 'Sem cidade'})")
        print(f"   Total de cursos: {len(campus.cursos)}")
        
        # Usa o método com verificação dinâmica
        tipos_campus = campus.contar_cursos_por_tipo()
        
        for tipo, qtd in tipos_campus.items():
            print(f"   - {tipo}: {qtd}")
            total_por_tipo[tipo] = total_por_tipo.get(tipo, 0) + qtd
        
        total_cursos += len(campus.cursos)
        
        # VERIFICAÇÃO DINÂMICA DETALHADA: Mostra cada curso
        for i, curso in enumerate(campus.cursos, 1):
            tipo_real = type(curso).__name__
            # Verifica a hierarquia de herança
            eh_graduacao = isinstance(curso, CursoGraduacao)
            eh_pos = isinstance(curso, CursoPosGraduacao)
            eh_curso_base = isinstance(curso, Curso)
            
            print(f"      {i}. {curso.nome} [{tipo_real}]")
            if eh_graduacao:
                print(f"          É CursoGraduacao")
            elif eh_pos:
                print(f"          É CursoPosGraduacao")
            elif eh_curso_base:
                print(f"          É Curso base")
    
    print(f"\n RESUMO GERAL:")
    print(f"   Total de cursos no sistema: {total_cursos}")
    print(f"   Distribuição por tipo:")
    for tipo, qtd in total_por_tipo.items():
        print(f"   - {tipo}: {qtd}")


if __name__ == "__main__":
    menu()
