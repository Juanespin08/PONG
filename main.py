from pantallas import Partida,Menu #IMPORTAR LA CLASE PARTIDA

juego = Partida() #CREAMOS UN OBJETO DE LA CLASE PARTIDA

juego.bucle_fotograma() # LLAMAMOS AL BUCLE FOTOGRAMA


menu = Menu()
mensaje = menu.bucle_pantalla()

if mensaje == 'jugar':
    juego = Partida() #creamos objeto de la clase Partida
    juego.bucle_fotograma() #llamamos al bucle de fotograma

print(mensaje)