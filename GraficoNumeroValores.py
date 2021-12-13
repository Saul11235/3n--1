# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from NumerosSerie import NumerosConjetura 

def InputDefecto(texto,valorPorDefecto):
    "solo funciona con valores enteros las respuestas son mayores o menores a 1"
    valor=input(texto)
    try:valor=abs(int(valor))
    except: valor=valorPorDefecto
    if valor==0:valor=1
    return(valor)

print(" Valores máximos en la serie de collatz")
print(" los valores en parantesis son por defecto\n")
minimo=InputDefecto(" Numero mínimo (def 1) : ",1)
maximo=InputDefecto(" Numero máximo (def 1000) :",1000)
intervalo=InputDefecto(" Intervalo (def 1) : ",1)
print("\nCalculando los valores, espere....")

#analizandp variables maximas y minimas
if maximo<minimo:
    variableayuda=minimo
    minimo=maximo
    maximo=variableayuda

MaximoNumerosAnalizados=5000 #<-- Mandar anuncios cada x nros
contadorNumeros=0

#generando lista de numeros analizados
listaDeValoresX=[] #numeros
listaDeValoresY=[] #valor max serie collatz
cicloValoresDeEntrada=True
numeroCiclo=minimo
while cicloValoresDeEntrada:
    valorY=NumerosConjetura(numeroCiclo)[1]
    valorX=numeroCiclo
    listaDeValoresX.append(valorX)
    listaDeValoresY.append(valorY)
    numeroCiclo+=intervalo
    if numeroCiclo>maximo:
        cicloValoresDeEntrada=False
    contadorNumeros=contadorNumeros+1    
    if contadorNumeros>MaximoNumerosAnalizados:
        contadorNumeros=0
        print(" al "+str(round(100-(maximo-numeroCiclo)/(maximo-minimo)*100,3))+"%")


#--- GRAFICANDO-----------------------------------
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(listaDeValoresX,listaDeValoresY)
plt.title("Número de valores de la Serie collatz, desde "+str(minimo)+" hasta "+str(maximo))
plt.xlabel("Números analizados")
plt.ylabel("Número total de valores de la serie")
plt.show()


