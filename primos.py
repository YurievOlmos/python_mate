lista_primos = []

def es_primo(num):
    if num < 2:
        return False
    indice = 0
    while lista_primos[indice] < int(num**0.5) + 1 :
        if num % lista_primos[indice] == 0:
            return False
        indice += 1
    if num > lista_primos[lista_primos.__len__() - 1]:
        lista_primos.append(num)
    return True

lista_primos.append(2)
cuenta = 1
for i in range(1, 5000):
    numero = 2*i + 1
    if es_primo(numero):
        cuenta = cuenta + 1

salir =  False
while not salir:
    print("ingresa un numero para verificar si es primo:")
    numera = int(input())
    if es_primo(numera) == True:
        print("es primo")
    else:
        print("no es primo")
