def cifradoc(texto, n):
    resultado = ""

    for letra in texto:
        resultado += chr(ord(letra) + n)

    return resultado

msj= input('Ingrese un mensaje: ')

cifrado = cifradoc(msj, 2)
print('Cifrado: ', cifrado)

descifrado = cifradoc(cifrado, -2)
print('Descifrado: ', descifrado)