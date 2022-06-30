#escrivir contenido en una fichero en vez de imprimir-lo por pantalla


nomFitxer = input("Nom del fitxer on vols guardar el resultat \n")
contingut = input("Entra el contingut que vols posar el fitxer")
obrirFitxer = open(nomFitxer,'w')
obrirFitxer.write(contingut)
obrirFitxer.close()