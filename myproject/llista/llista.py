# crear una llista de numeros i imprimir nomes els menors de 5 




numbers = [7, 3, 13, 6, 8, 5, 1, 2, 4, 15, 9, 10, 12, 14, 11]

newList = []

def ordenarLista(numbers):
    newList = [] #creem array buida

    for x in numbers:

        if x<5:

            newList.append(x) # afegir a la llista

        newList.sort() # ordenar la llista de menor a major 
    return newList

    #final del for

#mostrar llista

print(ordenarLista(numbers))
