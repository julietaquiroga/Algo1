#PROBABLEMENTE MUCHAS COSAS ESTEN MAL POIRQUE NO ENTENDIA LA DIFERENCIA ENTRE PRINT Y RETURN XD
#Ejercicio 1.1
def imprimir_hola_mundo():
        print("Hola Mundo")

#Ejercicio 1.2
def imprimir_un_verso():
        print("La cucaracha\nLa cucharacha \nYa no puede caminar")
        
import math
#Ejercicio 1.3
def raizde2():
        print (round (math.sqrt(2),4))
        
#Ejercicio 1.4
def factorial_2():
        print(math.factorial(2))

#Ejercicio 1.5
def perimetro():
        print(2*math.pi)

#Ejercicio 2.1
def imprimir_saludo (nombre:str):
        print("Hola" + nombre)
              
#Ejercicio 2.2
def raiz_cuadrada_de(numero: int):
        print(math.sqrt(numero))

#Ejercicio 2.3
def fahrenheit_a_celcius(t:float):
        print(((t-32)*5)/9)
    
#Ejercicio 2.4
def imprimir_dos_veces(estribillo:str):
        print(estribillo*2)
    
#Ejercicio 2.5
def es_multiplo_de(n:int,m:int)-> bool:
        print( n%m==0)

#Ejercicio 2.6
def es_par(numero:int)-> bool:
        print(es_multiplo_de(numero,2))
    
#Ejercicio 2.7
def cantidad_de_pizzas(comensales:int,min_cant_de_porciones:int)->int:
    print(math.ceil(comensales*min_cant_de_porciones/8))

#Ejercicio 3.1
def alguno_es_0(numero1:int, numero2:int)->int:
        print(numero1==0 or numero2==0)

#Ejercicio 3.2
def ambos_son_0(numero1:int,numero2:int)-> int:
        print(numero1==0 and numero2==0)

#Ejercicio 3.3
def es_nombre_largo(nombre:str)-> bool:
        print(3<=len(nombre)<=8)

#Ejercicio 3.4
def es_bisiesto(año:int)-> bool:
        print(año%400==0 or (año%4==0 and año%100!=0))
    
#Ejercicio 4
def peso_pino(altura:float)->float:
    res:float
    if altura<=3:
            res= 3*altura/0.01
    else:
        res= 900+((altura-3)*2/0.01)
    return res
    
def es_peso_util(peso:float)->str:
    res:str
    if 400<=peso<=1000:
        return "nos sirve tu pino"
    else: 
        res = "no nos sirve tu pinito"
        return res
    
def sirve_pino(altura:float)->str:
    res:str
    if (1.3333333333333333<= altura<=3.5) :
     res="nos sirve tu pino reyyy"
    else :
     res="flaco tu pino es una mierda"
    return res

def sirve_pino_comp(altura:float)->str:
    res:str
    if es_peso_util(peso_pino(altura))==True:
        res="nos sirve tu pino reyyy"
    else :
        res ="tu pino es una mierda"
    return res
#revisar, me da un res equivocado

#Ejercicio 5.1
def devolver_el_doble_si_es_par(numero:int)->int:
    res:int
    if numero%2==0:
        res = 2*numero
    else : 
        res = numero
    return res

#Ejercicio 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int)-> int:
    res:int
    if numero%2==0:
        res = numero
    else : 
        res = numero+1
    return res
#como implementar la funcion usando 2 if?

#Ejercicio 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int:
    res:int
    if numero%9==0:
        res = 3*numero
    elif numero%3!=0:
        res = 2*numero
    else :
        res = numero
    return res

#Ejercicio 5.4
def lindo_nombre(nombre:str)->str:
    res:int
    if len(nombre)>=5:
        res = "Tu nombre tiene muchas letras"
    else :
        res = "Tu nombre tiene menos de 5 caracteres"
    return res
#Ejercicio 5.5
def elRango(numero:int)->str:
    res:str
    if numero<5:
        res = "Menor a 5"
    elif numero>=10 and numero<=20:
        res = "Entre 10 y 20"
    else: 
        res = "Mayor a 20"
    return res

#Ejercicio 5.6
def vacaciones(sexo:str,edad:int)->str:
    res:str
    if edad<18 and(sexo=='F'or sexo=='M'):
        res="Anda de vacas chaval"
    elif 18<=edad<60 and(sexo=='F'or sexo=='M') :
        res="agarra la pala"
    elif edad>=60 and sexo=='F' : 
        res="disfrute señora"
    elif edad>=65 and sexo=='M' : 
        res="disfrute señor"
    return res
#caso M 60-65?
#Ejercicio 6.1
def numeros_del_1_al_10(contador:int):
    contador: int=1
    while contador<=10:
        print(contador)
        contador+=1
        contador <=10
        
#pq me imprime None cuando printeo
#Ejercicio 6.2
def pares_del_10_al_40(i:int):
    i: int=10
    while i<=40:
        print(i)
        i+=2
        i<=40
#otra forma
def hasta_40(inicio:int):
    for i in range(inicio,41,1):
     if i%2==0: 
        print (i)
#Ejercicio 6.3
def imprime_eco_10_veces(contador:int):
    contador : int=1
    while contador <=10:
        print("eco")
        contador +=1
        contador <=10
#otra forma
def imprime_10_veces_eco():
    i: int=1
    for i in range (0,10,1):
        print("eco")
