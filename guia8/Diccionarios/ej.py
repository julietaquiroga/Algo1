#DICCIONARIOS
#Ejercicio 19         
def separarEnPalabras(texto:str)->list[str]: #funcion split
    temp:str=""
    res:list[str]=[]
    i:int=0
    while i < len(texto):
        if esUnEspacio(texto[i]):
            res.append(temp)
            temp=""
            while i < len(texto) and esUnEspacio(texto[i]):
                i+=1
        else:
            temp+=texto[i]
            i+=1
    res.append(temp) 
    return res

def agrupar_por_longitud(nombre_archivo:str)->dict[int, int]:
    file=open(nombre_archivo,"r")
    contenido=file.read()
    file.close()
    
    listaDePalabras:list[str]= separarEnPalabras(contenido)
    diccionario:dict[int,int]={}
    
    for palabra in listaDePalabras:
        clave:int=len(palabra)
        if clave in diccionario:
            diccionario[clave]+=1
        else:
            diccionario[clave]=1
    return diccionario
        
#print(agrupar_por_longitud("archivos.txt"))

#Ejercicio 21

def cantidad_de_apariciones(nombre_archivo:str)->dict:
    file= open(nombre_archivo,"r")
    contenido= file.read()
    file.close()
    listadePalabras:list[str]=separarEnPalabras(contenido)
    diccionario:dict[str,int]={}
    for palabra in range(len(listadePalabras)):
        if palabra in diccionario:
            diccionario[palabra]+=1
        else:
            diccionario[palabra]=1
    return diccionario
#print(cantidad_de_apariciones("archivos.txt"))
            
def palabra_mas_frecuente(nombre_archivo:str)->str:        
    res:str=""
    diccionario=cantidad_de_apariciones(nombre_archivo)
    frecmax:int=0
    for palabra in diccionario:
        if diccionario[palabra]>=frecmax:
            frecmax==diccionario[palabra]
            res=palabra
    return res
#print(palabra_mas_frecuente("archivos.txt"))
#REVISAR CODIGO NO FUNCIONA UNA MIERDA ME DEVUELVE CUALQUIER COSA

#Ejercicio 22

historiales: dict = {}
historiales_aux: dict = {}
def visitar_sitio(historiales: dict, usuario: str, sitio: str):
    historial: Pila = Pila()
    historial.put(sitio)
    historiales[usuario] = historial

def navegar_atras(historiales: dict, usuario: str):
    historial: Pila = historiales[usuario]
    x = historial.get()
    historiales_aux[usuario] = x
    return x

def navegar_adelante(historiales: dict, usuario: str, y=historiales_aux):
    visitar_sitio(historiales, usuario, historiales_aux[usuario])

"""visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "pornhub.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_adelante(historiales, "Usuario1")"""     
