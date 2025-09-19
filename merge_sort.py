def merge_sort_iterativo(lista):
    n = len(lista)
    tamaño_sublista = 1

    # Ir duplicando el tamaño de las sublistas a combinar: 1, 2, 4, 8...
    while tamaño_sublista < n:
        for inicio in range(0, n, 2 * tamaño_sublista):
            mitad = inicio + tamaño_sublista
            fin = min(inicio + 2 * tamaño_sublista, n)

            izquierda = lista[inicio:mitad]
            derecha = lista[mitad:fin]

            i = j = 0
            k = inicio

            # Mezclar izquierda y derecha
            while i < len(izquierda) and j < len(derecha):
                if izquierda[i] < derecha[j]:
                    lista[k] = izquierda[i]
                    i += 1
                else:
                    lista[k] = derecha[j]
                    j += 1
                k += 1

            # Copiar lo que quede
            while i < len(izquierda):
                lista[k] = izquierda[i]
                i += 1
                k += 1
            while j < len(derecha):
                lista[k] = derecha[j]
                j += 1
                k += 1

        tamaño_sublista *= 2

    return lista

# Ejemplo de uso:
lista = [38, 27, 43, 3, 9, 82, 10]
ordenada = merge_sort_iterativo(lista[:])  # lista[:] para no modificar la original
print("Lista ordenada:", ordenada)
