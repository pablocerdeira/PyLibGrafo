# -*- coding:utf-8 -*-

from PyLibGrafo_criacao import *
from PyLibGrafo_conversao import *
from PyLibGrafo_plot import *
from PyLibGrafo_navegacao import *

class Grafo:

    # Atributos de Grafo
    grafo = []
    grafo_dicionario = grafo
    grafo_matriz = []
    grafo_tuplas = []

    def __init__(self):
        self.data = []
    
    def random(self,nNos = 50, minArestas = 1, maxArestas = 5, maxPeso = 10):
        self.grafo = cria_grafo_dicionario(nNos, minArestas, maxArestas, maxPeso)
        self.grafo_dicionario = self.grafo
        return self.grafo
        
    def converter(self,tipo="tuplas"):
        if tipo == "matriz":
            self.grafo_matriz = converter_grafo(self.grafo,tipo="matriz") 
            return self.grafo_matriz
        if tipo == "tuplas": 
            self.grafo_tuplas = converter_grafo(self.grafo,tipo="tuplas") 
            return self.grafo_tuplas
        
    def plota(self,engine="ubigraph",arquivo="grafo.png"):
        if engine == "ubigraph":    return plota_grafo_ubi(self.grafo_tuplas)
        if engine == "graph-tools": return plota_grafo_gt(self.grafo_tuplas,arquivo)
        if engine == "networkx":    return plota_grafo_nx(self.grafo_tuplas,arquivo)
        
    def bfs(self,inicio,fim):
        return bfs(self.grafo,inicio,fim)
        
    def dfs(self,inicio,fim):
        return dfs(self.grafo,inicio,fim)
        
    def r_dfs(self,inicio,fim):
        return r_dfs(self.grafo,inicio,fim,path=[])
        
        
        
        
        
        
        

