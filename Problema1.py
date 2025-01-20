Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def separar_y_ordenar(lista):
...     # Filtrar los valores negativos y positivos
...     negativos = [x for x in lista if x < 0]
...     positivos = [x for x in lista if x >= 0]
... 
...     # Ordenar ambas listas
...     negativos.sort()
...     positivos.sort()
... 
...     # Devolver las dos listas ordenadas
...     return negativos, positivos
... lista = [3, -2, 5, -1, 0, -7, 4]
... 
... # Llamar a la función
... negativos, positivos = separar_y_ordenar(lista)
... 
... # Imprimir los resultados
... print("Negativos:", negativos)
... print("Positivos:", positivos)
SyntaxError: invalid syntax
>>> 
============== RESTART: /Users/anaenriquesuarez/Documents/lista.py =============
Negativos: [-7, -2, -1]
Positivos: [0, 3, 4, 5]
