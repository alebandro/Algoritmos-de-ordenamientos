def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor = lista[i]
        j = i - 1
        # Desplazar elementos mayores hacia la derecha
        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1
        # Insertar el valor en la posición correcta
        lista[j + 1] = valor
    return lista

# Ejemplo de uso:
#lista2 = [29, 10, 14, 37, 13]
#print("Insertion Sort:", insertion_sort(lista2))

