# El jugador pot entrar per teclat pedra, paper o tisores

continuar = input("Entre (s) per iniciar jugada (n) per finalitzar:\n")

# inici jugada


def guanyador(j1, j2):

     if (j1 == "roca" and j2 == "tisores") or (j1 == "tisores" and j2 == "paper") or (j1 == "paper" and j2 == "roca"):
            print("j1 ha guanyat")
     elif j1 == j2:
            print("Empat")
     else:
        print("j2 ha guanyat")

while continuar != 'n':
    jugador1 = input("Jugador 1, quina es la teva jugada: ")
    jugador2 = input("Jugador 2, quina es la teva jugada: ")
    guanyador(jugador1,jugador2)
    continuar = input("Vols continuar jugant? ( 's' per si, 'n' per no ) ")


print("Heu finalitzat la jugada!")

