def comunidades(grafo):
    contador_label = label_propagation(grafo)
    ordenado = sorted(contador_label.items(), key=lambda x:x[1])
    for i in range(0, len(ordenado) - 1, -1):
        if ordenado[i][0] > 20000:
            continue
        elif ordenado[i][0] < 4:
            break
        else:
            print("Comunidad: {}".format(ordenado[i][0]))
            print("Cantidad de integrantes: {}".format(len(ordenado[i]) - 1))
            print("Integrantes:")
            for j in range(1, len(ordenado[i]) - 1, 1):
                print("{}: {}".format(j, ordenado[j]))
    return

def label_propagation(grafo):
    label, contador_label = asignar_etiquetas(grafo)
    ids = grafo.obtener_identificadores()
    actual = random.choice(list(ids))
    n = int(vertices/4) # Elegido de forma arbitraria
    for i in range(0, n, 1):
        apariciones = aproximacion_de_apariciones(grafo, actual, 1, 1) #si recibe 1 y 1, solo itera entre los adyacentes y nada mas
        apariciones = sorted(apariciones.items(), key=lambda x:x[1])
        label[actual] = apariciones[0][1]
        contador_label[apariciones[0][1]] = dic.get(apariciones, 0) + 1
        actual = random.choice(list(ids))
    return contador_label

def asignar_etiquetas(grafo):
    label = {}
    contador_label = {}
    vertices = grafo.obtener_identificadores()
    etiqueta = 0 #0 de originalidad (no puedo poner tantas casas de GOT)
    for vertice in vertices:
        label[vertice] = etiqueta
        contador_label[etiqueta] = dic[etiqueta].get(etiqueta, 0) + 1
        etiqueta += 1
    return label, contador_label
