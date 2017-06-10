int procesar_usuarios(char* nom_archivo){
	
	FILE *archivo;
	archivo = fopen( nom_archivo,"r");
	if (!archivo){
		printf("Error al abrir el archivo\n");
		return -1;
	}
	
	hash_t* hash= hash_crear(NULL);
	
	char* str = NULL;
	size_t n;
	ssize_t largo_linea= getline(&str, &n, archivo);
	
	while(largo_linea!=-1){
		
		char** arreglo= split(str,',');
		int contador=0;
		char* usuario= arreglo[0];
		for(int i=1;arreglo[i]!=NULL;i++){
			contador=contador+1;
		}
		if(hash_pertenece(hash,usuario)){//osea ya está de antes
			void* cont = hash_obtener(hash,usuario);
			contador+= (int) cont;
		}
		hash_guardar(hash,usuario,(void*)contador);
		free(str);
		free_strv(arreglo);
		str = NULL;
		largo_linea=getline(&str,&n,archivo);
	}
	if (str){
		free str;
	}
  
	hash_iter_t* iter= hash_iter_crear(dic);
	void** arreglo= malloc(sizeof(void*) * hash_cantidad(dic));
	for(int i=0; i<=hash_cantidad(dic);i++){
	char* clave = hash_iter_ver_actual(iter);
	void* dato = hash_obtener(hash, clave)
		nodo_h_t* nodo = nodo_h_crear(clave, dato);
		arreglo[i] = nodo;
		hash_iter_avanzar(iter);
	}
	ordenar_nombres(arreglo, hash_cantidad(hash), cmp);
	
	hash_iter_destruir(iter);
	hash_destruir(hash);
	fclose(archivo);
	return 0;
}
  
void ordenar_nombres(void** arreglo, int largo, cmp_func_t cmp){
  heap_t* heap = heap_crear_arr((void*)arreglo, k, cmp);
  // Encolo los elementos
  for (int i = o; i < largo; i++){
    heap_encolar(heap, &arreglo[i]);
  }
  int cantidad = 0;
  // Imprimo
  while (!heap_esta_vacio(heap)){
	nodo_t* nodo = heap_desencolar(heap);
	if (nodo_dato(nodo) != cantidad):
		printf("%i: %s", nodo_dato(nodo), nodo_clave(nodo));
	}
	else{
		printf(", %s", nodo_clave(nodo));
	}
}

//Para que compare de menor a mayor
int comparar_nodos_inverso (nodo_h_t* nodo_1, nodo_h_t* nodo_2){
	if (nodo_1->dato > nodo_2->dato)return -1;
	if(nodo_1->dato == nodo_2->dato)return 0;
	else{
		return 1;
		} //ver de dar vuelta
}