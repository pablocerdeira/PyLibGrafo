# -*- coding:utf-8 -*-

# Bibliotecas para graph_tool
from graph_tool.all import *

# Bibliotecas para o NetworkX
import xmlrpclib
import networkx as nx
import matplotlib.pyplot as plt

# ----------------------------------------------------------------
# FUNÇÕES PARA PLOTAGEM DOS GRAFOS
# ----------------------------------------------------------------

# Plota grafo utilizando a biblioteca Graph-Tools
def plota_grafo_gt(grafo,arquivo="grafoGraph-Tools.png"):

    g = Graph()
    v_id = g.new_vertex_property("int32_t")
    e_peso = g.new_edge_property("int32_t")

    # cria um conjunto com os vértices do grafo
    nos = set([])
    for key in grafo:
        nos.add(key[0])
        nos.add(key[1])

    # cria nós na mesma quantidade de vértices
    g.add_vertex(len(nos))

    # nomeia os vértices (v_id) com os nomes nós
    # e salva a relação em um dicionário
    nosIds = {}
    i = 0
    for item in nos:
        v_id[g.vertex(i)] = item
        nosIds[item] = g.vertex(i)
        i += 1

    for key in grafo:
        e = g.add_edge(g.vertex(nosIds[key[0]]),g.vertex(nosIds[key[1]]))
        e_peso[e] = int(grafo[key])
 
    graph_draw(g, size=(30,30), vprops={"label": v_id}, eprops={"penwidth": e_peso, "elen": e_peso}, layout="twopi", output=arquivo)
    return arquivo



# Plota grafo utilizando o Ubigraph
def plota_grafo_ubi(grafo):

    server_url = 'http://127.0.0.1:20738/RPC2'
    server = xmlrpclib.Server(server_url)
    g = server.ubigraph
    g.clear()

    # definições de estilos
    # estilo de vértice
    nBolaVermelha = g.new_vertex_style(0)
    g.set_vertex_style_attribute(nBolaVermelha, "shape", "sphere")
    g.set_vertex_style_attribute(nBolaVermelha, "shapedetail", "40")
    g.set_vertex_style_attribute(nBolaVermelha, "color", "#ff0000")

    # estilo de aresta
    vSeta = g.new_edge_style(0)
    g.set_edge_style_attribute(vSeta, "arrow", "true")
    g.set_edge_style_attribute(vSeta, "arrow_position", "1.0")
    g.set_edge_style_attribute(vSeta, "arrow_radius", "1.0")
    g.set_edge_style_attribute(vSeta, "arrow_lenght", "1.0")
    g.set_edge_style_attribute(vSeta, "oriented", "true")


    # cria um conjunto com os vértices do grafo
    nos = set([])
    for key in grafo:
        nos.add(key[0])
        nos.add(key[1])

    # plota os vértices
    for item in nos:
        g.new_vertex_w_id(item)
        g.change_vertex_style(item, nBolaVermelha)
        g.set_vertex_attribute(item,'label',str(item))

    # plota as arestas
    i = 0
    for key in grafo:
        g.new_edge_w_id(i, key[0], key[1])
        g.change_edge_style(i, vSeta)
        g.set_edge_attribute(i,'strength',str(abs(grafo[key])/1.8))
        g.set_edge_attribute(i,'width',str(abs(grafo[key])/1))
        i += 1

    return 1


# Plota grafo utilizando a biblioteca NetworkX
def plota_grafo_nx(grafo,arquivo="grafoNetworkX.png"):

    g = nx.DiGraph()

    # cria um conjunto com os vértices do grafo
    nos = set([])
    for key in grafo:
        nos.add(key[0])
        nos.add(key[1])

    # plota os vértices
    for item in nos:
        g.add_node(item)

    # plota as arestas
    i = 0
    for key in grafo:
        g.add_weighted_edges_from([(key[0], key[1], grafo[key])])
        i += 1

    nx.draw(g)
    plt.savefig(arquivo)

    return arquivo



# ----------------------------------------------------------------
# FUNÇÕES PARA PLOTAGEM DE TREES
# ----------------------------------------------------------------

# Plota tree utilizando a biblioteca Graph-Tools
def plota_tree_gt(grafo,arquivo="treeGraph-Tools.png"):

    g = Graph()
    v_id = g.new_vertex_property("int32_t")
    e_peso = g.new_edge_property("int32_t")

    # cria um conjunto com os vértices do grafo
    nos = set([])
    for galho in grafo:
        for ramo in galho:
            nos.add(ramo)
            for folha in galho[ramo]:
                nos.add(folha)

    nosDict = {}
    for no in nos:
        v = g.add_vertex()    
        v_id[v] = int(no)
        nosDict[no] = int(v)
    
    for galho in grafo:
        for ramo in galho:
            for folha in galho[ramo]:
                e = g.add_edge(g.vertex(nosDict[ramo]),g.vertex(nosDict[folha]))
                e_peso[e] = int(galho[ramo][folha])
 
    graph_draw(g, size=(30,30), vprops={"label": v_id}, eprops={"penwidth": e_peso, "elen": e_peso}, layout="dot", output=arquivo)

    return arquivo


# Plota tree utilizando o Ubigraph
def plota_tree_ubi(grafo):

    server_url = 'http://127.0.0.1:20738/RPC2'
    server = xmlrpclib.Server(server_url)
    g = server.ubigraph
    g.clear()

    # definições de estilos
    # estilo de vértice
    nBolaVermelha = g.new_vertex_style(0)
    g.set_vertex_style_attribute(nBolaVermelha, "shape", "sphere")
    g.set_vertex_style_attribute(nBolaVermelha, "shapedetail", "40")
    g.set_vertex_style_attribute(nBolaVermelha, "color", "#ff0000")

    # estilo de aresta
    vSeta = g.new_edge_style(0)
    g.set_edge_style_attribute(vSeta, "arrow", "true")
    g.set_edge_style_attribute(vSeta, "arrow_position", "1.0")
    g.set_edge_style_attribute(vSeta, "arrow_radius", "1.0")
    g.set_edge_style_attribute(vSeta, "arrow_lenght", "1.0")
    g.set_edge_style_attribute(vSeta, "oriented", "true")


    # cria um conjunto com os vértices do grafo
    nos = set([])
    for galho in grafo:
        for ramo in galho:
            nos.add(ramo)
            for folha in galho[ramo]:
                nos.add(folha)

    # plota os vértices
    for item in nos:
        g.new_vertex_w_id(item)
        g.change_vertex_style(item, nBolaVermelha)
        g.set_vertex_attribute(item,'label',str(item))

    # plota as arestas
    i = 0
    for galho in grafo:
        for ramo in galho:
            for folha in galho[ramo]:
                e = g.new_edge_w_id(i, ramo, folha)
                g.change_edge_style(i, vSeta)
                g.set_edge_attribute(i,'strength',str(abs(int(galho[ramo][folha]))/1.8))
                g.set_edge_attribute(i,'width',str(abs(int(galho[ramo][folha]))/1))
                i += 1

    return 1


# Plota tree utilizando a biblioteca NetworkX
def plota_tree_nx(grafo,arquivo="treeNetworkX.png"):

    g = nx.DiGraph()

    # cria um conjunto com os vértices do grafo
    nos = set([])
    for galho in grafo:
        for ramo in galho:
            nos.add(ramo)
            for folha in galho[ramo]:
                nos.add(folha)

    # plota os vértices
    for item in nos:
        g.add_node(item)

    # plota as arestas
    i = 0
    for galho in grafo:
        for ramo in galho:
            for folha in galho[ramo]:
                g.add_weighted_edges_from([(ramo, folha, galho[ramo][folha])])
                i += 1

    nx.draw(g)
    plt.savefig(arquivo)

    return arquivo









