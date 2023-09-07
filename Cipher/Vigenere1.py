# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Lee el contenido del archivo y guárdalo en una variable string
    contenido = archivo.read()

print(contenido)
