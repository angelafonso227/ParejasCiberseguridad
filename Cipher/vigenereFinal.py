'''
Cifrado de vigenere
Ángel Afonso - A01782545
Daniel Soult - A01782985
'''

#import os

#os.chdir('D:\Documentos\ACTIVIDADES TEC\QUINTO SEMESTRE\Ciberseguridad\ParejasCiberseguridad\Cipher')

alfabeto = "abcdefghijklmnopqrstuvwxyz " # alfabeto con un espacio 

# crear diccionario, para mapear el alfabeto (letras e index)
letra_index = dict(zip(alfabeto, range(len(alfabeto))))
index_letra = dict(zip(range(len(alfabeto)), alfabeto))

def descifrar(cifrado, key):
    resultado = ""
    separar = [cifrado[i : i + len(key)] for i in range(0, len(cifrado), len(key))] # divide el mensaje en partes iguales a la longitud de la llave

    for cada_espacio in separar:
        i = 0
        for letra in cada_espacio:
            num = (letra_index[letra] - letra_index[key[i]]) % len(alfabeto)
            resultado += index_letra[num] # agrega la letra resuelta al resultado
            i += 1

    return resultado


def cifrar(text_cifrar, key):
    res_cifrar = ""
    separar = [text_cifrar[i : i + len(key)] for i in range(0, len(text_cifrar), len(key))] # divide el mensaje en partes iguales a la longitud de la llave

    for cada_espacio in separar:
        i = 0
        for letra in cada_espacio:
            num = (letra_index[letra] + letra_index[key[i]]) % len(alfabeto)
            res_cifrar += index_letra[num] # agrega la letra resuelta al resultado
            i += 1

    return res_cifrar

def main():
    with open("cipher2.txt", 'r') as archivo:
        message = archivo.read()
    key = "hack"
    mensajeDescifrado = descifrar(message, key)
    mensajeCifrado = cifrar(mensajeDescifrado, key)

    print("Mensaje descifrado:")
    print(mensajeDescifrado)
    print("")
    print("Mensaje cifrado: ")
    print(mensajeCifrado)

main()