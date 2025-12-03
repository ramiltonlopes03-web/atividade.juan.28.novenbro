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
Vou analisar os códigos para verificar a implementação do princípio de Herança.

#Eu perguntei pra IA se o codigo implementar o principio de Herança:

## Análise da Implementação de Herança

**✅ SIM, o código implementa corretamente o princípio de Herança da Programação Orientada a Objetos.**

### Hierarquia de Classes Identificada:

```
EntidadeAcademica (classe base)
    │
    ├── Curso
    │     │
    │     ├── CursoGraduacao
    │     │
    │     └── CursoPosGraduacao
    │
    └── Campus
```

### Evidências de Herança Correta:

**1. Herança Simples:**
- `Curso` herda de `EntidadeAcademica`
- `Campus` herda de `EntidadeAcademica`

**2. Herança Multinível:**
- `CursoGraduacao` herda de `Curso` (que herda de `EntidadeAcademica`)
- `CursoPosGraduacao` herda de `Curso` (que herda de `EntidadeAcademica`)

**3. Uso Correto de `super()`:**
```python
super().__init__(nome)  # Chama construtor da classe pai
info = super().exibir_info()  # Chama método da classe pai
```

**4. Sobrescrita de Métodos (Override):**
Todas as classes filhas sobrescrevem o método `exibir_info()` adequadamente, estendendo o comportamento da classe pai.

**5. Especialização:**
- `CursoGraduacao` adiciona atributo `duracao_semestres`
- `CursoPosGraduacao` adiciona atributo `tipo`
- `Campus` adiciona atributos `cidade` e `cursos`

### Benefícios Obtidos:

- ✅ Reutilização de código (atributo `nome` e método `__str__`)
- ✅ Extensibilidade (fácil adicionar novos tipos de cursos)
- ✅ Polimorfismo (todos compartilham método `exibir_info()`)
- ✅ Organização hierárquica lógica

**Conclusão:** O código demonstra excelente aplicação do princípio de Herança com múltiplos níveis e especialização adequada das classes.
#Eu perguntei a IA se o codigo implementa verificação dinamica:

## Análise de Verificação Dinâmica de Tipos

**❌ NÃO, o código NÃO implementa verificação dinâmica de tipos de forma explícita.**

### O que é Verificação Dinâmica?

Verificação dinâmica envolve verificar o tipo de um objeto em tempo de execução usando funções como:
- `isinstance(objeto, Classe)` - verifica se objeto é instância de uma classe
- `type(objeto)` - retorna o tipo do objeto
- `issubclass(classe, SuperClasse)` - verifica herança entre classes
- `hasattr(objeto, 'atributo')` - verifica se objeto tem determinado atributo

### O que o Código Atual Faz:

```python
# Apenas usa __class__.__name__ para exibição
def exibir_info(self):
    return f"{self.__class__.__name__}: {self.nome}"
```

Isso é apenas para formatação de string, não é verificação dinâmica.

### O que Está Faltando:

**1. Nenhuma validação de tipos nos métodos:**
```python
def adicionar_curso(self, nome_curso, carga_horaria=0):
    self.cursos.append(Curso(nome_curso, carga_horaria))
    # ❌ Não verifica se nome_curso é string
    # ❌ Não verifica se carga_horaria é int
```

**2. Nenhuma verificação de instâncias:**
```python
# No menu.py
campus.cursos.append(curso)
# ❌ Não verifica se 'curso' é realmente uma instância de Curso
```

**3. Nenhum tratamento polimórfico com verificação:**
```python
# Poderia ter algo como:
def processar_curso(self, curso):
    if isinstance(curso, CursoGraduacao):
        # Lógica específica para graduação
    elif isinstance(curso, CursoPosGraduacao):
        # Lógica específica para pós
```

### Exemplo de Como Implementar Verificação Dinâmica:

```python
def adicionar_curso_seguro(self, curso):
    """Adiciona curso com verificação dinâmica"""
    if not isinstance(curso, Curso):
        raise TypeError("Apenas objetos do tipo Curso podem ser adicionados")
    self.cursos.append(curso)

def contar_por_tipo(self):
    """Conta cursos por tipo usando verificação dinâmica"""
    contagem = {
        'Graduação': 0,
        'Pós-Graduação': 0,
        'Outros': 0
    }
    for curso in self.cursos:
        if isinstance(curso, CursoGraduacao):
            contagem['Graduação'] += 1
        elif isinstance(curso, CursoPosGraduacao):
            contagem['Pós-Graduação'] += 1
        else:
            contagem['Outros'] += 1
    return contagem
```

### Conclusão:

O código implementa **Herança** corretamente, mas **NÃO implementa verificação dinâmica de tipos**. Ele assume que os dados fornecidos são corretos e não valida tipos em tempo de execução.
