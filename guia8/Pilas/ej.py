#PILAS
#Ejercicio 8
def generar_nros_al_azar(n:int,desde:int,hasta:int)->Pila:
    p:Pila = Pila()
    for i in range(0,n):
        p.put(random.randint(desde,hasta))
    return p
#print(generar_nros_al_azar(3,3,15))


# def generar_cola(cantidad:int,desde:int,hasta:int)->Cola[int]:
#     p:Pila[int]= generar_nros_al_azar(cantidad,desde,hasta)
#     c:Cola[int]=Cola()
#     while not p.empty():
#         num:int= p.get()
#         c.put(num)
#     return c
    
# cola = generar_cola(3, 0, 10)
# while not cola.empty():
#     print(cola.get())

#Ejercicio 9
pilarda = Pila()
pilarda.put(5)
pilarda.put(2)
pilarda.put(58)
pilarda.put(1)

def cantidad_de_elems(p:Pila)->int:
    contenido:Pila=[]
    contador:int=0 
    while not p.empty():
        contenido.append(p.get())
        contador+=1
    for elemento in contenido[::-1]:
        p.put(elemento)
    return contador
        
#print(cantidad_de_elems(pilarda))
#Ejercicio 10
def buscar_el_maximo(p:Pila)->int:
    maximo:int=p.get()
    while not p.empty():
        nuevo_elemento=p.get()
        if nuevo_elemento > maximo:
            maximo = nuevo_elemento
    return maximo

# print(buscar_el_maximo(pilarda))
