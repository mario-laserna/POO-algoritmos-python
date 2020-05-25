import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == '__main__':
    tamano_lista = int(input('Tamaño de la lista?'))
    objetivo = int(input('Numero a encontrar'))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])
    print(lista)

    encontrado = busqueda_lineal(lista, objetivo)
    print(f'El objetivo {objetivo} {"si esta" if encontrado else "no esta"}')

