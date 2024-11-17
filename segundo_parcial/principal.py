import pygame as pg
from constantes_buscaminas import *
from biblioteca import *

pg.init()
pg.mixer.init()
pantalla = pg.display.set_mode(RESOLUCION_PANTALLA, pg.RESIZABLE)
pg.display.set_caption("Buscaminas")
color_fondo = [0, 0, 0]
ruta_imagen_mina = "segundo_parcial/recursos/mina.jpg"
imagen_mina = pg.image.load(ruta_imagen_mina)
pg.display.set_icon(imagen_mina)
imagen_buscaminas = pg.image.load("segundo_parcial/recursos/buscaminas.png")
posicion_buscaminas = (400, 0)
texto_nivel = pg.font.Font(None, 36).render("Nivel", True, COLOR_NARANJA)
posicion_nivel = (70, 70)
texto_jugar = pg.font.Font(None, 36).render("Jugar", True, COLOR_NARANJA)
posicion_jugar = (70, 170)
texto_puntajes = pg.font.Font(None, 36).render("Ver puntajes", True, COLOR_NARANJA)
posicion_puntajes = (70, 270)
texto_salir = pg.font.Font(None, 36).render("Salir", True, COLOR_NARANJA)
posicion_salir = (70, 370)
ruta_imagen_blanco = "segundo_parcial/recursos/blanco.gif"
imagen_blanco = pg.image.load(ruta_imagen_blanco)
posicion_imagen_blanco = (70, 70)
ruta_musica_buscaminas = "segundo_parcial/recursos/buscaminas.mp3"
pg.mixer.music.load(ruta_musica_buscaminas)
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)
ruta_efecto_explosion = "segundo_parcial/recursos/explosion.mp3"
explosion = pg.mixer.Sound(ruta_efecto_explosion)        
explosion.set_volume(0.25)
reloj = pg.time.Clock()
matriz = crear_matriz_aleatoria(8, 8, -1, 0)
matriz_minas_contiguas = establecer_minas_contiguas(matriz)
mostrar_matriz(matriz_minas_contiguas)
botones_buscaminas = inicializar_matriz(8, 8, 0)
estado_juego = "inicio"
bandera_boton_buscaminas = False
corriendo = True

while corriendo == True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if boton_jugar.collidepoint(evento.pos):
                estado_juego = "jugando"
                if bandera_boton_buscaminas == True:
                    print("")
                    mostrar_matriz(matriz_minas_contiguas)
                    for i in range(len(matriz)):
                        for j in range(len(matriz[i])):
                            if botones_buscaminas[i][j].collidepoint(evento.pos):
                                print("\n", matriz_minas_contiguas[i][j])
                                match(matriz_minas_contiguas[i][j]):
                                    case -1:
                                        explosion.play()
    pantalla.fill(color_fondo)
    if estado_juego == "inicio":
        pantalla.blit(imagen_buscaminas, posicion_buscaminas)
        pantalla.blit(texto_nivel, posicion_nivel)
        pantalla.blit(texto_jugar, posicion_jugar)
        pantalla.blit(texto_puntajes, posicion_puntajes)
        pantalla.blit(texto_salir, posicion_salir)
        boton_nivel = pg.draw.rect(pantalla, COLOR_NARANJA, (50, 50, 200, 75), width=10, border_radius=15)
        boton_jugar = pg.draw.rect(pantalla, COLOR_NARANJA, (50, 150, 200, 75), width=10, border_radius=15)
        boton_puntajes = pg.draw.rect(pantalla, COLOR_NARANJA, (50, 250, 200, 75), width=10, border_radius=15)
        boton_salir = pg.draw.rect(pantalla, COLOR_NARANJA, (50, 350, 200, 75), width=10, border_radius=15)
    elif estado_juego == "jugando":
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                botones_buscaminas[i][j] = pantalla.blit(imagen_blanco, (posicion_imagen_blanco[0] + i * 16, posicion_imagen_blanco[1] + j * 16))
                bandera_boton_buscaminas = True
    reloj.tick(60)
    pg.display.flip()
pg.quit()
