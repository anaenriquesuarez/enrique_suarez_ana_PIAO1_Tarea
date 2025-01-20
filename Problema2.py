import string

def contar_palabras():
    # Solicitar al usuario ingresar una frase o párrafo
    texto = input("Ingresa una frase o párrafo: ")
    
    # Eliminar signos de puntuación y convertir a minúsculas
    texto_limpio = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    
    # Dividir el texto en palabras
    palabras = texto_limpio.split()
    
    # Crear un diccionario para contar la frecuencia de las palabras
    frecuencia = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    # Ordenar el diccionario por la palabra
    for palabra, count in sorted(frecuencia.items()):
        print(f"{palabra}: {count}")

# Llamar a la función
contar_palabras()

