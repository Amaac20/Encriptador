texto = input("Ingrese un texto: ")

llave = "Uide2026"

def xor_stream(texto, llave):
    resultado = ""

    for i in range(len(texto)):

        letra = ord(texto[i])

        bit_llave = ord(llave[i % len(llave)])

        cifrado = letra ^ bit_llave

        resultado += chr(cifrado)

    return resultado


print("Llave:", llave)

textoCifrado = xor_stream(texto, llave)
print("Texto cifrado:", textoCifrado)


textoDescifrado = xor_stream(textoCifrado, llave)
print("Texto descifrado:", textoDescifrado)
