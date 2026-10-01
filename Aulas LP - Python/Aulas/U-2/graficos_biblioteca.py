import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:
    def __init__ (self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__ (self):
        return f'"{self.titulo}" por {self.autor} | Gênero: {self.genero} | Disponível: {self.quantidade}'

# Criar uma lista de livros
biblioteca = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"'{titulo}' foi adicionado a biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros():
    print("\n--- Lista de todos os livros ----")
    for livro in biblioteca:
        print(livro)
    print("---------------------------------\n")

# Função para buscar livro pelo título
def buscar_livro(titulo_buscado):
    print(f"Buscando por: '{titulo_buscado}' ...")
    for livro in biblioteca:
        if livro.titulo.lower() == titulo_buscado.lower():
            print(f"Encontrado: {livro}\n")
            return
    print("Livro não encontrado na biblioteca. \n")

# Adicionar livros à biblioteca
adicionar_livro("Dom Casmurro", "Machado de Assis", "Romance", 8)
adicionar_livro("1984", "George Orwell", "Ficção", 6)
adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 12)
adicionar_livro("A Culpa é das Estrelas", "John Green", "Romance", 7 )
adicionar_livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 15)
adicionar_livro("O Alquimista", "Paulo Coelho", "Ficção", 5)
adicionar_livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 9)
adicionar_livro("A Revolução dos Bichos", "George Orwell", "Ficção", 13)
adicionar_livro("As Crônicas de Nárnia", "C.S. Lewis", "Fantasia", 5)
adicionar_livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 11)
adicionar_livro("Duna", "Frank Herbert", "Ficção", 4 )
adicionar_livro("O Processo", "Franz Kafka", "Ficção", 10)

# Testando listagem e busca
listar_livros()
buscar_livro("1984")
buscar_livro("O Código da Vinci") # <--- Testando um livro que nao existe na lista

# Contagem de livros agrupandp por gênero (somando a quantidade disponível)
contagem_por_genero = {}
for livro in biblioteca:
    if livro.genero in contagem_por_genero:
        contagem_por_genero[livro.genero] += livro.quantidade
    else:
        contagem_por_genero[livro.genero] = livro.quantidade

generos = list(contagem_por_genero.keys())
quantidades = list(contagem_por_genero.values())

# Criando um gráfico de barras
plt.bar(generos, quantidades, color='darkgreen')
plt.xlabel('Gênero Literário')
plt.ylabel('Quantidade de Livros')
plt.title('Quantidade de Livros Disponível por Gênero')


# Adicionando rótulos aos pontos de dados
for i, valor in enumerate(quantidades):
    plt.text(i, valor, str(valor), ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()