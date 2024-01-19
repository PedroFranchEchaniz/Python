words = {}

def cargarTexto():
    with open('palabras.txt', 'r') as file:
        global words
        for line in file.readlines():
            word = line.strip()
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words

print("Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    [1] – Importar palabras clave
    
    [2] – Mostrar palabras clave

    [0] – Salir""")
    opcion = input()

    if opcion == '1':
        cargarTexto()

    elif opcion == '2':
        for word, frequency in words.items():
            print(f"{word}: {frequency}")

    elif opcion =='0':
        print("Saliendo del programa")
        break

    else:
        print("Comando desconocido, vuelve a intentarlo")

