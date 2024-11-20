import random
from json import *

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

def establecer_cantidad_minas(matriz:list, cantidad:int)->None:
    '''
    Modifica una matriz para que tenga una cantidad de minas determinada.
    Recibe la matriz (list) y la cantidad de minas (int). 
    Retorna None.
    '''
    contador = 0
    while contador < cantidad:
        x = random.randint(0, len(matriz) - 1)
        y = random.randint(0, len(matriz[0]) - 1)
        matriz[x][y] = -1
        contador = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == -1:
                    contador += 1

def establecer_minas_contiguas(matriz:list)->None:
    '''
    Modifica de una matriz los elementos que no tienen minas con la cantidad de minas contiguas.
    Recibe la matriz (list).
    Retorna la matriz modificada.
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

def guardar_archivo_json(ruta:str, dato:any)->None:
    '''
    La funcion guarda el dato en un archivo en formato json.
    Recibe una ruta (str) y un dato (any).
    Retorna None.
    '''
    with open(ruta, "w") as archivo:
        dump(dato, archivo, indent=4)

def cargar_jugador(lista: list, nombre:str, puntaje:str, estado:str) -> dict:
    '''
    Carga un diccionario con valores.
    Recibe una lista de claves (list), un nombre, un puntaje y un estado (str).
    Retorna el diccionario cargado.
    '''
    diccionario = {}

    for clave in lista:
        if clave == estado:
            diccionario.update({clave: True})
        elif clave == lista[0]:
            diccionario.update({clave: nombre})
        else:
            diccionario.update({clave: puntaje})
    return diccionario

def cargar_archivo_json(ruta:str)->any:
    '''
    La funcion carga datos de un archivo en formato json.
    Recibe una ruta (str).
    Retorna los datos cargados.
    '''
    with open(ruta, "r") as archivo:
        datos = load(archivo)
    return datos

def definir_orden(diccionario:dict) -> str:
    '''
    La funcion establece el orden por puntaje.
    Recibe un diccionario (dict).
    Retorna el valor de diccionario en la clave puntaje
    '''
    return diccionario["puntaje"]

def ordenar_jugadores(lista_alumnos:list[dict], orden:str) -> None:
    '''
    La funcion ordena una lista de jugadores segun un orden.
    Recibe la lista (list[dict]) y el orden (str).
    Retorna None.
    '''
    if orden == "asc":
        lista_alumnos.sort(key=definir_orden)
    elif orden == "desc":
        lista_alumnos.sort(key=definir_orden, reverse=True)
