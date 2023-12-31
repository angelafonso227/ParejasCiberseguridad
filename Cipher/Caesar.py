'''
Cfrado de César
Ángel Afonso - A01782545
Daniel Soult - A01782985
'''

import os

os.chdir('D:\Documentos\ACTIVIDADES TEC\QUINTO SEMESTRE\Ciberseguridad\ParejasCiberseguridad\Cipher')

with open("cipher1.txt", 'r') as archivo:
    texto1 = archivo.read()



frecuencia_letras = {}
# Iterar a través del texto
for letras in texto1:
    # Convertir la letra a minúsculas (para tratar mayúsculas y minúsculas por igual)
    letras = letras.lower()
    # Comprobar si la letra es una letra del alfabeto
    if letras.isalpha():
        # Si la letra ya está en el diccionario, aumentar su contador en 1
        if letras in frecuencia_letras:
            frecuencia_letras[letras] += 1
        # Si la letra no está en el diccionario, inicializar su contador en 1
        else:
            frecuencia_letras[letras] = 1

# Encontrar la letra que más se repite
letra_mas_comun = max(frecuencia_letras, key=frecuencia_letras.get)

# Imprimir la letra que más se repite y su frecuencia
print("La llave de este cifrado es la letra:", letra_mas_comun)

letra = letra_mas_comun


alfabeto = "abcdefghijklmnopqrstuvwxyz"

indiceLlave = alfabeto.find(letra)  # Utiliza .upper() para hacer que la búsqueda sea insensible a mayúsculas/minúsculas
if indiceLlave != -1:
    indiceLlave +=1

def descifrar(texto1, abecedario):
    resultado = ""
    for letra in texto1:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nueva_posicion = (indice - indiceLlave) % len(abecedario)
            nueva_letra = abecedario[nueva_posicion]
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado


def cifrar(texto_cifrado, abecedario):
    resultado = ""
    for letra in texto_cifrado:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nueva_posicion = (indice + indiceLlave) % len(abecedario)
            nueva_letra = abecedario[nueva_posicion]
            resultado += nueva_letra
        else:
            resultado += letra
    return resultado

# Ejemplo de uso
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

texto_descifrado = descifrar(texto1, abecedario) #abecedario 

print(texto_descifrado)

texto_cifrado = cifrar(texto_descifrado, abecedario)

print("\nCifrado otra vez: \n", texto_cifrado)