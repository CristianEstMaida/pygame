import random

def crear_matriz_aleatoria(cantidad_filas:int, cantidad_columnas:int, desde:int, hasta:int)->list:
    '''
    Carga en un matriz números aleatorios.
    Recibe cantidad de filas, columnas, desde y hasta (int).
    Retorna None
    '''
    matriz = inicializar_matriz(cantidad_filas, cantidad_columnas, 0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(desde, hasta)
    return matriz

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)->list:
    '''
    Carga una matriz con valores iniciales.
    Recibe una cantidad de filas, columnas y una valor inicial.
    Retorna la matriz cargada.
    '''
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list)->None:
    '''
    Imprime en la pantalla la matriz.
    Recibe la matriz (list).
    Retorna None.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")

def establecer_minas_contiguas(matriz:list)->None:
    '''
    Modifica de una matriz los elementos que no tienen minas con la cantidad de minas contiguas.
    Recibe la matriz (list).
    Retorna None.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == -1:
                continue
            contador = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x and x < len(matriz) and 0 <= y and y < len(matriz[x]):
                        if matriz[x][y] == -1:
                            contador += 1
            matriz[i][j] = contador
