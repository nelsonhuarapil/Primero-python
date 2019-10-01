#!/usr/bin/python3

# guardar en la carpeta del proyecto como "usando_persona.py";
# del archivo(modulo) Persona.py impórtamos(la clase) persona
from Persona import Persona

# Ahora en el "main", voy a crear un objeto y voy a llamar al metodo
perrin = Persona("Juan eduardo lopez", "12345678-2")
perrin.imprimir()

# En python los atributos son siempre publicos...
# y por eso los puedo modificar
perrin.rut = "1284734-2"
perrin.imprimir()

# sin embargo hay una convencion -> si un atributo parte con _
# los programadores python lo tratan como si fuera privado.
# perring._nombre = "juan lopez" -> esto no se hace!

# voy a crear una persona leyendo desde a consola:
nombre = input("Ingrese su nombre: ")
rut = input("Ingrese su rut: ")
persona_nueva = Persona(nombre,rut)
persona_nueva.imprimir()