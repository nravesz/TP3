def comunidades(grafo):
    lista_usuarios= label_propagation(grafo)
    for comunidad, lista in lista_usuarios.items():
        if len(lista)>20000 or len(lista)<4:
            continue
        else:
            print("Comunidad: {}".format(comunidad))
            print("Cantidad de integrantes: {}".format(len(lista)))
            print("Integrantes:")
            print(lista)
    return

def label_propagation(grafo):
    label = asignar_etiquetas(grafo)
    ids = grafo.obtener_identificadores()
    actual = random.choice(list(ids))
    n = int(grafo.cantidad_vertices()/2)
    for i in range(0, n, 1):
        if len(grafo.obtener_adyacentes(actual)) > 0:
            apariciones = aproximacion_de_apariciones(grafo, actual, 1, 20)
            apariciones = sorted(apariciones.items(), key=lambda x:x[1])
            if len(apariciones) > 0:
                usuario, cantidad = apariciones[0]
                label[actual] = label[usuario]
        actual = random.choice(list(ids))
    label_lista_usuarios = {}
    for usuario, etiqueta in label.items():
        label_lista_usuarios[etiqueta] = label_lista_usuarios.get(etiqueta, []) + [usuario]
    return label_lista_usuarios

def asignar_etiquetas(grafo):
    label = {}
    vertices = grafo.obtener_identificadores()
    etiqueta = 0 #0 de originalidad (no puedo poner tantas casas de GOT)
    for vertice in vertices:
        label[vertice] = etiqueta
        etiqueta += 1
    return label
