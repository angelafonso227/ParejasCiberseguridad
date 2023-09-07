import os

os.chdir('D:\Documentos\ACTIVIDADES TEC\QUINTO SEMESTRE\Ciberseguridad\ParejasCiberseguridad\Cipher')

with open('cipher2.txt', 'r') as archivo:
    contenido = archivo.read()

cadenas_de_cuatro = []

for i in range(0, len(contenido), 4):
    cadena = contenido[i:i+4]
    cadenas_de_cuatro.append(cadena)

for cadena in cadenas_de_cuatro:
    print(cadena)