# -*- coding:utf-8 -*-

# Biblioteca para Grafo
from PyLibGrafo import Grafo

# ----------------------------------------------------------------
# INÍCIO DA DEMONSTRAĆÃO DA BIBLIOTECA GRAFO
# ----------------------------------------------------------------

def main():

    # instancia Grafo em grf
    grf = Grafo()

    print '''
-----------------------------------------------------------
Demonstracão da biblioteca Grafo
Professor: Alexandre Rademaker
Aluno: Pablo Cerdeira
-----------------------------------------------------------
    '''
    
    print '''
-----------------------------------------------------------
Setando o atributo grafo do objeto grf para um grafo
-----------------------------------------------------------
    '''
    grf.grafo = {0: {16: 4, 11: 2}, 1: {3: 2}, 2: {18: 3}, 3: {8: 3, 7: 3}, 4: {19: 3}, 5: {15: 3}, 6: {14: 1}, 7: {2: 5, 11: 3}, 8: {1: 5}, 9: {15: 1}, 10: {16: 4, 3: 5}, 11: {5: 3}, 12: {6: 5}, 13: {17: 2}, 14: {0: 5, 2: 3}, 15: {19: 1}, 16: {17: 2, 4: 1}, 17: {0: 1}, 18: {16: 1, 12: 3}, 19: {13: 2}, 20: {9: 5, 15: 1}}
    grafo = grf.grafo
    print '''
-----------------------------------------------------------
Imprime o grafo:
-----------------------------------------------------------
    '''
    print grafo

    print '''
-----------------------------------------------------------
Demonstrando a criacão de grafos randômicos
-----------------------------------------------------------
    '''
    nNos = 100                                                                   # nNos: número de nós no grafo
    minArestas = 1                                                              # minArestas: mínimo de arestas para cada nó
    maxArestas = 5                                                              # maxArestas: máximo de arestas para cada nó
    maxPeso = 5                                                                 # maxPeso: peso máximo de cada aresta

    grafo = grf.random(nNos,minArestas,maxArestas,maxPeso)
    
    print '''
-----------------------------------------------------------
Imprime o grafo randômico
-----------------------------------------------------------
    '''
    print grafo

    print '''
-----------------------------------------------------------
Converte grf.grafo para matriz de adjacências
-----------------------------------------------------------
    '''
    print grf.converter("matriz")

    print '''
-----------------------------------------------------------
Converte grf.grafo para dicionário de tuplas
-----------------------------------------------------------
    '''
    print grf.converter("tuplas")

    print '''
-----------------------------------------------------------
Plota grf.grafo usando o Ubigraph
-----------------------------------------------------------
    '''
    print "Output: ", grf.plota("ubigraph")

    print '''
-----------------------------------------------------------
Plota grf.grafo usando o Graph-Tools e salva em PDF
-----------------------------------------------------------
    '''
    print "Output: ", grf.plota("graph-tools",arquivo="grafoGraph-Tools.pdf")
    # pode-se utilizar as extensões png, pdf etc

    print '''
-----------------------------------------------------------
Plota grf.grafo usando o NetworkX e salva em PDF
-----------------------------------------------------------
    '''
    print "Output: ", grf.plota("networkx",arquivo="grafoNetworkX.pdf")
    # pode-se utilizar as extensões png, pdf etc

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
BFS - Breadth First Search
Nó Origem: 1
Nó Destino: 4
-----------------------------------------------------------
    '''
    print grf.bfs(inicio=1,fim=4)

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
BFS - Breadth First Search
Nó Origem: 1
Nó Destino: Até onde for possível
-----------------------------------------------------------
    '''
    print grf.bfs(inicio=1,fim=-1)

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
DFS - Deep First Search
Nó Origem: 1
Nó Destino: 4
-----------------------------------------------------------
    '''
    print grf.dfs(inicio=1,fim=4)

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
DFS - Deep First Search
Nó Origem: 1
Nó Destino: Até onde for possível
-----------------------------------------------------------
    '''
    print grf.dfs(inicio=1,fim=-1)

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
RDFS - Recursive Deep First Search
Nó Origem: 1
Nó Destino: 4
ATENCÃO: Ainda está bugado
-----------------------------------------------------------
    '''
    print grf.r_dfs(inicio=1,fim=4)

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
RDFS - Recursive Deep First Search
Nó Origem: 1
Nó Destino: Até onde for possível
-----------------------------------------------------------
    '''
    print grf.r_dfs(inicio=1,fim=-1)

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
Tree DFS - Gera Tree com o Deep First Search
Nó Origem: 1
Nó Destino: Até onde for possível
-----------------------------------------------------------
    '''
    print grf.tree_bfs(inicio=1,fim=-1)

    print "Output: ", grf.plota_tree("graph-tools",arquivo="treeGraph-Tools.pdf")
    print "Output: ", grf.plota_tree("networkx",arquivo="treeTreeNetworkX.pdf")
    print "Output: ", grf.plota_tree("ubigraph")

    print '''
-----------------------------------------------------------
Algoritmos de navegacão em grafos:
Tree DFS - Gera Tree com o Deep First Search
Nó Origem: 1
Nó Destino: 4
-----------------------------------------------------------
    '''
    print grf.tree_bfs(inicio=1,fim=4)


    print "Output: ", grf.plota_tree("graph-tools",arquivo="treeGraph-Tools2.pdf")
    print "Output: ", grf.plota_tree("networkx",arquivo="treeTreeNetworkX2.pdf")
    print "Output: ", grf.plota_tree("ubigraph")






if __name__ == "__main__":
    main()
    
    
    
