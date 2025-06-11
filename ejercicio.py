def validarLista():
    while True:
        entrada = input("Ingrese una lista de numeros enteros separados por un espacio: ")
        elementos = entrada.split()
        try:
            numeros = [int(e) for e in elementos]
            return numeros
        except ValueError:
            print("Error: Todos los valores deben ser numeros enteros.")

def clasificarParesImpares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

numeros = validarLista()
pares, impares = clasificarParesImpares(numeros)

print("Numeros pares:", pares)
print("Numeros impares:", impares)
