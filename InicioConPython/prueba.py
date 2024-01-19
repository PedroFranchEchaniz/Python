indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]

for indice, numero in enumerate(numeros):
    numeros[indice] *= 10

print(numeros)

cadena = 'Hola cabrones'
cadena2 = ''
indice = -1

for caracter in cadena:
    cadena2 += caracter
    indice -= 1

print(cadena2)