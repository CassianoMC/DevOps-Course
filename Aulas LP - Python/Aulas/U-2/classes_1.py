# Define uma classe chamada Pessoa
class Pessoa:

# O método __init__ é um contrutor, chamado quando um objeto da classe é criado
# Ele inicializa os atributos de classe
# self é uma convenção em Python que se refere á própia instância da classe
# Os parâmetros nome, idade e gênero são passados durante a criação do objeto
# Eles são usados para inicializar os atributos da instância
   def __init__ (self, nome, idade, genero):
      self.nome = nome
      self.idade = idade
      self.genero = genero

# O método "cumprimentar" retorna uma saudação com o nome da pessoa
   def cumprimentar (self):
     return f"Olá, meu nome é {self.nome}."

# O método aniversário aumenta a idade da pessoa em 1
   def aniversario(self):
     self.idade += 1
# Cria uma instância da da classe "Pessoa" com os valores "João", "30" e "Masculino"
pessoa1 = Pessoa("João", 30, "Masculino")

# Chama o método "cumprimentar" na instância "pessoa1" e imprime a saudação
# Acessa o atributo idade da instância "pessoa1" e imprime sua idade
print(pessoa1.cumprimentar())
print(f"Idade: {pessoa1.idade}")
print(f"Genero: {pessoa1.genero}")

# Chama o método "aniversário" na instânciacia "pessoa1" para aumentar sua idade em 1
pessoa1.aniversario()

# Acessa o atributo idade atualizado da instância "pessoa1" e imprime a nova idade dela
print(f"Nova idade: {pessoa1.idade}")