import random

def crearBaraja(palos, numeros):
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero + palo)
    return baraja

def intercambio (a,b):
    aux = a
    a = b
    b = aux
    return a, b
    
def barajar(lista_de_naipes):
    for i in range (len(lista_de_naipes)):
        nueva_pos = random.randrange(len(lista_de_naipes))
        #Intercambio de cartas, técnica del vaso vacio
        aux = lista_de_naipes[nueva_pos]
        lista_de_naipes [nueva_pos] = lista_de_naipes [i]
        lista_de_naipes [i] = aux
    return lista_de_naipes
    



        
    