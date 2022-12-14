from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

#definir la tasa de refresco de nuestro bucle de fotogramas fps= fotograma por segundo
cronometro = pg.time.Clock()

#defino objetos pelota y raqueta
pelota = Pelota(400,300)
raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(790,300)

# asignar velocidad
raqueta1.vy=80
raqueta2.vy=80
pelota.vx=4

game_over = False


while not game_over:

    vt = cronometro.tick(200)#variable para comtrolar la velocidad entre fotogramas
   #print(vt)


    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True


    raqueta1.mover(pg.K_w,pg.K_s)        
    raqueta2.mover(pg.K_UP,pg.K_DOWN)
    
    pelota.mover()

    pantalla_principal.fill((0,128,94)) #pintando pantalla

    #logica de choque
    """
    if pelota.derecha >= raqueta2.izquierda and \
       pelota.izquierda <= raqueta2.derecha and \
       pelota.abajo >= raqueta2.arriba and\
       pelota.arriba <= raqueta2.abajo :
       pelota.vx *= -1  


    if pelota.derecha >= raqueta1.izquierda and \
       pelota.izquierda <= raqueta1.derecha and \
       pelota.abajo >= raqueta1.arriba and\
       pelota.arriba <= raqueta1.abajo :
       pelota.vx *= -1    
   """
   # pelota.comprobar_choque(raqueta1,raqueta2)

    pelota.comprobar_choquev2(raqueta1,raqueta2)

    pelota.marcador(pantalla_principal) #pintado marcador
    pg.draw.line(pantalla_principal, (255,255,255),(400,0),(400,600), width=10) #pintando line blanca del centro del campo
    pelota.dibujar(pantalla_principal)#pintado pelota
    raqueta1.dibujar(pantalla_principal)#pintado raqueta1
    raqueta2.dibujar(pantalla_principal)#pintado raqueta2

   
    pg.display.flip()      