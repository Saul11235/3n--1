# ¿Qué es la conjetura de Collatz?

También conocido cómo conjetura de Ulam, problema de Kakutani, conjetura de Thwaites, algoritmo de Hasse ó problema de Siracusa 
Es una curiosidad matemática que se opera entre los enteros posistivos, dice resumidamente así:

> *Sea para un número entero posivo la función $F(n)/ n\in \mathbb Z^+$*
> 
>     *$F(n)=n/2 \longleftrightarrow x $ es par*
> 
>     *$F(n)=3n+1 \longleftrightarrow x$ es impar*
> 
> *La conjetura implica que para todo número $n$ tal que $n\in \mathbb Z^+$ al repetirse $F(n)$ sucesivamente, siempre acabará en el ciclo $4,2,1,4,2,1....$*

Este problema por trivial que pueda parecer aún no es resuelto y todavía no se puede refutar o afirmar esta cojetura, en este repositorio hay 3 scripts que permiten graficar y obtener valores respecto a esta conjetura.

_____

# NumerosSerie.py

Este script al ser ejecutado ejecuta un programa sencillo que halla los elementos de una serie según la conjetura de Collatz, si se importa en un programa python tiene una función que recibe un número y devuelve una lista con valores calulados.

<p align="center">
  <img src="https://media.giphy.com/media/MrrRm1wC0TntD8Ect5/giphy.gif" alt="animated" />
</p>

para poder utilizar esta función en sus propios programas se puede importar la función de la siguiente manera:

<code>from NumerosSerie import NumerosConjetura</code>

la función NumerosConjetura, tiene sólo un parámetro de entrada, que es el número a analizar, y devuelve una lista con los siguientes valores

`return [ListaNumerosSerie,NumeroElementos,ValorMaximo,PosicionValorMaximo]`

Los siguientes scripts son aplicaciones de esta función y se dedican a hacer gráficos de ciertos valores analizados, solicitan de entrada valores iniciales, finales e intérvalos entre estos para obtener info, todos estos datos deberán ser números enteros.

# GraficoNumeroValores.py

Analiza el parámetro <code>NumeroElementos</code> es decir el número de los elemtentos iterados hasta llegar a 1.

<img src="https://i.ibb.co/3hGGKLM/F1.png" alt="F1" border="0">

# GraficoPorcentajePosicionMaximo.py

Analiza en términos de porcentaje la posición de un número respecto a su posisción máxima, mediante la expresión: $\%posición=100\%-PosicionValorMaximo/NumeroElementos*100\%$

<img src="https://i.ibb.co/yNDMrr5/F2.png" alt="F2" border="0">

# GraficoPosicionMaximo.py

Analiza el parámetro <code>PosicionValorMaximo</code> es decir la posición del valor mayor en la <code>ListaNumerosSerie</code>.

<img src="https://i.ibb.co/W6RDCfk/F3.png" alt="F3" border="0">

# GraficoValorMaximo.py

Analiza el valor numérico máximo obtenido de la conjetura, vale decir <code>ValorMaximo</code>.

<img src="https://i.ibb.co/RTWFjvJ/F4.png" alt="F4" border="0">

Si bien esta gráfica fue hecha con los valores por defecto, se pueden apreciar los patrones de modo más claro al incrementar el umbral de valores calculados hasta 1000000, esto se puede indicar al momento de ejecutar el script.

<img src="https://i.ibb.co/PNfdgHK/Max-Millon.png" alt="Max-Millon" border="0">

recuerde que los valores por defecto se ingresarán en caso de que no se ingrese ningún valor numérico que sea un entero positivo.

-----



# Algunos links de interés

algunos links que te pueden servir si tienes algún interés en esto, (dicen que las matemáticas aun no están lo suficientemente maduras para tener respuestas concretas sobre esto).

- Veritasium (Muy entretenido) [The Simplest Math Problem No One Can Solve - Collatz Conjecture - YouTube](https://www.youtube.com/watch?v=094y1Z2wpJg) 

- Conjetura de Collatz wikipedia [Conjetura de Collatz - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Conjetura_de_Collatz) 
