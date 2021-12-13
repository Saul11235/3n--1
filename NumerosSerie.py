# -*- coding: utf-8 -*-
#script que calcula todos los numero de la conjetura de collatz
#No pierdas tiempo con esto anda a hacer otras cosas  :(

def NumerosConjetura(numeroEntrada):
    """Devuelve una lista con 3 elementos.\n0- una lista con todos los números\n1- número de elementos\n2- número máximo de la lista\n3- posición del número máximo"""
    numeroEntrada=int(abs(numeroEntrada))
    if not(numeroEntrada): numeroEntrada=1 #eliminando valores no fraccion ni negativos 
    numeros=[] #lista de nros
    numerodeElementos=0
    numeroMaximo=numeroEntrada
    posicionNumeroMaximo=0
    numeroDePrueba=numeroEntrada #numero que se calculara
    calcularvalores=True 
    UltimoCiclo=False
    while calcularvalores:
        #analizando si el numeroDePrueba es par
        espar=not(bool(numeroDePrueba/2-int(numeroDePrueba/2)))
        numerodeElementos=numerodeElementos+1
        if espar:
            numeroDePrueba=int(numeroDePrueba/2)
        else:
            numeroDePrueba=int(numeroDePrueba*3+1)
            if numeroMaximo<numeroDePrueba:
                numeroMaximo=numeroDePrueba
                posicionNumeroMaximo=numerodeElementos
        numeros.append(numeroDePrueba)    
        if numeroDePrueba==1:
            calcularvalores=False #fin del calculo
    return([numeros,numerodeElementos,numeroMaximo,posicionNumeroMaximo])
    

if __name__=="__main__":
    print("Conjetura de collatz")
    numero=abs(int(input(" >>> ")))
    lista=NumerosConjetura(numero)
    print(" Número de variables ciclo : "+str(lista[1]))
    print(" Número Máximo : "+str(lista[2]))
    print(" Posicion Número Máximo : "+str(lista[3]))
    input("> presione enter para continuar ")
    contador=0
    for x in lista[0]:
        contador=contador+1
        print(str(contador)+"\t"+str(x))
 
 
