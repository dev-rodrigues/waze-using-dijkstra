from dijkstra import dijkstra
from domain.fixture import get_bairros

if __name__ == '__main__':

    bairros = get_bairros()

    (caminho, melhor_caminho) = dijkstra(
        bairros,
        bairros["Ipanema"],
        bairros["Centro"]
    )

    print(f"A distância do Catete a Ipanema é de {caminho} km. E o melhor caminho é {melhor_caminho}")
