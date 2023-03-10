import math

from domain.entities import Bairro

largura_tela = 1024
altura_tela = 1024


def mercatorX(lon):
    r_major = 6378137.000
    return r_major * math.radians(lon)


def mercatorY(lat):
    if lat > 89.5: lat = 89.5
    if lat < -89.5: lat = -89.5
    r_major = 6378137.000
    r_minor = 6356752.3142
    temp = r_minor / r_major
    eccent = math.sqrt(1 - temp ** 2)
    phi = math.radians(lat)
    sinphi = math.sin(phi)
    conep = eccent * sinphi
    com = eccent / 2
    con = math.pow(((1.0 - com) / (1.0 + com)), (eccent / 2))
    ts = math.tan((math.pi / 2 - phi) / 2) / con
    y = 0 - r_major * math.log(ts) - 6000000.0
    return y


def get_bairros():
    # zona sul
    centro = Bairro("Centro", 50, 50)
    copacabana = Bairro("Copacabana", 250, 200)
    ipanema = Bairro("Ipanema", 350, 150)
    leblon = Bairro("Leblon", 450, 100)
    botafogo = Bairro("Botafogo", 200, 400)
    flamengo = Bairro("Flamengo", 100, 300)
    catete = Bairro("Catete", 100, 200)
    gloria = Bairro("Glória", 50, 150)
    laranjeiras = Bairro("Laranjeiras", 150, 250)
    jardim_botanico = Bairro("Jardim Botânico", 500, 300)
    tijuca = Bairro("Tijuca", 300, 50)

    # zona oeste
    campo_grande = Bairro('Campo Grande', 330, 450)
    bangu = Bairro('Bangu', 450, 480)
    santa_cruz = Bairro('Santa Cruz', 570, 510)
    realengo = Bairro('Realengo', 390, 580)
    cosmos = Bairro('Cosmos', 510, 580)
    paciencia = Bairro('Paciência', 630, 610)
    taquara = Bairro('Taquara', 750, 610)

    copacabana.adicionar_vizinho(botafogo, 3)

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
    ipanema.adicionar_vizinho(copacabana, 5)

    leblon.adicionar_vizinho(ipanema, 2)
    leblon.adicionar_vizinho(botafogo, 5)
    leblon.adicionar_vizinho(laranjeiras, 6)
    leblon.adicionar_vizinho(jardim_botanico, 7)

    laranjeiras.adicionar_vizinho(leblon, 6)
    laranjeiras.adicionar_vizinho(jardim_botanico, 5)
    laranjeiras.adicionar_vizinho(tijuca, 8)

    jardim_botanico.adicionar_vizinho(laranjeiras, 5)
    jardim_botanico.adicionar_vizinho(leblon, 7)
    jardim_botanico.adicionar_vizinho(tijuca, 4)

    tijuca.adicionar_vizinho(laranjeiras, 8)
    tijuca.adicionar_vizinho(jardim_botanico, 4)

    campo_grande.adicionar_vizinho(bangu, 5)
    campo_grande.adicionar_vizinho(realengo, 7)

    bangu.adicionar_vizinho(campo_grande, 5)
    bangu.adicionar_vizinho(realengo, 5)
    bangu.adicionar_vizinho(santa_cruz, 6)

    santa_cruz.adicionar_vizinho(bangu, 6)
    santa_cruz.adicionar_vizinho(cosmos, 7)
    santa_cruz.adicionar_vizinho(paciencia, 5)

    realengo.adicionar_vizinho(campo_grande, 7)
    realengo.adicionar_vizinho(bangu, 5)
    realengo.adicionar_vizinho(cosmos, 6)

    cosmos.adicionar_vizinho(realengo, 6)
    cosmos.adicionar_vizinho(santa_cruz, 7)
    cosmos.adicionar_vizinho(paciencia, 4)

    paciencia.adicionar_vizinho(santa_cruz, 5)
    paciencia.adicionar_vizinho(cosmos, 4)
    paciencia.adicionar_vizinho(taquara, 6)

    taquara.adicionar_vizinho(paciencia, 6)

    bairros = {
        "Centro": centro,
        "Copacabana": copacabana,
        "Ipanema": ipanema,
        "Leblon": leblon,
        "Botafogo": botafogo,
        "Flamengo": flamengo,
        "Catete": catete,
        "Glória": gloria,
        "Laranjeiras": laranjeiras,
        "Jardim Botânico": jardim_botanico,
        "Tijuca": tijuca,
        "Campo Grande": campo_grande,
        "Bangu": bangu,
        "Santa Cruz": santa_cruz,
        "Realengo": realengo,
        "Cosmos": cosmos,
        "Paciência": paciencia,
        "Taquara": taquara
    }

    return bairros
