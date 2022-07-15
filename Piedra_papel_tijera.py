import random
import logging

def jugar():
    print("'Pi' -> Piedra \n'Pa' -> Papel \n'Ti' -> Tijera")
    usuario = input("Ingrese su opcion: ").lower()
    computadora = random.choice(['pi','pa','ti'])
    print(computadora)
    print(usuario)
    if usuario == computadora:
        return("¡Empate!")
    elif gano_usuario(usuario, computadora):
        return("¡Ganaste!")
    else:
        return("¡Perdiste!")
        
def gano_usuario(usuario,computadora):
    if ((usuario == "pi" and computadora == "ti") 
    or (usuario == "pa" and computadora == "pi") 
    or (usuario == "ti" and computadora == "pa")):
        return(True)

def menu():
    print("-"*30)
    print("Opcion 1 -> Reglas")
    print("Opcion 2 -> Jugar")
    print("Opcion 0 -> Salir")
    print("-"*30)

    opcion = int(input("Ingrese la opcion: "))
    print(opcion)
    while 0 <= opcion <= 2:
        if opcion == 1:
            print("Reglas:")
            print("Piedra > Tijera")
            print("Papel > Piedra")
            print("Tijera > Papel\n")
        elif opcion == 2:
            print(jugar())
        elif opcion == 0:
            break
        menu()
    

def calcular_area_cuadrado(lado):
    # Calcular are de un cuadrado
    return lado * lado

def calcular_perimetro(*args):
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro
    
def funcion_kwargs(**kwargs):
    print(kwargs["nombre"], kwargs["apellido"])
    for llave, valor in kwargs.items():
        print(f"Categoria: {llave}-> {valor}")
    
## CORRECTO    
def parametros_ordenados(nombre, apellido, *args, **kwargs):
    pass

## INCORRECTO Esto es un error
## Primero va *args y luego **kwargs
"""
def parametros_desordenados(nombre,apellido,**kwargs,*args):
    pass
"""
#menu()
"""
area_cuadrado = calcular_area_cuadrado(10)
print(area_cuadrado)
perimetro = calcular_perimetro(1,2,3,4,5,6,7,8,8,10)
print(perimetro)

funcion_kwargs(nombre="Franco",apellido="Fernandez",edad=20,universidad="UTN",nota=8)




nombres = ["Franco", "Gabriel", "Nico", "Nacho", "Meli"]
for elem in nombres: # range(inicio, fin, paso)
    print(elem)
"""
logging.debug("Log de debugging")
logging.info("Log informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error crítico")
