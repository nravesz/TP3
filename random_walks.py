def random_walks(grafo,vertice,n):
    actual = vertice
    recorridos={}
    for i in range(0, n):
        adyacentes = grafo.obtener_adyacentes(actual)
        if not actual in recorridos:
            recorridos[actual] = 1
        else:
            recorridos[actual] += 1
        if len(adyacentes) > 0:
            actual = random.choice(list(adyacentes))
        else:
            break
    return recorridos
