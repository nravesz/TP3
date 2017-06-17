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
