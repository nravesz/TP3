import random
from collections import OrderedDict
from operator import itemgetter

class Grafo:
    def __init__(self):
        self.grafo = {}
        self.cant_vertices = 0
        self.cant_aristas = 0
    def agregar_vertice(self, elemento):
        self.grafo[elemento] = {}
        self.cant_vertices += 1
    def eliminar_vertice(self, elemento):
        if elemento in self.grafo:
            for adyacente in self.grafo[elemento]:
                self.grafo[adyacente].pop(elemento)
                self.cant_aristas -= 1
            self.grafo.pop(elemento)
            self.cant_vertices -= 1
    def agregar_arista(self, elemento1, elemento2):
        self.grafo[elemento1][elemento2] = None
        self.grafo[elemento2][elemento1] = None
        self.cant_aristas += 1
    def eliminar_arista(self, elemento1, elemento2):
        if elemento1 in self.grafo[elemento2]:
            self.grafo[elemento1].pop(elemento2)
            self.grafo[elemento2].pop(elemento1)
            self.cant_aristas -= 1
        else:
            raise Exception("Los elementos no están conectados")
    def son_adyacentes(self, elemento1, elemento2):
        return (elemento1 in self.grafo[elemento2])
    def obtener_adyacentes(self, elemento):
        return self.grafo[elemento]
    def existe_vertice(self, elemento):
        valor = self.grafo.get(elemento)
        if valor == None:
            return False
        return True
    def obtener_identificadores(self):
        return self.grafo.keys()
    def cantidad_vertices(self):
        return self.cant_vertices
    def cantidad_aristas(self):
        return self.cant_aristas

def crear_grafo():
    grafo = Grafo()
    grafo.agregar_vertice("Genji")
    grafo.agregar_vertice("Pharah")
    grafo.agregar_vertice("McCree")
    grafo.agregar_vertice("Reaper")
    grafo.agregar_vertice("Sombra")
    grafo.agregar_vertice("Tracer")
    grafo.agregar_vertice("Hanzo")
    grafo.agregar_vertice("Mei")
    grafo.agregar_vertice("Widow")
    grafo.agregar_vertice("DVA")
    grafo.agregar_vertice("Reinhardt")
    grafo.agregar_vertice("Zarya")
    grafo.agregar_vertice("Ana")
    grafo.agregar_vertice("Lucio")
    grafo.agregar_vertice("Mercy")
    grafo.agregar_vertice("Symmetra")
    grafo.agregar_vertice("Soldier")
    grafo.agregar_vertice("Zenyatta")
    grafo.agregar_arista("Genji", "Hanzo")
    grafo.agregar_arista("Genji", "McCree")
    grafo.agregar_arista("Genji", "Pharah")
    grafo.agregar_arista("Genji", "Reaper")
    grafo.agregar_arista("Pharah", "Ana")
    grafo.agregar_arista("Pharah", "Mercy")
    grafo.agregar_arista("Tracer", "Sombra")
    grafo.agregar_arista("Tracer", "Ana")
    grafo.agregar_arista("Tracer", "Lucio")
    grafo.agregar_arista("Tracer", "Mercy")
    grafo.agregar_arista("Tracer", "Widow")
    grafo.agregar_arista("Tracer", "Reinhardt")
    grafo.agregar_arista("McCree", "Hanzo")
    grafo.agregar_arista("McCree", "Pharah")
    grafo.agregar_arista("McCree", "Ana")
    grafo.agregar_arista("McCree", "Reaper")
    grafo.agregar_arista("McCree", "Sombra")
    grafo.agregar_arista("Reaper", "Soldier")
    grafo.agregar_arista("Reaper", "Ana")
    grafo.agregar_arista("Reaper", "Sombra")
    grafo.agregar_arista("Reaper", "Widow")
    grafo.agregar_arista("Reaper", "Soldier")
    grafo.agregar_arista("Sombra", "Widow")
    grafo.agregar_arista("Sombra", "Symmetra")
    grafo.agregar_arista("Tracer", "Widow")
    grafo.agregar_arista("Tracer", "Lucio")
    grafo.agregar_arista("Tracer", "Reinhardt")
    grafo.agregar_arista("Tracer", "Mercy")
    grafo.agregar_arista("Mei", "Mercy")
    grafo.agregar_arista("Mei", "DVA")
    grafo.agregar_arista("Mei", "Soldier")
    grafo.agregar_arista("Mei", "Zarya")
    grafo.agregar_arista("Ana", "Reinhardt")
    grafo.agregar_arista("Ana", "Soldier")
    grafo.agregar_arista("Mercy", "Soldier")
    return grafo

def random_walks(grafo,vertice,n):
    actual = vertice
    recorridos={}
    for i in range(0, n):
        adyacentes = grafo.obtener_adyacentes(actual)
        if not actual in recorridos:
            recorridos[actual]=1
        else:
            recorridos[actual]+=1
        actual = random.choice(list(adyacentes))
    return recorridos

def similares(grafo,usuario,n):
    dic={}
    for i in range(0, 3):
        walks = random_walks(grafo,usuario,100)
        lista = sorted(walks.items(), key=lambda x:x[1])
        for usuario, apariciones in lista:
            if usuario in dic:
                dic[usuario] += apariciones
            else:
                dic[usuario] = apariciones
    result = sorted(dic.items(), key=lambda x:x[1])
    if usuario in result:
        result.remove(usuario)
    for y in range(len(result) - 1, len(result) - n -1, -1):
        if y == len(result) - n:
            print("{}.\n".format(result[y][0]))
        else:
            print("{}, ".format(result[y][0]),  end='')

grafo = crear_grafo()
similares(grafo, "Tracer", 3)
