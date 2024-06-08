import random
#Ejercicio 1.1
def contar_lineas(nombre_archivo:str)->int:
    f=open(nombre_archivo)
    print(len(f.readlines()))
    f.close()
    return

#test11=contar_lineas("archivos.txt")
#Ejercicio 1.2
def existe_palabra(palabra:str,nombre_archivo:str)->bool:
    archivo=open(nombre_archivo)
    for line in archivo:
        if palabra in line:
            return True
    return False
        
# print(existe_palabra("hola","archivos.txt"))

#funciones auxiliares para .split y texto a lista de palabras    
def esUnEspacio(palabra:str)->bool:
    res:bool=False
    if palabra==" " or palabra=="\n" or palabra=="\t": #esto no es un comentario
        res=True
    return res
  
def rebanar(linea:str)->list[str]: #.split()
    temp:str=""
    i:int=0
    res:list[str]=[]
    while i < len(linea):
        if esUnEspacio(linea[i]):
            res.append(temp)
            temp=""
        else:
            temp+=(linea[i])
        i+=1
    res.append(temp)
    return res

def texto_a_lista_de_palabras(nombre_archivo:str)->list:
    lista:list=[]
    archivo= open(nombre_archivo,"r")
    linea=archivo.readline()
    while linea:
        palabras=rebanar(linea)
        lista.extend(palabras)
        linea=archivo.readline()
    archivo.close()
    return lista 
#Ejercicio 1.3
def cant_apariciones(nombre_archivo:str,palabra:str)->int:
    archivo=open(nombre_archivo,"r")
    contador:int=0
    contenido:list=texto_a_lista_de_palabras(nombre_archivo)
    for i in range(len(contenido)):
        if contenido[i] == palabra:
            contador+=1
        else:
            contador
    return contador
#Ejercicio 2
def es_un_comentario(linea:str)->bool:
    res:bool=False
    for i in range(len(linea)):
        if linea[i]!=" ":
            if linea[i]=="#":
                res=True
            break
    return res
    
    
    
def clonar_sin_comentarios(nombre_archivo:str):
    salida: list[str] = []
    #1 abro el archivo
    f_in=open(nombre_archivo)
    #2 miro cada una de las lineas
    contenido= f_in.readlines()
    for linea in contenido:
        #2.1 si es un comentario, lo ignoro
        #2.2 si no es un comentario lo guardo, .append
        if not es_un_comentario(linea):
            salida.append(linea)
    #3 cierro el archivo
    f_in.close()    
    #4 abrirr el archivo clonado
    nombre_archivo_clonado= "clonado_" + nombre_archivo
    f_out= open(nombre_archivo_clonado,"w")
    #5 copiar las lineas
    f_out.writelines(salida)
    #6 cerrarlo
    f_out.close()

#Ejercicio 3
def invertir_lineas(nombre_archivo:str):
    salida:list[str]=[]
    #1 abrir el archivo
    f_in=open(nombre_archivo)
    #2 copiar las lineas
    contenido= f_in.readlines()
    for linea in contenido:
        salida.append(linea)
    #3 cerrar el archivo
    f_in.close()
    #4 abrir el clonado(cambiar nombre arch clonado=reverso.txt)
    f_out=open("reverso.txt","a")
    #5 pegar las lineas dadas vuelta
    for linea in salida:
        f_out.write(linea)
    #6 cerrar reverso.txt
    f_out.close()

#Ejercicio 4
def agregar_frase_al_final(nombre_archivo:str,frase:str):
    #abro el archivo
    f=open(nombre_archivo,"a")
    #+ frase al final del archivo
    f.write(frase)
    #cierro el archivo
    f.close()
#Ejercicio 5
def agregar_frase_al_principio(nombre_archivo:str,frase:str):
    archivo=open(nombre_archivo,"r")
    contenido=archivo.read()
    archivow=open(nombre_archivo,"w")
    archivow.write(frase + "\n" + contenido)
    archivo.close()

#Ejercicio 7
#def promedio_estudiante(nombre_archivo:str ,lu:str)-> float:
#def calcular_promedio_por_estudiante(nombre_archivo_notas:str,nombre_archivo_promedios:str):
