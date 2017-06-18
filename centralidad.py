def centralidad(grafo, n):
    resultado = []
    centrales = {}
    lista = list(grafo.obtener_identificadores())
    for i in range(0, 100):
        actual = random.choice(lista)
        centrales = aproximacion_de_apariciones(grafo, centrales, actual, 5)
    centrales_ordenados = sorted(dic.items(), key=lambda x:x[1])
    for i in range()

def aproximacion_de_apariciones(grafo, dic, usuario,5):
    for i in range(0, 3):
        walks = random_walks(grafo,usuario,20)
        lista = sorted(walks.items(), key=lambda x:x[1])
        for usuario, apariciones in lista:
            dic[usuario] = dic[usuario].get(usuario, 0) + apariciones
    return dic



def random_walks(grafo,vertice,n):
    actual = vertice
    recorridos = {}
    for i in range (n):
        adyacentes = grafo.obtener_adyacentes(actual)
        if not actual in recorridos:
            recorridos[actual] = 1
        else:
            recorridos[actual] += 1
        actual = random.choice(list(adyacentes))
    return recorridos
