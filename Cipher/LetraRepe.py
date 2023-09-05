# Definir el texto
texto = "Lo que sea que se quiera saber cual es la letra que mas se repite"
# Crear un diccionario para almacenar la frecuencia de cada letra
frecuencia_letras = {}
# Iterar a través del texto
for letra in texto:
    # Convertir la letra a minúsculas (para tratar mayúsculas y minúsculas por igual)
    letra = letra.lower()
    # Comprobar si la letra es una letra del alfabeto
    if letra.isalpha():
        # Si la letra ya está en el diccionario, aumentar su contador en 1
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        # Si la letra no está en el diccionario, inicializar su contador en 1
        else:
            frecuencia_letras[letra] = 1

# Encontrar la letra que más se repite
letra_mas_comun = max(frecuencia_letras, key=frecuencia_letras.get)

# Imprimir la letra que más se repite y su frecuencia
print("La letra que más se repite es:", letra_mas_comun)
print("Frecuencia:", frecuencia_letras[letra_mas_comun])
