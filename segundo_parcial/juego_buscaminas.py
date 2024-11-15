import pygame as pg
from constantes_buscaminas import *
pg.init()
pg.mixer.init()

pantalla = pg.display.set_mode(RESOLUCION_PANTALLA, pg.RESIZABLE)
pg.display.set_caption("Buscaminas")
imagen_mina = pg.image.load("segundo_parcial/assets/mina.jpg")
pg.display.set_icon(imagen_mina)
imagen_buscaminas = pg.image.load("segundo_parcial/assets/buscaminas.png")
posicion_buscaminas = (400, 0)
nivel = pg.font.Font(None, 36).render("Nivel", True, COLOR_NARANJA)
posicion_nivel = (70, 70)
jugar = pg.font.Font(None, 36).render("Jugar", True, COLOR_NARANJA)
posicion_jugar = (70, 170)
puntajes = pg.font.Font(None, 36).render("Ver puntajes", True, COLOR_NARANJA)
posicion_puntajes = (70, 270)
salir = pg.font.Font(None, 36).render("Salir", True, COLOR_NARANJA)
posicion_salir = (70, 370)
pg.mixer.music.load("segundo_parcial/assets/buscaminas.mp3")
pg.mixer.music.set_volume(0.3)
pg.mixer.music.play(-1)

corriendo = True

while corriendo == True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            corriendo = False
    pantalla.blit(imagen_buscaminas, posicion_buscaminas)
    pantalla.blit(nivel, posicion_nivel)
    pantalla.blit(jugar, posicion_jugar)
    pantalla.blit(puntajes, posicion_puntajes)
    pantalla.blit(salir, posicion_salir)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 50, 200, 75), width=10, border_radius=15)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 150, 200, 75), width=10, border_radius=15)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 250, 200, 75), width=10, border_radius=15)
    pg.draw.rect(pantalla, COLOR_NARANJA, (50, 350, 200, 75), width=10, border_radius=15)
    
    pg.display.flip()
pg.quit()