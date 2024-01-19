numeros = (1,2,3,4)

for indice,numero in enumerate(numeros):
    print((numeros[indice])*10)

alumnos = {"Hecor":20, "Luis":20}
alumnos["Juan"] = 30

for alumno in alumnos:
    print(alumno)

for caca in alumnos:
    print(alumnos[caca])

lista = ("Hoo", "aa")

def palabraLarga(a):
    masLarta = ""
    for palabra in a:
        if len(palabra)>len(masLarta):
            masLarta = palabra
    return masLarta


def letrasMayusculas(palabra):
    contador = 0
    for letra in palabra:
        if letra != letra.lower():
            contador += 1
    print(contador)

palabra = input("Escrina una palaba con mayusucalas y minusuclas: ")
letrasMayusculas(palabra)

while (True):
    salir = 1
    print("Cero para salir")
    cumpleanios = {}
    nombre = input("indique nombre: ")
    edad = str(input("indique año: "))
    cumpleanios[nombre] = edad
    salir = input()
    if salir == '0':
        break

def calcularEdad(cumpleanios):
    anioActual = 2024
    edades = {}
    for anio in cumpleanios:
       edades[anio] = anioActual -int((cumpleanios[anio]))

    return edades



print(calcularEdad(cumpleanios))


print(palabraLarga(lista))

frase = input("Introduce una frase: ")
palabras = frase.split()  # Dividir la frase en una lista de palabras

palabras_invertidas = [palabra[::-1] for palabra in palabras]  # Invertir cada palabra

frase_invertida = ' '.join(palabras_invertidas)  # Unir las palabras invertidas en una sola frase

print(frase_invertida)

num = 0
loteria = []
loteriaOrdenada = []

while num < 3:
    loteria.append(int(input("indique el numero ")))
    num += 1

loteria.sort(reverse=True)

print(loteria)

divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisabuscada=str(input("indique una divisa "))

if divisabuscada in divisa:
    print("La simbolo de " +divisabuscada +" es " +divisa[divisabuscada])

nombre = input("Indique su nombre: ")
apellido = input("Indique su apellido: ")
edad = input("Indique su edad: ")
tlf = input("Indique su tlf: ")

informacion = {"nombre":nombre, "apellido":apellido, "edad":edad, "tlf":tlf}
print("El usuario " +informacion["nombre"] +" tiene " +informacion["edad"])