def similares(grafo,usuario,n):
    dic={}
    for i in range(0, 2):
        walks = random_walks(grafo,usuario,20)
        lista = sorted(walks.items(), key=lambda x:x[1])
        for usuario, apariciones in lista:
            dic[usuario] = dic[usuario].get(usuario, 0) + apariciones
    result = sorted(dic.items(), key=lambda x:x[1])
    for y in range(len(dic), len(dic)-n, -1):
        if y == len(dic) - n:
            print("{}".format(result[y][0]))
        else:
            print("{},".format(result[y][0]))
