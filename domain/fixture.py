import math
import re

from domain.entities import Bairro


def mercator(lat, lon, zoom=16):
    R = 6371  # raio da Terra em km
    tileSize = 256
    siny = math.sin(lat * math.pi / 180)
    y = math.log((1 + siny) / (1 - siny)) / 2
    scale = 256 * math.pow(2, zoom)
    pixelX = (lon + 180) / 360 * scale
    pixelY = (0.5 - y / (2 * math.pi)) * scale
    return int(pixelX), int(pixelY)


def str_to_latitude(coord_str):
    # Extrai os valores de graus, minutos e segundos da string
    graus, minutos, segundos = map(int, re.findall(r'\d+', coord_str))

    # Calcula a latitude em graus decimais
    latitude = graus + minutos / 60 + segundos / 3600

    # Verifica se a latitude é sul (coord. S) e inverte o sinal se necessário
    if 'S' in coord_str:
        latitude = -latitude

    return latitude


def coord_to_longitude(coord):
    # Separa a string em graus, minutos e segundos
    graus, minutos, segundos = coord.split()[1::2]

    # Converte as strings para números inteiros
    graus = int(graus)
    minutos = int(minutos)
    segundos = int(segundos)

    # Calcula a longitude em graus decimais
    longitude = graus + minutos / 60 + segundos / 3600

    return longitude


def get_bairros():
    # centro = Bairro("Centro", 50, 50)
    # copacabana = Bairro("Copacabana", 250, 200)
    # ipanema = Bairro("Ipanema", 350, 150)
    # leblon = Bairro("Leblon", 450, 100)
    # botafogo = Bairro("Botafogo", 200, 400)
    # flamengo = Bairro("Flamengo", 100, 300)
    # catete = Bairro("Catete", 100, 200)
    # gloria = Bairro("Glória", 50, 150)
    # laranjeiras = Bairro("Laranjeiras", 150, 250)
    # jardim_botanico = Bairro("Jardim Botânico", 500, 300)
    # tijuca = Bairro("Tijuca", 300, 50)
    #
    # copacabana.adicionar_vizinho(botafogo, 3)
    #
    # centro.adicionar_vizinho(catete, 2)
    # centro.adicionar_vizinho(flamengo, 3)
    #
    # catete.adicionar_vizinho(centro, 2)
    # catete.adicionar_vizinho(botafogo, 3)
    # catete.adicionar_vizinho(gloria, 1)
    #
    # botafogo.adicionar_vizinho(catete, 3)
    # botafogo.adicionar_vizinho(ipanema, 4)
    # botafogo.adicionar_vizinho(leblon, 5)
    #
    # flamengo.adicionar_vizinho(centro, 3)
    # flamengo.adicionar_vizinho(catete, 1)
    #
    # gloria.adicionar_vizinho(catete, 1)
    #
    # ipanema.adicionar_vizinho(botafogo, 4)
    # ipanema.adicionar_vizinho(leblon, 2)
    # ipanema.adicionar_vizinho(copacabana, 5)
    #
    # leblon.adicionar_vizinho(ipanema, 2)
    # leblon.adicionar_vizinho(botafogo, 5)
    # leblon.adicionar_vizinho(laranjeiras, 6)
    # leblon.adicionar_vizinho(jardim_botanico, 7)
    #
    # laranjeiras.adicionar_vizinho(leblon, 6)
    # laranjeiras.adicionar_vizinho(jardim_botanico, 5)
    # laranjeiras.adicionar_vizinho(tijuca, 8)
    #
    # jardim_botanico.adicionar_vizinho(laranjeiras, 5)
    # jardim_botanico.adicionar_vizinho(leblon, 7)
    # jardim_botanico.adicionar_vizinho(tijuca, 4)
    #
    # tijuca.adicionar_vizinho(laranjeiras, 8)
    # tijuca.adicionar_vizinho(jardim_botanico, 4)
    #
    # bairros = {
    #     "Centro": centro,
    #     "Copacabana": copacabana,
    #     "Ipanema": ipanema,
    #     "Leblon": leblon,
    #     "Botafogo": botafogo,
    #     "Flamengo": flamengo,
    #     "Catete": catete,
    #     "Glória": gloria,
    #     "Laranjeiras": laranjeiras,
    #     "Jardim Botânico": jardim_botanico,
    #     "Tijuca": tijuca
    # }
    #
    # return bairros
