import random

def busqueda_lineal(lista, objetivo):
    match = False
    iteraciones = 0

    for elemento in lista:
        iteraciones += 1
        if elemento == objetivo:
            match = True
            break

    print(f'Iteraciones {iteraciones}')

    return match


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista?'))
    objetivo = int(input('Numero a encontrar'))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El objetivo {objetivo} {"si esta" if encontrado else "no esta"}')

