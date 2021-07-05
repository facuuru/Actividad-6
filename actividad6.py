import numpy as np

def random_square_matrix(n):
    A = np.random.randint(low=0, high= 100, size=(n,n))
    return A

def define_square_matrix(n):
    A = np.zeros((n,n), dtype=int)

    for x in range(n):
        for y in range(n):
            A[x][y] = int(input(f'Inserte el valor de la fila {x+1} columna {y+1}: '))
    return A

def random_matrix(m,n):
    A = np.random.randint(low=0, high= 100, size=(m,n))
    return A

def parte_1():
    n = int(input('Inserte un numero entre 2 y 7: '))
    if n % 2 == 0:
        A = random_square_matrix(n)
    else:
        A = define_square_matrix(n)
    print(f'Matriz A: \n{A}')
    print(f'Promedio de la matriz A: { A.mean()}')

    product = 1
    for x in range(n):
        for y in range(n):
            if x is not y:
                product *= A[x][y]
    print(f'El producto de las posiciones donde i no es igual a j es: {product}')

def parte_2():
    n = int(input('Introduzca el numero del orden de las dos matrices cuadradas: '))
    A = random_square_matrix(n)
    B = random_square_matrix(n)


    print(f'Matriz A: \n{A}')
    print(f'Matriz B: \n{B}')

    summ = np.add(A,B)

    exit = False
    while not exit:
        option = input('[1]Producto de elementos de filas y columnas iguales\n[2]Producto de elementos de filas y columnas impares\n[3]Producto de elementos de filas y columnas pares\n[4]Elemento dentro de la matriz\n[5]Salir\nOpcion:')
        product = 1
        if option == '1':
            for x in range(n):
                for y in range(n):
                    if x == y:
                        product *= summ[x][y]
            print(f'Resultado del producto: {product}\n')
        elif option == '2':
            for x in range(n):
                for y in range(n):
                    if (x+1) % 2 != 0 and (y+1) % 2 != 0 and x != y:
                        product *= summ[x][y]
            print(f'Resultado del producto: {product}\n')
        elif option == '3':
            for x in range(n):
                for y in range(n):
                    if (x+1) % 2 == 0 and (y+1) % 2 == 0 and x != y:
                        product *= summ[x][y]
            print(f'Resultado del producto: {product}\n')
        elif option == '4':
            value = int(input('Inserte el valor del elemento que desea buscar dentro de la matriz: '))
            for x in range(n):
                for y in range(n):
                    if summ[x][y] == value:
                        print(f'El valor de la fila {x+1} columna {y+1} es: {summ[x][y]}')
        elif option == '5':
            exit = True

def parte_3():
    m = int(input('Inserte el numero de filas de la matriz: '))
    n = int(input('Inserte el numero de columnas de la matriz: '))

    A = random_matrix(m, n)

    value = int(input('Inserte el valor del elemento que desea buscar en la matriz: '))
    found = False
    #F
    for x in range(m):
        for y in range(n):
            if A[x][y] == value:
                print(f'El valor de la fila {x+1} columna {y+1} es: {A[x][y]}')
                found = True

    if not found:
        print('No existe este elemento dentro de la matriz\n')
    # H
    for x in range(m):
        for y in range(n):
            if x != y and A[x][y] == value:
                print(f'El valor de la fila {x+1} columna {y+1} es: {A[x][y]}')

    # I and J
    m = int(input('Inserte el numero de filas de la segunda matriz: '))
    n = int(input('Inserte el numero de columnas de la segunda matriz: '))

    B = random_matrix(m,n)

    try:
        product_matrix = np.dot(A,B)
        print('\nLas matrices son conformables para la multiplicacion\n')
        sum_of_product = np.sum(product_matrix)
        cubic_root = np.cbrt(sum_of_product)
        print(f'Raiz cubica de la suma de los elementos del producto de las dos matrices: {cubic_root}\n')
    except ValueError:
        print('\nNo se puede realizar multiplicacion de las matrices\n')

exit = False

while not exit:
    part = input('Inserte la parte de la actividad que desea correr:\n[1]Parte 1\n[2]Parte 2\n[3]Parte 3\nOpcion: ')
    if part == '1':
        parte_1()
    elif part == '2':
        parte_2()
    elif part == '3':
        parte_3()

    option = input('Desea reiniciar el programa?\n[1]Si\n[2]No\nOpcion: ')
    if option == '1':
        exit = False
    else:
        exit = True