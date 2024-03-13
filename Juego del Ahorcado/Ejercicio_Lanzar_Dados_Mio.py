from random import *

def lanzar_dados():
    op1 = randint(1,6)
    op2 = randint(1,6)
    return op1,op2

def evaluar_jugada(op1,op2):
    suma_dados = op1 + op2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable.")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances.")
    elif suma_dados >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora.")

dado1,dado2 = lanzar_dados()
print(dado1,dado2)
evaluar_jugada(dado1,dado2)
