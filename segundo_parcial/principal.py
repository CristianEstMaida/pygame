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
contador_puntaje = 0
bandera_boton_buscaminas = False
bandera_tiempo_inicial = False
ruta_imagen_mina = "segundo_parcial/recursos/mina.jpg"
imagen_mina = pg.image.load(ruta_imagen_mina)
pg.display.set_icon(imagen_mina)
imagen_buscaminas = pg.image.load("segundo_parcial/recursos/buscaminas.png")
posicion_buscaminas = (400, 0)
fuente_inicio = pg.font.Font(None, 36)
fuente_jugando = pg.font.Font(None, 36)
texto_nivel = fuente_inicio.render("Nivel", True, COLOR_NARANJA)
posicion_nivel = (70, 70)
texto_jugar = fuente_inicio.render("Jugar", True, COLOR_NARANJA)
posicion_jugar = (70, 170)
texto_puntajes = fuente_inicio.render("Ver puntajes", True, COLOR_NARANJA)
posicion_puntajes = (70, 270)
texto_salir = fuente_inicio.render("Salir", True, COLOR_NARANJA)
posicion_salir = (70, 370)
ruta_imagen_blanco = "segundo_parcial/recursos/blanco.gif"
imagen_blanco = pg.image.load(ruta_imagen_blanco)
posicion_imagen_blanco = (70, 100)
imagen_reiniciar = pg.image.load("segundo_parcial/recursos/cara_sonriente.gif")
posicion_imagen_reiniciar = (120, 70)
ruta_musica_buscaminas = "segundo_parcial/recursos/buscaminas.mp3"
pg.mixer.music.load(ruta_musica_buscaminas)
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)
ruta_efecto_explosion = "segundo_parcial/recursos/explosion.mp3"
explosion = pg.mixer.Sound(ruta_efecto_explosion)        
explosion.set_volume(0.25)
reloj = pg.time.Clock()
matriz = crear_matriz_aleatoria(8, 8, -1, 0)
establecer_cantidad_minas(matriz, 10, -1, 0)
establecer_minas_contiguas(matriz)
mostrar_matriz(matriz)
botones_buscaminas = inicializar_matriz(8, 8, 0)
bandera_matriz_descubierta = inicializar_matriz(8, 8, False)
estado_juego = "inicio"
corriendo = True

while corriendo == True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if boton_jugar.collidepoint(evento.pos):
                estado_juego = "jugando"
            if bandera_boton_buscaminas == True:
                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        if botones_buscaminas[i][j].collidepoint(evento.pos):
                            if bandera_tiempo_inicial == False:
                                tiempo_inicial = time.time()
                                bandera_tiempo_inicial = True
                            match(matriz[j][i]):
                                case -1:
                                    explosion.play()
                                    estado_juego = "fin"
                                case _:
                                    if bandera_matriz_descubierta[i][j] == False:
                                        contador_puntaje += 1
                                    bandera_matriz_descubierta[i][j] = True
                if evento.button == 3:
                    print("Derecho")
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
        pantalla.blit(imagen_reiniciar, posicion_imagen_reiniciar)
        pantalla.blit(texto_tiempo, posicion_tiempo)
        pantalla.blit(texto_puntaje, posicion_puntaje)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                botones_buscaminas[i][j] = pantalla.blit(imagen_blanco, (posicion_imagen_blanco[0] + i * 16, posicion_imagen_blanco[1] + j * 16))
                bandera_boton_buscaminas = True
    elif estado_juego == "fin":
        bandera_tiempo_inicial = False
        bandera_boton_buscaminas = False
        bandera_matriz_descubierta = inicializar_matriz(8, 8, False)
        tiempo_inicial = 0
        tiempo_transcurrido_minutos = 0
        tiempo_transcurrido_segundos = "0".zfill(2)
        contador_puntaje = 0
        matriz = crear_matriz_aleatoria(8, 8, -1, 0)
        establecer_cantidad_minas(matriz, 10, -1, 0)
        establecer_minas_contiguas(matriz)
        print("\n")
        mostrar_matriz(matriz)
        estado_juego = "inicio"
    reloj.tick(30)
    pg.display.flip()
pg.quit()
pg.quit()
