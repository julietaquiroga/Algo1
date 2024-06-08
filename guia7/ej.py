import math
#Ejercicio 1 (con for i in range)
def pertenece(s:list,e:int)->bool:
    res: bool= False
    for caracter in range(0,len(s),1):
        if caracter == e:
            res = True
    return res
#Ejercicio 1 (con while)
def perteneceW(s:list,e:int)->bool:
    i:int=0
    while i < len(s) and s[i]!=e:
        i+=1
    return i < len(s)
#Ejercicio 1(con if)
def perteneceif(s:list,e:int)->bool:
    res:bool = False
    if e in s:
        res = True
    else:
        res =False
    return res

#Ejercicio 2 
def divide_a_todosA(s:list,e:int)->bool:
    res:bool=False
    for i in range(0,len(s),1):
        if s[i]%e==0:
             res = True
        else:
            res = False
    return res
#Ejercicio 2 otra forma
def divide_a_todosB(s:list,e:int)->bool:
    res:bool
    for i in range(0,len(s),1):
        if s[i]%e!=0:
            res= False
        else:
            res= True
    return res

#Ejercicio 3 
def suma_total(s:list)->int:
    acum: int = 0
    i: int = 0
    while i < len(s):
        acum += s[i]
        i+=1
    return acum
def suma_totalB(s:list)->int:
    sumatoria:int=0
    for i in range(0,len(s),1):
        sumatoria = sumatoria + s[i]
    return sumatoria
       

#Ejercicio 4
def ordenados(s:list)->bool:
    res:bool= True
    for i in range(0,len(s)-1,1):
        if not(s[i]<s[i+1]):
            res=False
    return res
#por que sin el not no funciona, siempre devuelve True
#Ejercicio 5
def longitud_palabras(s:list)->bool:
    res:bool = False
    for palabra in s:
        if len(palabra)>7:
            res = True
    return res
#print(longitud_palabras(['julieta','otorrinolaringologo','hola']))
#Ejercicio 6
def es_palindromo(texto:str)->bool:
    res:bool = True
    for i in range(0,len(texto),1):
        if texto[i]!=texto[len(texto)-1-i]:
            res=False
    return res
#x[len(x)-1-i] recorro un string AL REVES!!!
#Ejercicio 7
#funcion si tiene una minus
def minuscula(contraseña:str)-> bool:
    res:bool=False
    for letra in contraseña:
        if 'a'<=letra<='z':
            res=True
    return res
#funcion si tiene una mayus
def mayuscula(contraseña:str)->bool:
    res:bool=False
    for letra in contraseña:
        if 'A'<=letra<='Z':
            res=True
    return res
#funcion si tiene numero
def numero(contraseña:str)->bool:
    res:bool=False
    for numero in contraseña:
        if '1'<=numero<='9':
            res=True
    return res
#ahora llamo la funcion principal
def fortaleza(contraseña:str)->str:
    res:str='AMARILLO'
    if len(contraseña)>8 and mayuscula(contraseña) and minuscula(contraseña) and numero(contraseña):
        res = print('VERDE')
    elif len(contraseña)<5:
        res = print('ROJO')
    else:
        print(res)
    return res
#contraseña = input("ingrese contraseña: ")
#essegura = fortaleza(contraseña)

#Ejercicio 8 devolver saldo actual del historial de movimientos de la cuenta bancaria
#si la tupla es ("I",000) ingresa dinero, por lo tanto se suma el monto-> +000
#si la tupla es ("R",111) retira dinero, por lo tanto se resta la segunda componente de la tupla -> -111 
def saldoactual(s:list)->int:
    res:int=0
    for i in range(0,len(s),1):
        if s[i][0]=="I":
            res= res+s[i][1]
        elif s[i][0]=="R":
            res= res-s[i][1]
    return res
s=saldoactual([("I",2)])
print(s)
#como hago para que no pueda ser negativo el monto?

#Ejercicio 9 Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso contrario.
def tresvocalesdist(palabra:str)->bool:
    res:bool=False
    lista:str=["A","E","I","O","U","a","e","i","o","u"]
    contador:int=0
    for letra in range(len(palabra)):
        for vocal in range(len(lista)):
            if palabra[letra]==lista[vocal]:
                contador +=1
                lista[vocal]="" 
    if contador>=3:
        res= True
    return res

#SEGUNDAPARTE
import math
import random
import numpy as np

#Ejercicio 2.1
def borrar_pares(s:list[int])->None:
    res:list[int]
    for i in range(0,len(s),2):
        s[i]=0
        
# s = [1, 2, 3, 4, 5, 6]
# borrar_pares(s)
# print(s)
#Ejercicio 2 Lo mismo del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista, igual a la anterior
#pero con las posiciones pares en cero, es decir, la lista pasada como par´ametro es de tipo in.
def borrar_paresB(s:list[int])->list[int]:
    res= s.copy()
    for i in range(0,len(res),1):
        if s[1]%2==0:
            res[1]=0
    return res

#print(borrar_paresB([1,2,3,4,5,6,7]))
#Ejercicio 2.3 Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
#sino que borra la vocal y concatena a continuaci´on.  
def borrar_vocales(palabra:str)->str:
    vocales=["A","E","I","O","U","a","e","i","o","u"]
    res:str="" 
    for letra in range(len(palabra)):     
        if pertenecestr(vocales,palabra[letra]):
            res=res
        else:
            res=res+palabra[letra]
    return res
    
def pertenecestr(vocales:str,letra:str)->bool:
    res:bool=False
    for v in range(len(vocales)):
        if vocales[v]==letra:
            res= True
    return res

#Ejercicio 2.4
# problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
# requiere: { T rue }
# asegura: {|res| = |s|}
# asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
# (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) }
def reemplaza_vocales(s:str)->str:
    vocales=["A","E","I","O","U","a","e","i","o","u"]
    res:str=""  
    for i in range(0,len(s),1):
        if pertenecestr(vocales,s[i]):
            res= res + " "
        else:
            res= res + s[i]
    return res

# test4=reemplaza_vocales(["j","u","l","i","e","t","a"])
# print(reemplaza_vocales(test4))

# Ejercicio 2.5
# . problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
# requiere: { T rue }
# asegura: {|res| = |s|}
# asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1]}
def da_vuelta_str(palabra:str)->str:
    res:str=""
    for l in range(len(palabra)):
        res = res + palabra[len(palabra)-l-1]
    return res

# Ejercicio 2.6
def eliminar_repetidos(palabra:str)->str:
    res:str=""
    for l in range(0,len(palabra),1):
        if pertenecestr(res,palabra[l]):
            res= res
        else:
            res= res + palabra[l]
    return res

# test6=eliminar_repetidos("papa")
# print(test6)

def pertenece(lista:list[int],numero)->bool:
    res:bool=False
    for n in range(0,len(lista),1):
        if lista[n]==numero:
            res = True
    return res

# test0=pertenece([1,2,3],2)
# print(test0)

#Ejercicio 3
# asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
# asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio est´a entre 4 (inclusive) y 7}
# asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
def aprobado(notas:int)->int:
    promedio:int= np.mean(notas)
    for i in range(len(notas)):
        if notas[i]>=4 and promedio>=7:
            res=1
        elif notas[i]>=4 and 4<=promedio<7:
            res=2
        elif notas[i]<4 and promedio<4:
            res=3
    return res


#Ejercicio 4.1
#funcion para construir una lista con nombres ingresado en input(), devuelve la lista con todos los nombres hasta q ingrese "listo"
def construir_lista()->list[str]:
    res:list[str]=[]
    nombre: str = (input("Nombre:"))
    while (nombre!="listo"):
        res.append(nombre)
        nombre = str(input("Nombre:"))
    return res


#Ejercicio 4.2
#funcion devuelve una lista con el historial de la sube(en"C" y "D",monto), en "X" fin
def historial_sube():
    print("Para cargar escriba C y luego el monto a cargar,para descontar D y el monto a descontar, para terminar reporte X.")
    c:int=0
    d:int=0
    monto:int=0
    res:list[tuple]=[]
    operacion:str=(input("Operacion a realizar:"))
    while operacion!="X":
        if operacion=="D":
            monto:int=(input("Monto a descontar:"))
            res=res + [("D",int(monto))]
        elif operacion=="C":
            monto:int=(input("Monto a cargar:"))
            res=res+ [("C",int(monto))]
        elif operacion!="X" and operacion!="C" and operacion!="D":
            print("NO VALID TRY AGAIN")
        operacion:str=(input("Operacion a realizar:"))
    return res

#Ejercicio 4.3 
# def sieteymedio():
#     print("A continuacion se te dará una carta, si desea sacar otra carta ingrese SI, si desea plantarse ingrese NO:")
#     x=random.randint(1,12)
#     w:int=0.5
#     posibles_valores=[1,2,3,4,5,6,7,10,11,12]
#     y=random.choice(posibles_valores)
#     lista_cartas:list=[]
#     lista_cartas.append(x)
#     if x>9:
#         print("Tu carta es: ",x)
#         print("Perdiste xD")
#     else:
#         print("Tu carta es",x)
#         res+=x
#         decision:str=(input("¿Desea sacar otra carta?: "))
#         while True:
#             if decision=="si":
#                 y=random.choice(posibles_valores)
#                 res+=y
#                 if res==7.5:
#                     print("Ganaste, tu carta fue:",y,", la suma de tus cartas fue:",res)
#                     break
#                 elif res<7.5:
#                     print("Tu nueva carta es:",y)
#                     print("La suma de tus cartas es:",res)
#                 elif (res)>7:
#                     print("Has perdido, tu nueva carta es",y,"y la suma de tus cartas llegó hasta",res)
#                     break
#             elif decision=="no" and res<7.5:
#                 print("La suma de tus cartas es:",res)
#                 print("Has ganado!")
#                 break
#             elif decision!="NO" or decision!="SI":
#                 print("Introduzca acción valida")
#             decision=input("Deseas sacar otra carta?:")
#     return lista_cartas
from typing import List

#Ejercicio 5.1
#auxiliar pertenece
def pertenece(s:list,e:int)->bool:
    res:bool=False
    for i in range(len(s)):
        if s[i]==e:
            res=True
    return res
# test=pertenece([1,2,3],8)
# print(test)
def pertenece_a_cada_unoA(s:list[int],e:int)->None:
    output:list[bool]=[]
    for i in range(0,len(s),1):
        if pertenece(s[i],e):
            output.append(True)
        else:
            output.append(False)
    return output        
              
# test51=pertenece_a_cada_unoA([[1,2,3],[3,4,5],[3,6,8],[]],5)
# print(test51)
#Ejercicio 5.3
def es_matriz(s:list[int])->bool:
    res:bool=True
    for i in range(len(s)):
        if len(s[i])!=len(s[0]):
            res=False
    return res
# test53=es_matriz([[1,2],[1,2],[1,2,3]])
# print(test53)

#Ejercicio 5.4
#funcion auxiliar ordenados
def ordenados(s:list[int])->bool:
    res:bool=True
    for i in range(0,len(s)-1,1):
        if s[i]>s[i+1]:
            res= False
    return res
# testo=ordenados([1,2,3,4,5,3])
# print(testo)
def filas_ordenadas(s:list[int])->None:
    output:list[bool]=[]
    if es_matriz(s)==True:
        for i in range(0,len(s),1):
            output.append(ordenados(s[i]))
        return output
# test54=filas_ordenadas([[1,2],[9,4]])
# print(test54)
