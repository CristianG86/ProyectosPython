def devolver_distintos(num1,num2,num3):
    suma = num1 + num2 + num3
    print(f"la suma es {suma}")
    if suma > 15:
        if num1 > num2 and num1 > num3:
            print(f"El mayor número es {num1}")
        elif num2 > num1 and num2 > num3:
            print(f"El mayor número es {num2}")
        elif num3 > num1 and num3 > num2:
            print(f"El mayor número es {num3}")
    elif suma < 10:
        if num1 < num2 and num1 < num3:
            print(f"El menor número es {num1}")
        elif num2 < num1 and num2 < num3:
            print(f"El menor número es {num2}")
        elif num3 < num1 and num3 < num2:
            print(f"El menor número es {num3}")
    elif suma >= 10 and suma <= 15:
        if num1 > num2 and num1 < num3:
            print(f"El número de valor intermedio es {num1}")
        elif num2 > num1 and num2 < num3:
            print(f"El número de valor intermedio es {num2}")
        elif num3 > num1 and num3 < num2:
            print(f"El número de valor intermedio es {num3}")


devolver_distintos(5,2,7)