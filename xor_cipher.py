import random

texto = "Uide2026 seguridad"

def generarLlave(longitud):

    llave = ""

    for i in range(longitud):
        llave += random.choice("01")

    return llave


def xor_stream(texto, llave):

    resultado = ""

    for i in range(len(texto)):

        letra = ord(texto[i])

        bitLlave = int(llave[i])

        cifrado = letra ^ bitLlave

        resultado += chr(cifrado)

    return resultado



llave = generarLlave(len(texto))

print("Texto original:", texto)

print("Llave:", llave)


textoCifrado = xor_stream(texto, llave)
print("Texto cifrado:", textoCifrado)


textoDescifrado = xor_stream(textoCifrado, llave)
print("Texto descifrado:", textoDescifrado) textoDescifrado)
