import os

os.chdir('D:\Documentos\ACTIVIDADES TEC\QUINTO SEMESTRE\Ciberseguridad\ParejasCiberseguridad\Cipher')

alfabeto = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alfabeto, range(len(alfabeto))))
index_to_letter = dict(zip(range(len(alfabeto)), alfabeto))

def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alfabeto)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def main():
    with open("cipher2.txt", 'r') as archivo:
        message = archivo.read()
    key = "hack"
    decrypted_message = decrypt(message, key)

    print("Mensaje: " + decrypted_message)


main()
