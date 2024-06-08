# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def ultima_aparicion(s: list, e: int) -> int:
    res:int=0
    i:int=0
    for i in range(len(s)-1,-1,-1):
        if s[i]==e:
            res=i
            break
    return res
        
#print(ultima_aparicion([1,2,3,1,3],3))
##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def eliminar_rep(l:list)->list:
    res:list=[]
    for i in range(len(l)):
        if l[i] not in res:
            res+=[l[i]]
    return res
#print(eliminar_rep([-1,4,0,4,3,0,100,0,-1,-1]))            
def elementos_exclusivos(s:list,t:list)->list:
    eliminar_rep(s)
    eliminar_rep(t)
    res:list=[]
    for i in range(len(s)):
        if (s[i] not in t) and (s[i] not in res):
            res+=[s[i]]
    for j in range(len(t)):
        if (t[j] not in s) and (t[j] not in res):
            res+=[t[j]]
    return res
#print(elementos_exclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5]))

##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res:int=0
    for k in ingles.keys():
        if ingles.get(k)==aleman.get(k):
            res+=1 
    return res   
    
#print(contar_traducciones_iguales({"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"},{"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}))

##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

def eliminar_repes(l:list)->list:
    res:list=[]
    for i in range(len(l)):
        if l[i] not in res:
            res+=[l[i]]
    return res
#print(eliminar_repes([-1,4,0,4,3,0,100,0,-1,-1]))   
def cantidad_de_apariciones(s:list,n:int)->int:
    contador:int=0
    i:int=0
    for i in range(len(s)):
        if s[i]==n:
            contador+=1
    return contador
#print(cantidad_de_apariciones([1,2,3,3,3],23))
 
def convertir_a_diccionario(lista: list) -> dict:
    diccionario:dict[int,int]={}
    listaAux:list=eliminar_repes(lista) #VA A SER LA LISTA SIN REPETIDOS [-1,0,4,100]
    for i in range(len(listaAux)):
        diccionario[listaAux[i]]=cantidad_de_apariciones(lista,listaAux[i])  #lista.count(listaAux[i])
    return diccionario
#print(convertir_a_diccionario([-1, 0, 4, 100, 100, -1, -1]))

  
