import heapq

def dijkstra(grafo, inicio, fim):
    bairros = {b.nome: b for b in grafo}

    distancias = {nome: float('inf') for nome in bairros}

    distancias[inicio.nome] = 0

    heap = [(0, inicio.nome)]

    while heap:
        (distancia_atual, nome_atual) = heapq.heappop(heap)  # pega o nó com a menor distância

        if nome_atual == fim.nome:  # se encontrou o destino, retorna a distância
            return distancia_atual

        if distancia_atual > distancias[nome_atual]:  # se a distância atual é maior que a distância registrada, ignora
            continue
        bairro_atual = bairros[nome_atual]  # pega o objeto Bairro correspondente ao nome

        for vizinho_nome in bairro_atual.obter_vizinhos():
            vizinho = bairros[vizinho_nome]  # pega o objeto Bairro correspondente ao nome

            peso = bairro_atual.obter_peso(vizinho)  # pega o peso da aresta

            distancia = distancias[nome_atual] + peso  # calcula a nova distância

            if distancia < distancias[vizinho_nome]:  # se a nova distância é menor que a distância registrada, atualiza
                distancias[vizinho_nome] = distancia

                heapq.heappush(heap, (distancia, vizinho_nome))  # adiciona na lista de prioridades

    return None
