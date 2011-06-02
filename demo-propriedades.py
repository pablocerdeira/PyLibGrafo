# -*- coding:utf-8 -*-
# ----------------------------------------------------------------
# DEMONSTRACAO DE USO DE PROPRIEDADES DA CLASSE GRAFO
# ----------------------------------------------------------------


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
Criacão de grafos randômicos
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
A funcão grf.nos() retorna um set com todos os nós do grafo.
-----------------------------------------------------------
    '''
    print "Conjunto de nós: %s" % str(grf.nos())



    print '''
-----------------------------------------------------------
É possível fazer looping com os dados do grafo.
Demonstrando looping para imprimir nós e arestas.
-----------------------------------------------------------
    '''
    for noOrigem in grf.grafo:
        for noDestino in grf.grafo[noOrigem]:
            print "Nó Origem: %s - Nó Destino: %s - Peso da Aresta: %s" % (str(noOrigem), str(noDestino), str(grf.grafo[noOrigem][noDestino]))

    print '''
-----------------------------------------------------------
Também é possível acessar um nó diretamente, pegando seus destinos,
bem como o peso de cada destino.
-----------------------------------------------------------
    '''

    print "Destinos e pesos do nó 5: %s" % str(grf.grafo[5])
    print ""
    print "Destinos e pesos a partir do nó 5: "
    for noDestino in grf.grafo[5]:
        print "Destino: %s - Peso: %s" % (str(noDestino), str(grf.grafo[5][noDestino]))
    
    print '''
-----------------------------------------------------------
Podemos setar propriedades para os nós.
Setando propriedade label e tamanho.
Outras propriedades podem ser adicionadas livremente com os
seguintes parâmetros:
grf.adProp(<no>, <propriedade>, <valor>)
-----------------------------------------------------------
    '''

    grf.adProp(5,"label","Texto do 5")
    grf.adProp(5,"tamanho", 6)
    
    grf.adProp(10,"label","Texto do 10")
    grf.adProp(10,"tamanho",8)

    print "Label do nó 5: %s" % str(grf.props[5]["label"])
    print "Tamanho do nó 5: %s" % str(grf.props[5]["tamanho"])
    print "Label do nó 10: %s" % str(grf.props[10]["label"])
    print "Tamanho do nó 10: %s" % str(grf.props[10]["tamanho"])


    print '''
-----------------------------------------------------------
Exemplo de adicão de propriedade label e cor para todos os nós
Para este exemplo utilizaremos a funcão gfr.nos() pois só
precisamos dos nós, e não das arestas.
Imprimimos o label e a cor dos nós 2 e 7. 
-----------------------------------------------------------
    '''

    i = 1
    for no in grf.nos():
        grf.adProp(no,"label","Bola " + str(no))
        if i > 0:
            grf.adProp(no,"cor","azul")
        else:
            grf.adProp(no,"cor","vermelho")
        i = i * (-1)
                
    print grf.props[2]["label"], " - cor: ", grf.props[2]["cor"] 
    print grf.props[7]["label"], " - cor: ", grf.props[7]["cor"] 
    

    print '''
-----------------------------------------------------------
Podemos refazer o looping que imprime todos os dados do grafo
mas agora exibindo os labels e as cores dos nós
-----------------------------------------------------------
    '''
    for noOrigem in grf.grafo:
        for noDestino in grf.grafo[noOrigem]:
            print "Nó Origem: %s (%s) - Nó Destino: %s (%s) - Peso da Aresta: %s" % (grf.props[noOrigem]["label"], grf.props[noOrigem]["cor"], grf.props[noDestino]["label"], grf.props[noDestino]["cor"], grf.grafo[noOrigem][noDestino])

    

if __name__ == "__main__":
    main()
    


