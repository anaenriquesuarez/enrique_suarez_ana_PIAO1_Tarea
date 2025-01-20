def obtener_conjunto():
    # Pedir al usuario que ingrese los elementos del conjunto
    conjunto_str = input("Ingresa los elementos del conjunto separados por espacios: ")
    # Convertir la entrada en una lista de números enteros
    conjunto = set(map(int, conjunto_str.split()))
    return conjunto

def main():
    print("Crea el primer conjunto de números:")
    conjunto1 = obtener_conjunto()

    print("Crea el segundo conjunto de números:")
    conjunto2 = obtener_conjunto()

    # Calcular la intersección, unión y diferencia simétrica
    interseccion = conjunto1 & conjunto2
    union = conjunto1 | conjunto2
    diferencia_simetrica = conjunto1 ^ conjunto2

    # Mostrar los resultados
    print("\nResultados:")
    print(f"Intersección (elementos comunes): {interseccion}")
    print(f"Unión (todos los elementos sin duplicados): {union}")
    print(f"Diferencia simétrica (elementos que están en uno u otro conjunto, pero no en ambos): {diferencia_simetrica}")

# Llamar a la función principal
main()

