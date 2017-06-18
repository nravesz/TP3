def estadistica(grafo):
    vertices = grafo.cantidad_vertices()
    aristas = grafo.cantidad_aristas()
    entrada = aproximar_cantidad_vertices(grafo)
    densidad = (int)((2 * aristas)/ (vertices * (vertices - 1)))
    print("Estadisticas:")
    print("Cantidad de vértices: ", vertices)
    print("Cantidad de aristas: ", aristas)
    print("Promedio de entrada de cada vértice: ", entrada)
    print("Promedio de salida de cada vértice: ", entrada)
    print("Densidad del grafo: ", densidad)

def aproximar_cantidad_vertices(grafo):
    entrada = 0
    for i in range(0, 100):
        actual = random.choice(list(grafo.obtener_identificadores()))
        entrada += len(grafo.obtener_adyacentes(actual))
    return (int)(entrada/100)
