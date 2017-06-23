def aproximacion_de_apariciones(grafo, usuario, y,n):
    dic = {}
    for i in range(10):
        walks = random_walks(grafo, usuario, n)
        for usuario, apariciones in walks.items():
            dic[usuario] = dic.get(usuario, 0) + apariciones
    if y == 1 or y == 2:
        dic.pop(usuario)
        if y == 2:
            for v in grafo.obtener_adyacentes(usuario):
                if v in dic:
                    dic.pop(v)		
    return dic
