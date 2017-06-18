class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError
        return self.items.pop(0)
    def esta_vacia(self):
        return len(self.items) == 0

def caminos(grafo, origen, final):
    padre = {}
    orden = {}
    nivel = {}
    visitados = {}
    if grafo.existe_vertice(origen):
        padre[origen] = None
        nivel[0] = origen
        orden[origen] = 0
        orden, nivel = bfs_caminar(grafo, origen, final, padre, orden, nivel, visitados)
        camino = minimo_camino(grafo, origen, final, orden, nivel)
        return camino

def bfs_caminar(grafo, origen, final, padre, orden, nivel, visitados):
    q = Cola()
    q.encolar(origen)
    visitados[origen] = True
    while not q.esta_vacia() > 0:
        v = q.desencolar()
        if v == final:
            break
        else:
            for w in grafo.obtener_adyacentes(v):
                if w not in visitados:
                    visitados[w] = True
                    orden[w] = orden[v] + 1
                    nivel[orden[v] + 1] = nivel.get(orden[v] + 1, []) + [w]
                    padre[w] = v
                    q.encolar(w)
    return orden, nivel

def minimo_camino(grafo, origen, final, orden, nivel):
    camino = []
    orden_final = orden[final]
    nivel_final = nivel[orden_final]
    actual = final
    for i in range(orden_final - 1, -1, -1):
        adyacentes_actual = grafo.obtener_adyacentes(actual)
        for w in adyacentes_actual:
            if w in nivel[i]:
                camino.insert(0, w)
                actual = w
                break
    camino.append(final)
    return camino
