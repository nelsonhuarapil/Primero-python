#!/usr/bin/python3

# guardar en la carpeta del proyecto como ;
#'Persona.py'

class Persona:
    """ que representa a una Persona
        En chile
        self -> rol similar al this de java
        El constructor se llama siempre
        (doble underscore)init(doble underscore)
        Todas las operaciones de la clase reciben
        al self como primer parametro!!!
    """
    def __init__(self,nombre, rut):
        self._nombre = nombre
        self.rut = rut

    #ojo todos los metodos reciben el self como parametro!
    def imprimir(self):
        texto = " ".join(["Soy", self._nombre, ", Mi rut es",self.rut ])
        print(texto)

