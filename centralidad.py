def centralidad(grafo, n):
    resultado = []
    centrales = {}
    lista = list(grafo.obtener_identificadores())
    for i in range(0, 100):
        actual = random.choice(lista)
        aproximacion = aproximacion_de_apariciones(grafo, actual, 1, 0)
        for usuario, apariciones in aproximacion.items():
            centrales[usuario] = dic.get(usuario, 0) + apariciones
    ordenados = sorted(centrales.items(), key=lambda x:x[1])
    for i in range(len(ordenados) - 1, len(centrales) - n - 1, -1):
        resultado.insert(0, ordenados[i][0])
    return resultado
