def similares(grafo,usuario,n):
    dic={}
    for i in range (3):#yo digo q lo haga tres veces el random walks pero se puede cambiar al toque
        walks=random_walks(grafo,usuario,100)#dps vemos de cambiar la cosa jejeje
        walks.pop(usuario)
        lista= sorted(walks.items(), key=lambda x: x[1]) 
        x=len(lista)
        cont=x-n-1
        while cont<x:
            if lista[cont][0] in dic:
                dic[lista[cont][0]]+=lista[cont][1]   
            else:
                dic[lista[cont][0]]=lista[cont][1]   
            cont+=1
    result= sorted(dic.items(), key=lambda x: x[1])
    a=len(result)
    aux=a-1
    while aux>a-n:
        print("{}-".format(result[aux][0]))
        aux-=1
