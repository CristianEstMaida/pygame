import time
import pygame as pg
from constantes_buscaminas import *
from biblioteca import *

pg.init()
pg.mixer.init()

pantalla = pg.display.set_mode(RESOLUCION_PANTALLA, pg.RESIZABLE)
pg.display.set_caption("Buscaminas")
color_fondo = COLOR_GRIS_CLARO

cantidad_minas = "10"
tiempo_inicial = 0
tiempo_transcurrido_minutos = 0
tiempo_transcurrido_segundos = "0".zfill(2)
tiempo_fin = 0
contador_puntaje = 0
bandera_boton_buscaminas = False
bandera_tiempo_inicial = False

ruta_imagen_mina = "segundo_parcial/recursos/mina.jpg"
imagen_mina = pg.image.load(ruta_imagen_mina)
pg.display.set_icon(imagen_mina)

imagen_buscaminas = pg.image.load("segundo_parcial/recursos/buscaminas.png")
posicion_buscaminas = (400, 70)

ruta_fuente_pixel = "segundo_parcial/recursos/pixelifysans_variablefont_wght.ttf"
ruta_fuente_jugando = "segundo_parcial/recursos/digital_7.ttf"
fuente_inicio = pg.font.Font(ruta_fuente_pixel, 24)
fuente_jugando = pg.font.Font(ruta_fuente_jugando, 24)
fuente_casilleros = pg.font.Font(ruta_fuente_pixel, 15)
texto_nivel = fuente_inicio.render("Nivel", True, COLOR_NARANJA)
posicion_nivel = (70, 70)
texto_jugar = fuente_inicio.render("Jugar", True, COLOR_NARANJA)
posicion_jugar = (70, 170)
texto_puntajes = fuente_inicio.render("Ver puntajes", True, COLOR_NARANJA)
posicion_puntajes = (70, 270)
texto_salir = fuente_inicio.render("Salir", True, COLOR_NARANJA)
posicion_salir = (70, 370)
nombre_ingresado = ""
fuente_nombre = pg.font.SysFont(ruta_fuente_pixel, 72, bold=True)
nombre_usuario = fuente_nombre.render(nombre_ingresado, True, COLOR_ROJO)

ruta_imagen_blanco = "segundo_parcial/recursos/blanco.gif"
imagen_blanco = pg.image.load(ruta_imagen_blanco)
IMAGEN_BLANCO_ANCHO = imagen_blanco.get_width()
IMAGEN_BLANCO_ALTO = imagen_blanco.get_height()
RESOLUCION_IMAGEN_BLANCO = (IMAGEN_BLANCO_ANCHO, IMAGEN_BLANCO_ALTO)

imagen_reiniciar = pg.image.load("segundo_parcial/recursos/cara_sonriente.gif")
IMAGEN_REINICIAR_ANCHO = imagen_reiniciar.get_width()
IMAGEN_REINICIAR_ALTO = imagen_reiniciar.get_height()
RESOLUCION_IMAGEN_REINICIAR = (IMAGEN_REINICIAR_ANCHO, IMAGEN_REINICIAR_ALTO)
imagen_reiniciar = pg.transform.scale(imagen_reiniciar, RESOLUCION_IMAGEN_REINICIAR)
posicion_imagen_reiniciar = (120, 70)

ruta_imagen_bandera = "segundo_parcial/recursos/bandera.gif"
imagen_bandera = pg.image.load(ruta_imagen_bandera)
IMAGEN_BANDERA_ANCHO = imagen_bandera.get_width()
IMAGEN_BANDERA_ALTO = imagen_bandera.get_height()
RESOLUCION_IMAGEN_BANDERA = (IMAGEN_BANDERA_ANCHO, IMAGEN_BANDERA_ALTO)
ruta_musica_buscaminas = "segundo_parcial/recursos/buscaminas.mp3"
pg.mixer.music.load(ruta_musica_buscaminas)
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)

ruta_efecto_explosion = "segundo_parcial/recursos/explosion.mp3"
explosion = pg.mixer.Sound(ruta_efecto_explosion)        
explosion.set_volume(0.25)
ruta_efecto_descubrimiento = "segundo_parcial/recursos/descubrimiento.mp3"
descubrimiento = pg.mixer.Sound(ruta_efecto_descubrimiento)
descubrimiento.set_volume(0.25)

reloj = pg.time.Clock()
FILAS_FACIL = 8
FILAS_MEDIO = 16
FILAS_DIFICIL = 30
COLUMNAS_FACIL = 8
COLUMNAS_MEDIO = 16
COLUMNAS_DIFICIL = 30
CANTIDAD_MINAS_FACIL = 10
CANTIDAD_MINAS_MEDIO = 40
CANTIDAD_MINAS_DIFICIL = 100

matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
botones_buscaminas = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)

establecer_minas_contiguas(matriz)
mostrar_matriz(matriz)

bandera_identificarse = False
estado_juego = "inicio"
nivel = "dificil"

corriendo = True

while corriendo == True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_jugar.collidepoint(evento.pos) == True:
                    estado_juego = "jugando"
                if bandera_boton_buscaminas == True:
                    if boton_reiniciar.collidepoint(evento.pos) == True:
                        bandera_tiempo_inicial = False
                        bandera_boton_buscaminas = False
                        bandera_identificarse = False
                        nombre_ingresado = ""
                        tiempo_inicial = 0
                        tiempo_transcurrido_minutos = 0
                        tiempo_transcurrido_segundos = "0".zfill(2)
                        contador_puntaje = 0
                        if nivel == "facil":
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                            matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
                        elif nivel == "medio":
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                            matriz = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_MEDIO)
                        elif nivel == "dificil":
                            bandera_matriz_descubierta = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                            bandera_matriz_marcada = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                            matriz = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                            establecer_cantidad_minas(matriz, CANTIDAD_MINAS_DIFICIL)
                        establecer_minas_contiguas(matriz)
                        print("\n")
                        mostrar_matriz(matriz)
                    for i in range(len(matriz)):
                        for j in range(len(matriz[i])):
                            if botones_buscaminas[i][j].collidepoint(evento.pos) == True:
                                if bandera_tiempo_inicial == False:
                                    tiempo_inicial = time.time()
                                    bandera_tiempo_inicial = True
                                match(matriz[j][i]):
                                    case -1:
                                        explosion.play()
                                        estado_juego = "identificarse"
                                        tiempo_fin = time.time()
                                    case _:
                                        if bandera_matriz_descubierta[i][j] == False:
                                            descubrimiento.play()
                                            contador_puntaje += 1
                                            bandera_matriz_descubierta[i][j] = True
                if boton_salir.collidepoint(evento.pos) == True:
                    corriendo = False
            elif evento.button == 3:
                for i in range(len(matriz)):
                        for j in range(len(matriz[i])):
                            if botones_buscaminas[i][j].collidepoint(evento.pos) == True:
                                if bandera_matriz_marcada[i][j] == False:
                                    bandera_matriz_marcada[i][j] = True
                                else:
                                    bandera_matriz_marcada[i][j] = False
        if evento.type == pg.KEYDOWN:
            if estado_juego == "identificarse":
                if evento.key == pg.K_RETURN:
                    if len(nombre_ingresado) >= 3: 
                        bandera_identificarse = True
                elif evento.key == pg.K_BACKSPACE:
                    nombre_ingresado = nombre_ingresado[0:-1]
                else:
                    if len(nombre_ingresado) < 15:
                        nombre_ingresado += evento.unicode
                nombre_usuario = fuente_inicio.render(nombre_ingresado, True, COLOR_ROJO)
    pantalla.fill(color_fondo)
    if estado_juego == "inicio":
        pantalla.blit(imagen_buscaminas, posicion_buscaminas)
        pantalla.blit(texto_nivel, posicion_nivel)
        pantalla.blit(texto_jugar, posicion_jugar)
        pantalla.blit(texto_puntajes, posicion_puntajes)
        pantalla.blit(texto_salir, posicion_salir)
        coordenadas_boton_nivel = (50, 50, 200, 75)
        coordenadas_boton_jugar = (50, 150, 200, 75)
        coordenadas_boton_puntajes = (50, 250, 200, 75)
        coordenadas_boton_salir = (50, 350, 200, 75)
        boton_nivel = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_nivel, width=10, border_radius=15)
        boton_jugar = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_jugar, width=10, border_radius=15)
        boton_puntajes = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_puntajes, width=10, border_radius=15)
        boton_salir = pg.draw.rect(pantalla, COLOR_NARANJA, coordenadas_boton_salir, width=10, border_radius=15)
    elif estado_juego == "jugando":
        pg.mixer.music.set_volume(0.2)
        texto_cantidad_minas = fuente_jugando.render(cantidad_minas, True, COLOR_ROJO)
        posicion_cantidad_minas = (70, 70)
        if bandera_tiempo_inicial == True:
            tiempo_transcurrido_minutos = int(time.time() - tiempo_inicial) // 60
            tiempo_transcurrido_segundos = str(int(time.time() - tiempo_inicial) % 60).zfill(2)
        texto_tiempo = fuente_jugando.render(f"{tiempo_transcurrido_minutos}:{tiempo_transcurrido_segundos}", True, COLOR_ROJO)
        posicion_tiempo = (160, 70)
        puntaje = str(contador_puntaje).zfill(4)
        texto_puntaje = fuente_jugando.render(puntaje, True, COLOR_ROJO)
        posicion_puntaje = (220, 70)
        pantalla.blit(texto_cantidad_minas, posicion_cantidad_minas)
        boton_reiniciar = pantalla.blit(imagen_reiniciar, posicion_imagen_reiniciar)
        pantalla.blit(texto_tiempo, posicion_tiempo)
        pantalla.blit(texto_puntaje, posicion_puntaje)
        posicion_casillero_inicial = (70, 100)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                posicion_casillero = (posicion_casillero_inicial[0] + i * 16, posicion_casillero_inicial[1] + j * 16)
                if bandera_matriz_descubierta[i][j] == False:
                    if bandera_matriz_marcada[i][j] == False:
                        botones_buscaminas[i][j] = pantalla.blit(imagen_blanco, posicion_casillero)
                    else:
                        botones_buscaminas[i][j] = pantalla.blit(imagen_bandera, posicion_casillero)
                elif matriz[j][i] > 0:
                    texto_casillero = fuente_casilleros.render(f"{matriz[j][i]}", True, COLOR_ROJO)
                    pantalla.blit(texto_casillero, posicion_casillero)
                bandera_boton_buscaminas = True
    elif estado_juego == "identificarse":
        texto_nombre_usuario = fuente_inicio.render(f"Ingrese nombre: {nombre_ingresado}", True, COLOR_ROJO)
        posicion_nombre_usuario = (pantalla.get_width() // 2 - nombre_usuario.get_width() // 2, pantalla.get_height() // 2)
        pantalla.blit(texto_nombre_usuario, posicion_nombre_usuario)
        if bandera_identificarse == True:
            estado_juego = "fin"
    elif estado_juego == "fin":
        texto_fin = fuente_inicio.render("PERDISTE", True, COLOR_ROJO)
        posicion_fin = (pantalla.get_width() // 2 - texto_fin.get_width() // 2, pantalla.get_height() // 2)
        pantalla.blit(texto_fin, posicion_fin)
        if int(time.time() - tiempo_fin) >= 5:
            bandera_tiempo_inicial = False
            bandera_boton_buscaminas = False
            bandera_identificarse = False
            nombre_ingresado = ""
            tiempo_inicial = 0
            tiempo_transcurrido_minutos = 0
            tiempo_transcurrido_segundos = "0".zfill(2)
            contador_puntaje = 0
            if nivel == "facil":
                bandera_matriz_descubierta = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                bandera_matriz_marcada = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, False)
                matriz = inicializar_matriz(FILAS_FACIL, COLUMNAS_FACIL, 0)
                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_FACIL)
            elif nivel == "medio":
                bandera_matriz_descubierta = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                bandera_matriz_marcada = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, False)
                matriz = inicializar_matriz(FILAS_MEDIO, COLUMNAS_MEDIO, 0)
                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_MEDIO)
            elif nivel == "dificil":
                bandera_matriz_descubierta = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                bandera_matriz_marcada = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, False)
                matriz = inicializar_matriz(FILAS_DIFICIL, COLUMNAS_DIFICIL, 0)
                establecer_cantidad_minas(matriz, CANTIDAD_MINAS_DIFICIL)
            establecer_minas_contiguas(matriz)
            print("\n")
            mostrar_matriz(matriz)
            estado_juego = "inicio"
    reloj.tick(30)
    pg.display.flip()
pg.quit()
