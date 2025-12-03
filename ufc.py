# Classe base (superclasse)
class EntidadeAcademica:
    """Classe base para entidades acadêmicas"""

    def __init__(self, nome):
        # VERIFICAÇÃO DINÂMICA: Valida se nome é string
        if not isinstance(nome, str):
            raise TypeError(f"Nome deve ser string, recebido {type(nome).__name__}")
        if not nome.strip():
            raise ValueError("Nome não pode ser vazio")
        self.nome = nome

    def __str__(self):
        return self.nome

    def exibir_info(self):
        return f"{self.__class__.__name__}: {self.nome}"


# Classe Curso herda de EntidadeAcademica
class Curso(EntidadeAcademica):
    def __init__(self, nome, carga_horaria=0):
        super().__init__(nome)
        
        # VERIFICAÇÃO DINÂMICA: Valida tipo de carga_horaria
        if not isinstance(carga_horaria, (int, float)):
            raise TypeError(f"Carga horária deve ser número, recebido {type(carga_horaria).__name__}")
        if carga_horaria < 0:
            raise ValueError("Carga horária não pode ser negativa")
        
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
        
        # VERIFICAÇÃO DINÂMICA: Valida tipo de cidade
        if not isinstance(cidade, str):
            raise TypeError(f"Cidade deve ser string, recebido {type(cidade).__name__}")
        
        self.cidade = cidade
        self.cursos = []

    def adicionar_curso(self, curso):
        """
        VERIFICAÇÃO DINÂMICA IMPLEMENTADA:
        - Verifica se o objeto é uma instância de Curso
        - Previne adicionar tipos incorretos à lista
        """
        if not isinstance(curso, Curso):
            raise TypeError(
                f"Apenas objetos do tipo Curso podem ser adicionados. "
                f"Recebido: {type(curso).__name__}"
            )
        self.cursos.append(curso)
        print(f"✓ Curso '{curso.nome}' do tipo '{type(curso).__name__}' adicionado!")

    def listar_cursos(self):
        return [curso.nome for curso in self.cursos]

    def atualizar_curso(self, indice, novo_nome, nova_carga=None):
        """
        VERIFICAÇÃO DINÂMICA IMPLEMENTADA:
        - Valida tipo do índice
        - Valida intervalo do índice
        - Valida tipos dos novos valores
        """
        if not isinstance(indice, int):
            raise TypeError(f"Índice deve ser inteiro, recebido {type(indice).__name__}")
        
        if not isinstance(novo_nome, str):
            raise TypeError(f"Novo nome deve ser string, recebido {type(novo_nome).__name__}")
        
        if not 0 <= indice < len(self.cursos):
            raise IndexError(f"Índice {indice} fora do intervalo válido (0-{len(self.cursos)-1})")
        
        if nova_carga is not None and not isinstance(nova_carga, (int, float)):
            raise TypeError(f"Carga horária deve ser número, recebido {type(nova_carga).__name__}")
        
        self.cursos[indice].nome = novo_nome
        if nova_carga is not None:
            self.cursos[indice].carga_horaria = nova_carga

    def remover_curso(self, indice):
        """
        VERIFICAÇÃO DINÂMICA IMPLEMENTADA:
        - Valida tipo e intervalo do índice
        """
        if not isinstance(indice, int):
            raise TypeError(f"Índice deve ser inteiro, recebido {type(indice).__name__}")
        
        if not 0 <= indice < len(self.cursos):
            raise IndexError(f"Índice {indice} fora do intervalo válido (0-{len(self.cursos)-1})")
        
        del self.cursos[indice]

    def contar_cursos_por_tipo(self):
        """
        VERIFICAÇÃO DINÂMICA EM USO:
        - Usa isinstance() para identificar tipos específicos
        - Demonstra polimorfismo com verificação de tipo
        """
        contagem = {}
        for curso in self.cursos:
            # type().__name__ retorna o nome da classe do objeto
            tipo = type(curso).__name__
            contagem[tipo] = contagem.get(tipo, 0) + 1
        return contagem

    def listar_cursos_por_tipo(self, tipo_curso):
        """
        VERIFICAÇÃO DINÂMICA EM USO:
        - Filtra cursos baseado no tipo da classe
        - Aceita a classe como parâmetro
        """
        if not isinstance(tipo_curso, type):
            raise TypeError("tipo_curso deve ser uma classe")
        
        if not issubclass(tipo_curso, Curso):
            raise TypeError("tipo_curso deve ser uma subclasse de Curso")
        
        return [c for c in self.cursos if isinstance(c, tipo_curso)]

    def exibir_info(self):
        """Sobrescreve o método da classe pai"""
        info = super().exibir_info()
        if self.cidade:
            info += f" - Cidade: {self.cidade}"
        info += f" - Total de Cursos: {len(self.cursos)}"
        
        # VERIFICAÇÃO DINÂMICA EM USO: Mostra estatísticas por tipo
        if self.cursos:
            tipos = self.contar_cursos_por_tipo()
            info += f" - Por tipo: {tipos}"
        
        return info


# Exemplo de especialização: CursoGraduacao herda de Curso
class CursoGraduacao(Curso):
    def __init__(self, nome, carga_horaria=0, duracao_semestres=8):
        super().__init__(nome, carga_horaria)
        
        # VERIFICAÇÃO DINÂMICA: Valida duracao_semestres
        if not isinstance(duracao_semestres, int):
            raise TypeError(f"Duração deve ser inteiro, recebido {type(duracao_semestres).__name__}")
        if duracao_semestres <= 0:
            raise ValueError("Duração deve ser positiva")
        
        self.duracao_semestres = duracao_semestres

    def exibir_info(self):
        info = super().exibir_info()
        info += f" - Duração: {self.duracao_semestres} semestres"
        return info


# Exemplo de especialização: CursoPosGraduacao herda de Curso
class CursoPosGraduacao(Curso):
    TIPOS_VALIDOS = ["Especialização", "Mestrado", "Doutorado"]
    
    def __init__(self, nome, carga_horaria=0, tipo="Especialização"):
        super().__init__(nome, carga_horaria)
        
        # VERIFICAÇÃO DINÂMICA: Valida tipo de pós-graduação
        if not isinstance(tipo, str):
            raise TypeError(f"Tipo deve ser string, recebido {type(tipo).__name__}")
        
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo deve ser um de: {self.TIPOS_VALIDOS}")
        
        self.tipo = tipo

    def exibir_info(self):
        info = super().exibir_info()
        info += f" - Tipo: {self.tipo}"
        return info


# DEMONSTRAÇÃO DE VERIFICAÇÃO DINÂMICA
if __name__ == "__main__":
    print("=== DEMONSTRAÇÃO DE VERIFICAÇÃO DINÂMICA ===\n")
    
    # Criando um campus
    campus = Campus("Campus do Pici", "Fortaleza")
    
    # Criando cursos de diferentes tipos
    curso1 = CursoGraduacao("Ciência da Computação", 3600, 8)
    curso2 = CursoPosGraduacao("Inteligência Artificial", 400, "Mestrado")
    curso3 = Curso("Python Básico", 40)
    
    # Adicionando cursos (verificação dinâmica em ação)
    campus.adicionar_curso(curso1)
    campus.adicionar_curso(curso2)
    campus.adicionar_curso(curso3)
    
    print(f"\n{campus.exibir_info()}\n")
    
    # Listando cursos por tipo usando isinstance()
    print("--- Cursos de Graduação ---")
    graduacoes = campus.listar_cursos_por_tipo(CursoGraduacao)
    for c in graduacoes:
        print(f"  - {c.exibir_info()}")
    
    print("\n--- Cursos de Pós-Graduação ---")
    pos_graduacoes = campus.listar_cursos_por_tipo(CursoPosGraduacao)
    for c in pos_graduacoes:
        print(f"  - {c.exibir_info()}")
    
    # Demonstrando verificação de tipo
    print("\n--- Verificando Tipos Dinamicamente ---")
    for i, curso in enumerate(campus.cursos):
        print(f"{i+1}. {curso.nome}")
        print(f"   + Tipo: {type(curso).__name__}")
        print(f"   + É Curso? {isinstance(curso, Curso)}")
        print(f"   + É CursoGraduacao? {isinstance(curso, CursoGraduacao)}")
        print(f"   + É CursoPosGraduacao? {isinstance(curso, CursoPosGraduacao)}")
        print()
    
    # Testando erros de verificação dinâmica
    print("--- Testando Validações ---")
    try:
        campus.adicionar_curso("Isso não é um curso")
    except TypeError as e:
        print(f" Erro capturado: {e}")
    
    try:
        curso_invalido = CursoGraduacao("Teste", "texto_invalido")
    except TypeError as e:
        print(f" Erro capturado: {e}")
