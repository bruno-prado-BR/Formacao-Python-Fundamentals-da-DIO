class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo instância da classe")

    def falar(self):
        print("Auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "Amarelo")
c.falar()

print("Olá mundo")
print("Olá mundo")

del c # Forçar o uso do destrutor

print("Olá mundo")
print("Olá mundo")

#criar_cachorro()