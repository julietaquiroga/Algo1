#COLAS
#Ejercicio 13 generar numeros al azar pero encolados
def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Cola[int]:
    salida:Cola[int]=Cola()
    for i in range(0,len(cantidad)):
        salida.put(random.randint(desde,hasta))
    return salida

#Ejercicio 14
def cant_de_elementos(c:Cola)->int:
    contador:int=0
    contenido:Cola=Cola()
    while not c.empty():
        contenido.append(c.put())
        contador+=1
    for i in contenido:
        c.put()
    return contador
        
#Ejercicio 15
def buscar_el_maximo(c:Cola)->int:
    maximo:int=c.get()
    while not c.empty():
        nuevo_elemento=c.get()
        if nuevo_elemento > maximo:
            maximo = nuevo_elemento
    return maximo             

#probemosla
# colita:Cola[int]=Cola()
# colita.put(6)
# colita.put(86)
# colita.put(1)
# print(buscar_el_maximo(colita))

#Ejercicio 16.1 armar secuencia de numeros desordenados del 0 al 99(bolillero)
def armar_sec_de_bingo()->Cola[int]:
    listaDeBolillas:list[int]=[]
    for bolilla in range(99):
        listaDeBolillas.append(bolilla)
    
    random.shuffle(listaDeBolillas)    #mezclo las bolillas
    
    bolillero: Cola [int] = Cola()
    for b in listaDeBolillas:
        bolillero.put(b)   
    return bolillero
#Ejercicio 16.2 jugar carton
def jugar_carton_de_bingo(carton:list[int],bolillero:Cola[int])->int:
    contadorjugadas:int=0
    bolilleroAux: Cola = Cola()
    cantSinMarcar:int=len(carton)
    while cantSinMarcar>0:
        bolilla:int=bolillero.get()
        bolilleroAux.put(bolilla)
        if bolilla in carton:
            cantSinMarcar-=1
        contadorjugadas+=1
    
    while not bolillero.empty(): # vacio por completo el bolillero
        bolilla:int=bolillero.get()
        bolilleroAux.put(bolilla)

    while not bolilleroAux.empty(): # regenero el bolillero
        bolilla:int=bolilleroAux.get()
        bolillero.put(bolilla)

    return contadorjugadas
bolillero = armar_sec_de_bingo()
carton = [13,74]

#print(list(bolillero.queue))
#print(jugar_carton_de_bingo(carton,bolillero))
#Ejercicio 17
def n_pacientes_urgentes(c:Cola[(int,str,str)])->int:
    contador:int=0
    colaAux:Cola[(int,str,str)]=Cola()
    while not c.empty():
        paciente=c.get()
        colaAux.put(paciente)
        if paciente[0] in [1,2,3]:
            contador+=1
    while not colaAux.empty():
        paciente=colaAux.get()  #los deuvelvo a la cola original
        c.put(paciente)
    return contador     

# cola=Cola()
# cola.put((1,'Jorge','ahi anda'))
# cola.put((1,'Maria','esta jodida'))
# cola.put((7,'Alejandro','blabla'))
# cola.put((4,'Martin','Anda bien dentro de todo'))
# print(n_pacientes_urgentes(cola))

#Ejercicio 18 #nick,dni,pref T/F,prioridad T/F
def atencion_a_clientes(c:Cola[(str,int,bool,bool)])->Cola[(str,int,bool,bool)]:
    cola_prioridades:Cola[(str,int,bool,bool)]=Cola()
    cola_preferencial:Cola[(str,int,bool,bool)]=Cola()
    cola_resto:Cola[(str,int,bool,bool)]=Cola()
    cola_auxiliar:Cola[(str,int,bool,bool)]=Cola()
    cola_ordenada:Cola[(str,int,bool,bool)]=Cola()
    while not c.empty():
        cliente=c.get()                                    #ASI RECORRO LA COLA
        cola_auxiliar.put(cliente)
        if cliente[3]:
            cola_prioridades.put(cliente)
        elif cliente[2]:
            cola_preferencial.put(cliente)
        else:
            cola_resto.put(cliente)
    while not cola_auxiliar.empty():
        cliente=cola_auxiliar.get()
        c.put(cliente)
    while not cola_prioridades.empty():
        cola_ordenada.put(cola_prioridades.get())
    while not cola_preferencial.empty():
        cola_ordenada.put(cola_preferencial.get())
    while not cola_resto.empty():
        cola_ordenada.put(cola_resto.get())
    return cola_ordenada

# cola=Cola()
# cola.put(('Jorge',19391293,False,False))
# cola.put(('Andrea',11523351,True,False))
# cola.put(('Adelina',7976723,False,True))
# cola.put(('Roberto',12452413,True,False))

# cola_ordenada=atencion_a_clientes(cola)
# while not cola_ordenada.empty(): 
#     print(cola_ordenada.get())
