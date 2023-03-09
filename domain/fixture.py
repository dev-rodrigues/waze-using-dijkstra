from domain.entities import Bairro


def get_bairros():
    centro = Bairro("Centro")
    copacabana = Bairro("Copacabana")
    ipanema = Bairro("Ipanema")
    leblon = Bairro("Leblon")
    botafogo = Bairro("Botafogo")
    flamengo = Bairro("Flamengo")
    catete = Bairro("Catete")
    gloria = Bairro("Glória")

    centro.adicionar_vizinho(catete, 2)
    centro.adicionar_vizinho(flamengo, 3)

    catete.adicionar_vizinho(centro, 2)
    catete.adicionar_vizinho(botafogo, 3)
    catete.adicionar_vizinho(gloria, 1)

    botafogo.adicionar_vizinho(catete, 3)
    botafogo.adicionar_vizinho(ipanema, 4)
    botafogo.adicionar_vizinho(leblon, 5)

    flamengo.adicionar_vizinho(centro, 3)
    flamengo.adicionar_vizinho(catete, 1)

    gloria.adicionar_vizinho(catete, 1)

    ipanema.adicionar_vizinho(botafogo, 4)
    ipanema.adicionar_vizinho(leblon, 2)

    leblon.adicionar_vizinho(ipanema, 2)
    leblon.adicionar_vizinho(botafogo, 5)

    bairros = {
        "Centro": centro,
        "Copacabana": copacabana,
        "Ipanema": ipanema,
        "Leblon": leblon,
        "Botafogo": botafogo,
        "Flamengo": flamengo,
        "Catete": catete,
        "Glória": gloria
    }

    return bairros