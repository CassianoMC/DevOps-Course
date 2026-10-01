# Herença --> classe-pai "Animal" e duas classes-filhas
class animal:
    def __init__ (self, nome):
        self.nome = nome

    def fazer_barulho(self):
        pass # <-- Método "vazio" que será sobrescrito pelas "filhas"

class cachorro(animal):
    def fazer_barulho(self):
        return "Au au!"

class gato(animal):
    def fazer_barulho(self):
        return "Miau!"

#Criando e usando objetos das classes-filhas
rex = cachorro("Rex")
tom = gato("Tom")

# Chamando o método "fazer_barulho" em objetos
print(f"{rex.nome} diz: {rex.fazer_barulho()}")
print(f"{tom.nome} diz: {tom.fazer_barulho()}")