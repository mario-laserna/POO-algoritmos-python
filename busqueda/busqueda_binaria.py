import random


def busqueda_binaria(lista, comienzo, final, objetivo, iteraciones):
    print(f'Iteración {iteraciones} -- Buscando entre {comienzo} y {final - 1}')

    if comienzo > final:
        return False

    medio = (comienzo+final) // 2  # division de enteros

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, len(lista), objetivo, iteraciones + 1)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iteraciones + 1)


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista?'))
    objetivo = int(input('Numero a encontrar'))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, 0)

    print(lista)
    print(f'El objetivo {objetivo} {"si esta" if encontrado else "no esta"}')

