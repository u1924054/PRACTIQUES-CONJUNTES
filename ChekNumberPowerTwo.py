#Programa que mira si un numero es potencia de dos

numero = int(input ("Entra el numero que vols comprovar \n"))


def es_potencia(n):
    return n > 0 and (n & (n-1) == 0)

print(es_potencia(numero))