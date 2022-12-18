from pantallas import *


class SceneController:
    def __init__(self):
        self.menu = Menu()
        self.partida = Partida()
        self.resultado =Resultado()
        self.records = Records()
        self.valor_resultado=""

    def start(self):
        self.menu.bucle_pantalla()
        self.valor_resultado = self.partida.bucle_fotograma()
        self.resultado.recibir_resultado(self.valor_resultado)
        self.resultado.bucle_pantalla()