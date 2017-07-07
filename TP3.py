import csv 
import random
from collections import OrderedDict
from operator import itemgetter
import sys 

class _Nodo:
	def __init__(self,dato,prox=None,ant=None):
		self.dato=dato
		self.prox=prox
		
class Cola:
	def __init__(self):
		self.prim=None
		self.ult=None
	def encolar(self,dato):
		nuevo=_Nodo(dato)
		if self.ult is not None:
			self.ult.prox=nuevo
		else:
			self.prim=nuevo
		self.ult=nuevo
	def desencolar(self):
		if self.prim:
			valor=self.prim.dato
			self.prim=self.prim.prox
			if not self.prim:
				self.ult=None
			return valor
		else:
			raise ValueError("La cola está vacía")
	def esta_vacia(self):
		return self.prim is None

"""Clase grafo"""
class  Grafo:
	def __init__(self):
		self.grafo = {}
		self.cant_vertices = 0
		self.cant_aristas = 0
	def agregar_vertice(self, elemento):
		self.grafo[elemento] = {}
		self.cant_vertices += 1
	def eliminar_vertice(self, elemento):
		if elemento in self.grafo:
			for adyacente in self.grafo[elemento]:
				self.grafo[adyacente].pop(elemento)
				self.cant_aristas -= 1
			self.grafo.pop(elemento)
			self.cant_vertices -= 1
	def agregar_arista(self, elemento1, elemento2):
		if elemento1 not in self.grafo:
			self.agregar_vertice(elemento1)
		if elemento2 not in self.grafo:
			self.agregar_vertice(elemento2)
		self.grafo[elemento1][elemento2] = None
		self.grafo[elemento2][elemento1] = None
		self.cant_aristas += 2
	def eliminar_arista(self, elemento1, elemento2):
		if elemento1 in self.grafo[elemento2]:
			self.grafo[elemento1].pop(elemento2)
			self.grafo[elemento2].pop(elemento1)
			self.cant_aristas -= 1
		else:
			raise Exception("Los elementos no están conectados")
	def son_adyacentes(self, elemento1, elemento2):
		return (elemento1 in self.grafo[elemento2])
	def obtener_adyacentes(self, elemento):
		return self.grafo[elemento]
	def existe_vertice(self, elemento):
		valor = self.grafo.get(elemento)
		if valor == None:
			return False
		return True
	def obtener_identificadores(self):
		return self.grafo.keys()
	def cantidad_vertices(self):
		return self.cant_vertices
	def cantidad_aristas(self):
		return self.cant_aristas

"""Devuelve la cantidad de vertices a x distancia del vértice dado"""		
def distancias(grafo,vertice):
	visitados={}
	orden={}
	dic={}
	q=Cola()
	q.encolar(vertice)
	visitados[vertice]=True
	orden[vertice]=0
	while not q.esta_vacia() > 0:
		v=q.desencolar()
		for w in grafo.obtener_adyacentes(v):
			if w not in visitados:#ver si es necesaria!
				orden[w]=orden[v]+1
				if not orden[w] in dic:
					dic[orden[w]]=1
				else:
					dic[orden[w]]+=1
				visitados[w]=True
				q.encolar(w)
	for dist in dic:
		print("Distancia {}: {}".format(dist,dic[dist]))

"""Realiza un camino random y devuelve un diccionario con todos lo vértices que formaron parte del recorrido
y las veces que aparecieron en este si se repitieron"""
def random_walks(grafo,vertice,n):
	actual = vertice
	recorridos={}
	for i in range(n):
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

""" y puede ser 0:Que quede todo 1:solo sacar el usuario o 2:ni el mismo ni sus ady"""
def aproximacion_de_apariciones(grafo, usuario,n):
	dic = {}
	for i in range(10):
		walks = random_walks(grafo, usuario, n)
		for usuario, apariciones in walks.items():
			dic[usuario] = dic.get(usuario, 0) + apariciones
	return dic

def similares(grafo,usuario,n):
	usuario=str(usuario)
	n=int(n)
	dic=aproximacion_de_apariciones(grafo,usuario,10)
	if usuario in dic:
		dic.pop(usuario)
	result= sorted(dic.items(), key=lambda x: x[1])
	a=len(result)
	for y in range(a -1, a-n-1, -1):
		if y==a-n:
			print(result[y][0])
		else:
			print("{} ".format(result[y][0]),end="")
		
def recomendar(grafo,usuario,n):
	usuario=str(usuario)
	n=int(n)
	dic=aproximacion_de_apariciones(grafo,usuario,20)
	for v in grafo.obtener_adyacentes(usuario):
		if v in dic:
			dic.pop(v)
	if usuario in dic:
		dic.pop(usuario)
	result= sorted(dic.items(), key=lambda x: x[1])
	a=len(result)
	for y in range(a -1, a-n-1, -1):
		if y==a-n:
			print(result[y][0])
		else:
			print("{},".format(result[y][0]),end="")

def centralidad(grafo, n):
	resultado = []
	centrales = {}
	n=int(n)
	lista = list(grafo.obtener_identificadores())
	for i in range(100):
		actual = random.choice(lista)
		aproximacion = aproximacion_de_apariciones(grafo, actual, 100)
		for usuario, apariciones in aproximacion.items():
			centrales[usuario] = centrales.get(usuario, 0) + apariciones
	ordenados = sorted(centrales.items(), key=lambda x:x[1])
	for i in range(len(ordenados) - 1, len(centrales) - n - 1, -1):
		resultado.insert(0, ordenados[i][0])
	for y in range(len(resultado)):
		if y==len(resultado)-1:
			print(resultado[y])
		else:
			print("{} ".format(resultado[y]),end="")

def camino(grafo, origen, final):
	padre = {}
	orden = {}
	nivel = {}
	visitados = {}
	origen=str(origen)
	final=str(final)
	if grafo.existe_vertice(origen):
		padre[origen] = None
		nivel[0] = origen
		orden[origen] = 0
		orden, nivel = bfs_caminar(grafo, origen, final, padre, orden, nivel, visitados)
		camino = minimo_camino(grafo, origen, final, orden, nivel)
		x=len(camino)
		for i in range(x):
			if i==x-1:
				print(camino[i])
			else:
				print("{} -> ".format(camino[i]),end="")

def bfs_caminar(grafo, origen, final, padre, orden, nivel, visitados):
	q = Cola()
	q.encolar(origen)
	visitados[origen] = True
	while not q.esta_vacia() > 0:
		v = q.desencolar()
		if v == final:
			break
		else:
			for w in grafo.obtener_adyacentes(v):
				if w not in visitados:
					visitados[w] = True
					orden[w] = orden[v] + 1
					nivel[orden[v] + 1] = nivel.get(orden[v] + 1, []) + [w]
					padre[w] = v
					q.encolar(w)
	return orden, nivel

def minimo_camino(grafo, origen, final, orden, nivel):
	camino = []
	orden_final = orden[final]
	nivel_final = nivel[orden_final]
	actual = final
	for i in range(orden_final - 1, -1, -1):
		adyacentes_actual = grafo.obtener_adyacentes(actual)
		for w in adyacentes_actual:
			if w in nivel[i]:
				camino.insert(0, w)
				actual = w
				break
	camino.append(final)
	return camino

def estadistica(grafo):
	vertices = grafo.cantidad_vertices()
	aristas = grafo.cantidad_aristas()
	entrada = vertices/aristas
	densidad = (int)((2 * aristas)/ (vertices * (vertices - 1)))
	print("Estadisticas:")
	print("Cantidad de vértices: ", vertices)
	print("Cantidad de aristas: ", aristas)
	print("Promedio de entrada de cada vértice: {:.4}".format(entrada))
	print("Promedio de salida de cada vértice: {:.4}".format(entrada))
	print("Densidad del grafo: ", densidad)


def comunidades(grafo):
	lista_usuarios = label_propagation(grafo)
	print("Termino de crear la lista de usuarios")
	for comunidad, lista in lista_usuarios.items():
		if len(lista) > 2000 or len(lista) < 4:
			continue
		else:
			print("-Comunidad: {}".format(comunidad))
			print("Cantidad de integrantes: {}".format(len(lista)))
			print("Integrantes:")
			print(lista)
			print("\n")

def label_propagation(grafo):
	label = asignar_etiquetas(grafo)
	vertices = grafo.obtener_identificadores()
	ids = sorted(vertices, key=lambda k: random.random())
	for vertice in ids:
		etiqueta = hallar_etiqueta(grafo, label, vertice)
		label[vertice] = etiqueta
	label_lista_usuarios = {}
	for usuario, etiqueta in label.items():
		if etiqueta not in label_lista_usuarios:
			label_lista_usuarios[etiqueta] = [usuario]
		else:
			label_lista_usuarios[etiqueta].append(usuario)
	return label_lista_usuarios


def asignar_etiquetas(grafo):
	label = {}
	vertices = grafo.obtener_identificadores()
	etiqueta = 0 #0 de originalidad (no puedo poner tantas casas de GOT)
	for vertice in vertices:
		label[vertice] = etiqueta
		etiqueta += 1
	return label

def hallar_etiqueta(grafo, label, vertice):
	adyacentes = grafo.obtener_adyacentes(vertice)
	etiquetas_adyacentes = {}
	for adyacente in adyacentes:
		etiqueta = label[adyacente]
		etiquetas_adyacentes[etiqueta] = etiquetas_adyacentes.get(etiqueta, 0) + 1
	maximo, valor = max(etiquetas_adyacentes.items(), key=lambda x:x[1])
	return maximo
	
def generar_grafo(grafo,archivo):
	archivo = open(archivo)
	for linea in archivo:
		if linea[0] != "#":
			linea = linea.rstrip('\n').split("\t")
			grafo.agregar_arista(linea[0], linea[1])



"""---INTERFAZ---"""

def funciones():
	funciones={}
	funciones["distancias"]=(distancias,1)
	funciones["similares"]=(similares,2)
	funciones["recomendar"]=(recomendar,2)
	funciones["comunidades"]=(comunidades,0)
	funciones["camino"]=(camino,2)
	funciones["centralidad"]=(centralidad)
	funciones["estadistica"]=(estadistica,0)
	return funciones

def imprimir_dic(dic):
	for elem in dic:
		print("{}  ".format(elem),end="")
	print("\n")

def comprobar_parametros(lista,dic):
	if lista[0] in dic:
		largo=len(lista)
		parametros=dic[lista[0]][1]
		if not largo==parametros+1:
			return False
	return True


def pedir_input(dic):
	line=input("Ingrese el comando deseado: ")
	dic=funciones()
	funcion=line.split()
	while not funcion[0] in dic or comprobar_parametros(funcion,dic)==False:
		if funcion[0].lower() =="help":
			imprimir_dic(dic)
			line=input("Ingrese el comando deseado:")
		elif funcion[0].lower() == "exit":
			break
		else:
			print("El comando ingresado es incorrecto")
			line=input("Ingrese nuevamente el comando deseado: ")
		funcion=line.split()
	return funcion


def main():
	print("YOUTUBE")
	print("Espere unos momentos por favor...")
	grafo=Grafo()
	archivo=sys.argv[1]
	generar_grafo(grafo,archivo)
	print("Se ha cargado el archivo correctamente")
	print("Ingrese help para imprimir los comandos disponibles")
	print("Ingrese el comando deseado o exit para salir del programa")
	while True:
		func=funciones()
		funcion=pedir_input(func)
		if funcion[0].lower()=="exit":
			print("Adiós")
			break
		parametros= funcion[1:]
		func[funcion[0]][0](grafo,*parametros)

main()
