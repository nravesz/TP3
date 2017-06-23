def comunidades(grafo):
    contador_label, label_usuarios = label_propagation(grafo)
    ordenado = sorted(contador_label.items(), key=lambda x:x[1])
    for i in range(len(ordenado) - 1, -1, -1):
        if ordenado[i][0] > 20000:
            continue
        elif ordenado[i][0] < 4:
            break
        else:
            comunidad = ordenado[i][0]
            print("Comunidad: {}".format(comunidad))
            lista_usuarios = label_usuarios[comunidad]
            print("Cantidad de integrantes: {}".format(len(lista_usuarios)))
            print("Integrantes:")
            print(lista_usuarios)
    return

def label_propagation(grafo):
    label, contador_label = asignar_etiquetas(grafo)
    ids = grafo.obtener_identificadores()
    actual = random.choice(list(ids))
    n = int(grafo.cantidad_vertices()/4) # Elegido de forma arbitraria
    for i in range(0, n, 1):
        if len(grafo.obtener_adyacentes(actual)) > 0:
            apariciones = aproximacion_de_apariciones(grafo, actual, 15, 1) #si recibe 1 y 1, solo itera entre los adyacentes y nada mas
            apariciones = sorted(apariciones.items(), key=lambda x:x[1])
            if len(apariciones) > 0:
                usuario, cantidad = apariciones[0]
                label[actual] = label[usuario]
                contador_label[label[usuario]] = contador_label.get(label[usuario], 0) + 1
        actual = random.choice(list(ids))
    label_usuarios = {}
    for usuario, etiqueta in label.items():
        label_usuarios[etiqueta] = label_usuarios.get(etiqueta,[]) + [usuario]
    return contador_label, label_usuarios

def asignar_etiquetas(grafo):
    label = {}
    contador_label = {}
    vertices = grafo.obtener_identificadores()
    etiqueta = 0 #0 de originalidad (no puedo poner tantas casas de GOT)
    for vertice in vertices:
        label[vertice] = etiqueta
        contador_label[etiqueta] = contador_label.get(etiqueta, 0) + 1
        etiqueta += 1
    return label, contador_label
