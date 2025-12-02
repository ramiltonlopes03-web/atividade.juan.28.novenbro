# atividade.juan.28.novenbro
Implementação do principio de Herança
Modo de uso:
inicia pelo codigo menu.py
em ufc.py é onde fica os Conceitos de Herança Aplicados:

1. Classe Base (Superclasse)

EntidadeAcademica: Classe pai que contém atributos e métodos comuns

2. Classes Derivadas (Subclasses)

Curso → herda de EntidadeAcademica
Campus → herda de EntidadeAcademica
CursoGraduacao → herda de Curso
CursoPosGraduacao → herda de Curso

Principais Melhorias:

super(): Usado para chamar o construtor da classe pai
Sobrescrita de métodos: O método exibir_info() é sobrescrito em cada classe
Especialização: Criei subclasses específicas (Graduação e Pós-Graduação)
Reutilização de código: Atributos comuns ficam na classe base
Polimorfismo: Todas as classes podem usar exibir_info() de forma diferente
