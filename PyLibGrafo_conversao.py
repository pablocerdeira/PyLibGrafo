# -*- coding:utf-8 -*-

# Importando bibliotecas para matrizes
from sympy import pprint
from sympy import Symbol
from sympy.matrices import *
import sys


# ----------------------------------------------------------------------
# Converte grafo
# ----------------------------------------------------------------------
def converter_grafo(grafo, tipo):

    if tipo == "matriz":
        linhas = []
        nosOrigem = grafo.keys()                                                
        for noOrigem in nosOrigem:
            for noDestino in grafo[noOrigem]:
                linha = [0]*len(nosOrigem)                                      
                linha[noOrigem] = grafo[noOrigem][noDestino]
                linha[noDestino] = grafo[noOrigem][noDestino] * (-1)
                linhas.append(linha)
        return Matrix(linhas)

    if tipo == "tuplas":
        tuplas = {}
        nosOrigem = grafo.keys()                                                
        for noOrigem in nosOrigem:
            for noDestino in grafo[noOrigem]:
                tuplas[noOrigem,noDestino] = grafo[noOrigem][noDestino]
        return tuplas


