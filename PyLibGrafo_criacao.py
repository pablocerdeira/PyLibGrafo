# -*- coding:utf-8 -*-

# Bibliotecas de uso geral
import random


# ----------------------------------------------------------------------
# Cria grafo no formato dicionário:
# ----------------------------------------------------------------------
# Parâmetros:
#   nNos: número de nós
#   minArestas: mínimo de arestas por nó
#   maxArestas: máximo de arestas por nó
# Obs:
#   Esta representação de grafo é sempre direcional
# Saída:
#   Dicionário no qual as chaves são os nós de origem de uma aresta 
#   e o valor são subdicionário com os nós de destino (key) e o peso (value).
def cria_grafo_dicionario(nNos, minArestas, maxArestas, maxPeso):
    nos, arestas, tmpArestas = [], {}, {}

    nos = range(0,nNos)                                                       # cria lista com os nós

    for i in range(0,nNos+1):                                                 # loop nos nós
        for j in range(minArestas,random.randint(minArestas+1,maxArestas)):   # cria n. aleatório de arestas (entre min e max)
            tmp = random.choice(nos)                                          # escolhe um nó aleatório para ligar
            if tmp == i: continue                                             # se dest = origem então ignorar
            if tmp not in tmpArestas:                                         # se tmp já não está em tmpArestas...
                tmpArestas[tmp] = random.randint(1,maxPeso)                   # então adiciona o nó na lista tmpArestas
        arestas[i] = tmpArestas                                               # liga tmpArestas (lista de nós) ao nó origem
        tmpArestas = {}                                                       # zera tmpArestas para o próximo loop
    return arestas


