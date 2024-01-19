
import math
def baseCuadrado (b, a):
    return b * a

def areaCircuo(r):
    return (r**2)*math.pi

def numeroIntermedio(a, b):
    return (a+b)/2

def numerosParesImpares(a):
    pares = []
    impares = []

    for numero in a:
        if numero%2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares



while(True):
    print("""
    [1]-Calcular areal del cuacrado
    [2]-Calcular area del circulo
    [3]-Numero intermedio
    [4]-Pares impares
    [0]-Salir""")
    opcion = input()

    if opcion == '1':
        altura = int(input("Indique la altura del cuadrado: "))
        base = int(input("Indique la base del cuacrado: "))
        print(f"El area del cuadrado es: " +str(baseCuadrado(base, altura)))

    elif opcion == '2':
        radio = int(input("Indique el radio de un circulo: "))
        print("El area del circulo es: " +str(areaCircuo(radio)))

    elif opcion == '3':
        numero1=int(input("Indique un numero"))
        numero2=int(input("Indique un numero mayor"))
        print("El numero intermedio es: " +str(numeroIntermedio(numero1, numero2)))

    elif opcion == '0':
        break

    elif opcion == '4':
        numeros = ([1,2,3,4,5,6])
        pares, impares = numerosParesImpares(numeros)
        print(pares)
        print(impares)


    else:
        print("Opción incorrecta")





