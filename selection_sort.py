def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Suponemos que el mínimo está en la posición i
        min_idx = i
        # Buscamos el mínimo en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiamos el elemento actual con el mínimo encontrado
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Ejemplo de uso:
#lista1 = [29, 10, 14, 37, 13]
#print("Selection Sort:", selection_sort(lista1))

