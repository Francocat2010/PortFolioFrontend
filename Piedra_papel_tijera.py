import random
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
    

menu()