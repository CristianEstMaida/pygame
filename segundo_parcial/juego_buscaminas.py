import pygame as pg
from constantes_buscaminas import *

pg.init()
pg.mixer.init()
pantalla = pg.display.set_mode(RESOLUCION_PANTALLA, pg.RESIZABLE)
pg.display.set_caption("Buscaminas")
ruta_imagen_mina = "segundo_parcial/assets/mina.jpg"
imagen_mina = pg.image.load(ruta_imagen_mina)
pg.display.set_icon(imagen_mina)
imagen_buscaminas = pg.image.load("segundo_parcial/assets/buscaminas.png")
posicion_buscaminas = (400, 0)
texto_nivel = pg.font.Font(None, 36).render("Nivel", True, COLOR_NARANJA)
posicion_nivel = (70, 70)
texto_jugar = pg.font.Font(None, 36).render("Jugar", True, COLOR_NARANJA)
posicion_jugar = (70, 170)
texto_puntajes = pg.font.Font(None, 36).render("Ver puntajes", True, COLOR_NARANJA)
posicion_puntajes = (70, 270)
texto_salir = pg.font.Font(None, 36).render("Salir", True, COLOR_NARANJA)
posicion_salir = (70, 370)
ruta_musica_buscaminas = "segundo_parcial/assets/buscaminas.mp3"
pg.mixer.music.load(ruta_musica_buscaminas)
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)
ruta_efecto_explosion = "pygame/explosion.mp3"
explosion = pg.mixer.Sound(ruta_efecto_explosion)        
explosion.set_volume(0.25)
reloj = pg.time.Clock()
corriendo = True

while corriendo == True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
    pantalla.blit(imagen_buscaminas, posicion_buscaminas)
    pantalla.blit(texto_nivel, posicion_nivel)
    pantalla.blit(texto_jugar, posicion_jugar)
    pantalla.blit(texto_puntajes, posicion_puntajes)
    pantalla.blit(texto_salir, posicion_salir)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 50, 200, 75), width=10, border_radius=15)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 150, 200, 75), width=10, border_radius=15)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 250, 200, 75), width=10, border_radius=15)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 350, 200, 75), width=10, border_radius=15)
    reloj.tick(60)
    pg.display.flip()
pg.quit()
