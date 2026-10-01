import matplotlib.pyplot as plt


class Produto:
    def __init__ (self, nome, preco, categoria, estoque):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque

# Definimos como o produto aparece quando é impresso
    def __str__ (self):
        return (f"{self.nome} | R$ {self.preco: .2f} | "
                f"Categoria: {self.categoria} | Estoque: {self.estoque}")

# Criar catálogo (lista) de produtos
catalogo = []
categorias = []

def adicionar_produto(nome, preco, categoria, estoque):
        novo_produto = Produto(nome, preco, categoria, estoque)
        catalogo.append(novo_produto)
        categorias.append(categoria)
        print(f"Produto '{nome}' adicionado ao catálogo")


def listar_catalogo():
    print("\n --- Catálogo da MinhaLoja ---")
    for produto in catalogo:
        print(produto)


# Cadastrar produtos
adicionar_produto('Notebook', 3500.00, "Informática", 15)
adicionar_produto("Smartphone", 2500.00, "Telefonia", 20)
adicionar_produto("Cafeteira", 500.00, "Eletrodoméstico", 30)
adicionar_produto("Geladeira", 1800.00, "Eletrodoméstico", 10)
adicionar_produto("Fone Bluetooth", 100.00, "Acessório", 50)
adicionar_produto("Teclado de PC", 50.00, "Periférico", 35)

listar_catalogo()

# Gráfico por categoria
categorias_unicas = list(set(categorias))
categorias_unicas.sort()

# Contagem de produtos em cada categoria (list comprehension)
contagem = [categorias.count(cat) for cat in categorias_unicas]

plt.bar(categorias_unicas, contagem, color='darkgreen')
plt.xlabel('Categoria')
plt.ylabel('Numero de produtos')
plt.title(' --- MinhaLoja - Produtos por categoria ---')
plt.show()