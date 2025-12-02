# Classe base (superclasse)
class EntidadeAcademica:
    """Classe base para entidades acadêmicas"""

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def exibir_info(self):
        return f"{self.__class__.__name__}: {self.nome}"


# Classe Curso herda de EntidadeAcademica
class Curso(EntidadeAcademica):
    def __init__(self, nome, carga_horaria=0):
        super().__init__(nome)  # Chama o construtor da classe pai
        self.carga_horaria = carga_horaria

    def exibir_info(self):
        """Sobrescreve o método da classe pai"""
        info = super().exibir_info()
        if self.carga_horaria > 0:
            info += f" - Carga Horária: {self.carga_horaria}h"
        return info


# Classe Campus também herda de EntidadeAcademica
class Campus(EntidadeAcademica):
    def __init__(self, nome, cidade=""):
        super().__init__(nome)
        self.cidade = cidade
        self.cursos = []

    def adicionar_curso(self, nome_curso, carga_horaria=0):
        self.cursos.append(Curso(nome_curso, carga_horaria))

    def listar_cursos(self):
        return [curso.nome for curso in self.cursos]

    def atualizar_curso(self, indice, novo_nome, nova_carga=None):
        if 0 <= indice < len(self.cursos):
            self.cursos[indice].nome = novo_nome
            if nova_carga is not None:
                self.cursos[indice].carga_horaria = nova_carga

    def remover_curso(self, indice):
        if 0 <= indice < len(self.cursos):
            del self.cursos[indice]

    def exibir_info(self):
        """Sobrescreve o método da classe pai"""
        info = super().exibir_info()
        if self.cidade:
            info += f" - Cidade: {self.cidade}"
        info += f" - Total de Cursos: {len(self.cursos)}"
        return info


# Exemplo de especialização: CursoGraduacao herda de Curso
class CursoGraduacao(Curso):
    def __init__(self, nome, carga_horaria=0, duracao_semestres=8):
        super().__init__(nome, carga_horaria)
        self.duracao_semestres = duracao_semestres

    def exibir_info(self):
        info = super().exibir_info()
        info += f" - Duração: {self.duracao_semestres} semestres"
        return info


# Exemplo de especialização: CursoPosGraduacao herda de Curso
class CursoPosGraduacao(Curso):
    def __init__(self, nome, carga_horaria=0, tipo="Especialização"):
        super().__init__(nome, carga_horaria)
        self.tipo = tipo  # Especialização, Mestrado, Doutorado

    def exibir_info(self):
        info = super().exibir_info()
        info += f" - Tipo: {self.tipo}"
        return info