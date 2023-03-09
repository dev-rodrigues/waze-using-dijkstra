

class Bairro:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = {}

    def adicionar_vizinho(self, vizinho, peso=0):
        self.vizinhos[vizinho.nome] = peso

    def obter_vizinhos(self):
        return list(self.vizinhos.keys())

    def obter_peso(self, vizinho):
        return self.vizinhos[vizinho.nome]