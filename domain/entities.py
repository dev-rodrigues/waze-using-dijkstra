import pygame
import math


class Bairro:
    def __init__(self, nome, x, y, debbug=False):
        self.nome = nome
        self.x = x #self.latitude_para_x(x, 1024)
        self.y = y #self.longitude_para_y(y, 800)
        self.vizinhos = {}
        if debbug:
            debbug(f"Bairro('{nome}', {x}, {y})")

    def adicionar_vizinho(self, vizinho, peso=0):
        self.vizinhos[vizinho.nome] = peso

    def obter_vizinhos(self):
        return list(self.vizinhos.keys())

    def obter_peso(self, vizinho):
        return self.vizinhos[vizinho.nome]

    def __str__(self):
        return f'Bairro: {self.nome}, x: {self.x}, y: {self.y}'

    def latitude_para_x(self, latitude, largura_tela):
        largura_graus = 360 / (2 * math.pi * 6378.1) * largura_tela

        # O ponto x correspondente à longitude da latitude, assumindo uma projeção Mercator:
        x = (latitude + 90) / 180 * largura_graus

        return int(x)

    def longitude_para_y(self, longitude, largura_tela):
        # intervalo de longitude da tela
        longitude_min = -43.5
        longitude_max = -43.2

        # intervalo de pixels na tela correspondente à longitude
        y_min = 50
        y_max = largura_tela - 50

        # cálculo da proporção entre a longitude e o intervalo de longitude na tela
        proporcao = (longitude - longitude_min) / (longitude_max - longitude_min)

        # cálculo do ponto y correspondente à proporção
        y = y_min + (y_max - y_min) * proporcao

        return y
