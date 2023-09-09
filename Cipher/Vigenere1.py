# import os

# os.chdir('D:\Documentos\ACTIVIDADES TEC\QUINTO SEMESTRE\Ciberseguridad\ParejasCiberseguridad\Cipher')

# with open('cipher2.txt', 'r') as archivo:
#     contenido = archivo.read()

# cadenas_de_cuatro = []

# contenido="ripqglqeldbkz ohgfccoetjhsbwe okztgagfqvsoyngaujtybqyeccgpccyopj"

# for i in range(0, len(contenido), 4):
#     cadena = contenido[i:i+4]
#     cadenas_de_cuatro.append(cadena)

# for cadena in cadenas_de_cuatro:
#     print(cadena) 

def descifrarPrimera(texto, abecedario):
    resultado = ""
    contador = 0
    
    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            
            if contador % 4 == 0:  # Cambiar solo la primera letra del grupo de 4
                nueva_posicion = (indice + 7) % len(abecedario)
                nueva_letra = abecedario[nueva_posicion]
            else:
                nueva_letra = letra
            
            resultado += nueva_letra
            contador += 1
        else:
            resultado += letra
    
    return resultado

def descifrarSegunda(texto, abecedario):
    resultado = ""
    contador = 0
    
    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            
            if contador % 4 == 1:  # Cambiar solo la primera letra del grupo de 4
                nueva_posicion = (indice) % len(abecedario)
                nueva_letra = abecedario[nueva_posicion]
            else:
                nueva_letra = letra
            
            resultado += nueva_letra
            contador += 1
        else:
            resultado += letra
    
    return resultado

def descifrarTercera(texto, abecedario):
    resultado = ""
    contador = 0
    
    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            
            if contador % 4 == 2:  # Cambiar solo la primera letra del grupo de 4
                nueva_posicion = (indice+2) % len(abecedario)
                nueva_letra = abecedario[nueva_posicion]
            else:
                nueva_letra = letra
            
            resultado += nueva_letra
            contador += 1
        else:
            resultado += letra
    
    return resultado

def descifrarCuarta(texto, abecedario):
    resultado = ""
    contador = 0
    
    for letra in texto:
        if letra in abecedario:
            indice = abecedario.index(letra)
            
            if contador % 4 == 3:  # Cambiar solo la primera letra del grupo de 4
                nueva_posicion = (indice+10) % len(abecedario)
                nueva_letra = abecedario[nueva_posicion]
            else:
                nueva_letra = letra
            
            resultado += nueva_letra
            contador += 1
        else:
            resultado += letra
    
    return resultado

# Ejemplo de uso
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
texto_original = "ripqglqeldbkz ohgfccoetjhsbwe okztgagfqvsoyngaujtybqyeccgpccyopj"
texto_cifrado = descifrarPrimera(texto_original, abecedario)
texto_original= texto_cifrado
texto_cifrado = descifrarSegunda(texto_original, abecedario)
texto_original= texto_cifrado
texto_cifrado = descifrarTercera(texto_original, abecedario)
texto_original= texto_cifrado
texto_cifrado = descifrarCuarta(texto_original, abecedario)

print(texto_cifrado)