import heapq


def dijkstra(grafo, inicio, fim):
    bairros = grafo.keys()

    distancias = {nome: float('inf') for nome in bairros}
    distancias[inicio.nome] = 0

    antecessores = {nome: None for nome in bairros}

    heap = [(0, inicio.nome)]

    while heap:
        (distancia_atual, nome_atual) = heapq.heappop(heap)  # pega o nó com a menor distância

        if nome_atual == fim.nome:  # se encontrou o destino, retorna a distância e o melhor caminho
            caminho_final = [fim.nome]

            while antecessores[caminho_final[-1]] is not None:
                caminho_final.append(antecessores[caminho_final[-1]])

            caminho_final.reverse()

            return distancia_atual, caminho_final

        if distancia_atual > distancias[nome_atual]:  # se a distância atual é maior que a distância registrada, ignora
            continue

        bairro_atual = grafo[nome_atual]  # pega o objeto Bairro correspondente ao nome

        for vizinho_nome in bairro_atual.obter_vizinhos():
            vizinho = grafo[vizinho_nome]  # pega o objeto Bairro correspondente ao nome

            peso = bairro_atual.obter_peso(vizinho)  # pega o peso da aresta

            distancia = distancias[nome_atual] + peso  # calcula a nova distância

            if distancia < distancias[vizinho_nome]:  # se a nova distância é menor que a distância registrada, atualiza
                distancias[vizinho_nome] = distancia
                antecessores[vizinho_nome] = nome_atual

                heapq.heappush(heap, (distancia, vizinho_nome))  # adiciona na lista de prioridades

    return None, None
