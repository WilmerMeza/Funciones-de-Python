try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("¡Error! El archivo no se pudo encontrar👻👻👻👻")
