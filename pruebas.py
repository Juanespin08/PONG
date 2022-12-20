"""
from figura_class import Pelota
import pygame as pg
objPelota =  Pelota(300,400)
print(objPelota.pos_x)#300
print( objPelota.derecha )#320
print( objPelota.izquierda )#280
print(objPelota.abajo )#420
print(objPelota.arriba )#380
"""
'''
def funcionespecial(*parametros):
    print( type( parametros) )
    for params in parametros:
        print(params)
funcionespecial("Jose",25,[1,2,3,4])
'''
"""
class Valores:
    def __init__(self):
        self.nombre ="Rolando Lopez"  
    def dameValorAlCuadrado(self,valor):
        return valor*valor
    def dameNombre(self):
        return self.nombre  
class Clase2:
    def __init__(self,valor):
        self.valorRecibido = valor
    def loQueReciba(self,valor):
        self.valorRecibido= valor
obj1 = Valores()
nombre = obj1.dameNombre()
obj2 = Clase2(nombre)
print(obj2.valorRecibido)
"""
'''
def dameValorAlCuadrado(valor):
    return valor*valor
def dameNombre():
    return "Rolando Lopez"
def muestrame(valor):
    for i in range(1,valor):
        print(i)    
    if(True):
        print("Es true y el valor es", valor)
    print("esto es lo que te puedo mostrar")
print("El nombre es: ",dameNombre())
print("El valor al cuadrado de 5 es : ",dameValorAlCuadrado(5) )
muestrame(10)
'''

#operador ternario
edad = 24
estado = "Es mayor de edad" if edad >= 18 else "Eres un chavalin"
print(estado)
#diccionarios
imagenes ={
        'izqda':'electric00_izqda.png',
        'drcha':'electric00_drcha.png'
}
print( imagenes['drcha'] )
print( imagenes['drcha'] )

class Persona:
    def __init__(self):
        self._nombre=''
        self._apellido=''
        self._codigo =''

    #metodo getter, sirver para devolver el valor de un atributo
    @property
    def nombre(self):
        return self.__nombre


    #metodo setter, sirve para cargar valor a un atributo
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre    


objPersona = Persona()
objPersona.nombre="Rolando"
print(objPersona.nombre)


imagenes ={

        'izqda':['electric00_izqda.png','electric01_izqda.png','electric02_izqda.png'],

        'drcha':['electric00_drcha.png','electric01_drcha.png','electric02_drcha.png']

}

imagenprueba={}
for lado in imagenes:
    imagenprueba[lado]=[]
    print(imagenes[lado])
    for nombre_fichero in imagenes[lado]:
        print(nombre_fichero)
        #fotos = pg.image.load( f"images/raquetas/{ nombre_fichero }" )
        imagenprueba[lado].append(fotos)


