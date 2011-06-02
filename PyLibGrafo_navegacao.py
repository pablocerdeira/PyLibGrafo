# -*- coding:utf-8 -*-

# ----------------------------------------------------------------
# FUNÇÕES PARA NAVEGAÇÃO NOS GRAFOS
# ----------------------------------------------------------------

def bfs(grafo, inicio, fim):

    nos = grafo.keys()
    tmp = [nos[inicio]]
    path = []
    while tmp:
        noOrigem = tmp.pop(0)
        if noOrigem not in path:
            path = path + [noOrigem]
            if noOrigem == fim:
                return path
            for noDestino in grafo[noOrigem]:
                tmp = tmp + [noDestino]
                if noDestino == fim:
                    path = path + [noDestino] 
                    return path
    return path
    

def dfs(grafo, inicio, fim):

    nos = grafo.keys()
    tmp = [nos[inicio]]
    path = []
    while tmp:
        noOrigem = tmp.pop(0)
        if noOrigem not in path:
            path = path + [noOrigem]
            if noOrigem == fim:
                return path
            for noDestino in grafo[noOrigem]:
                tmp = [noDestino] + tmp
                if noDestino == fim:
                    path = path + [noDestino] 
                    return path
    return path

# TODO: não consegui fazer parar o rcursivo quando encontra o destino
def r_dfs(grafo, inicio, fim, path=[], done=False):

    if done:
        return path

    path = path + [inicio]

    for no in grafo[inicio]:
        if no == fim:
            done = True
        if not no in path:
            path = r_dfs(grafo, no, fim, path, done)
    return path
    

# Gera árvore utilizando o BFS
def tree_bfs(grafo, inicio, fim):

    nos = grafo.keys()
    tmp = [nos[inicio]]
    path, pathDestino = [], []
    arestas, tmpArestas = [], {}
    while tmp:
        noOrigem = tmp.pop(0)
        if noOrigem not in path:
            path = path + [noOrigem]
            if noOrigem != fim:
                for noDestino in grafo[noOrigem]:
                    tmp = tmp + [noDestino]
                    if noDestino not in path:
                        if noDestino not in pathDestino:
                            if noDestino != fim:
                                tmpArestas[noDestino] = grafo[noOrigem][noDestino]
                                pathDestino = pathDestino + [noDestino]
                            else:
                                tmpArestas[noDestino] = grafo[noOrigem][noDestino]
                                arestas.append({noOrigem:tmpArestas})
                                return arestas
                                break
                arestas.append({noOrigem:tmpArestas})
                tmpArestas = {}
            else:
                return arestas
                break
        
    return arestas

















