

class Bairro:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, peso=0):
        self.vizinhos[vizinho.nome] = peso

    def obter_vizinhos(self):
        return list(self.vizinhos.keys())

    def obter_peso(self, vizinho):
        return self.vizinhos[vizinho.nome]