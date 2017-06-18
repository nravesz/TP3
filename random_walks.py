def random_walks(grafo,vertice,n):
    actual=vertice
    recorridos={}
    for i in range (n):
        adyacentes=grafo.obtener_adyacentes(actual)
        if not actual in recorridos:
            recorridos[actual]=1
        else:
            recorridos[actual]+=1
        actual=random.choice(list(adyacentes))
    return recorridos
