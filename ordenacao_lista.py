lista = [64, 34, 25, 12, 22, 11, 90]

def ordenar_lista(lista: list) -> list:
    lista_ordenada = lista.copy()

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista_ordenada[i] > lista_ordenada[j]:
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]

    return lista_ordenada

print(ordenar_lista(lista))