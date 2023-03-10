import pygame
import time

from dijkstra import dijkstra
from domain.fixture import get_bairros

largura_tela = 800
altura_tela = 600

terminou = False

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("meu waze")
pygame.display.init()

pygame.font.init()
clock = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 20)


def desenha_bairros(bairros):
    for bairro in bairros.values():
        x = bairro.x
        y = bairro.y

        # Desenha um ponto em verde no local do bairro
        pygame.draw.circle(tela, (0, 255, 0), (x, y), 5)

        # Desenha o nome do bairro
        texto = fonte.render(bairro.nome, True, (255, 255, 255))
        tela.blit(texto, (x - 20, y - 20))

        for vizinho in bairro.vizinhos:
            vx = bairros[vizinho].x
            vy = bairros[vizinho].y
            pygame.draw.line(tela, (255, 255, 255), (x, y), (vx, vy))


def destaca_melhor_caminho(bairros, caminho):
    for i in range(len(caminho) - 1):
        atual = caminho[i]
        proximo = caminho[i + 1]
        pygame.draw.line(
            tela,
            (255, 0, 0),
            (bairros[atual].x, bairros[atual].y),
            (bairros[proximo].x, bairros[proximo].y),
            5
        )


while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    # obtem o grafo de bairros
    bairros = get_bairros()

    desenha_bairros(bairros)

    pygame.display.update()

    # encontra caminho e distancia
    (caminho, melhor_caminho) = dijkstra(
        bairros,
        bairros["Ipanema"],
        bairros["Centro"]
    )

    destaca_melhor_caminho(bairros, melhor_caminho)
    pygame.display.update()

# if __name__ == '__main__':
#     # obtem o grafo de bairros
#     bairros = get_bairros()
#
#     # encontra caminho e distancia
#     (caminho, melhor_caminho) = dijkstra(
#         bairros,
#         bairros["Ipanema"],
#         bairros["Centro"]
#     )
#
#     print(f"A distância do Catete a Ipanema é de {caminho} km. E o melhor caminho é {melhor_caminho}")

