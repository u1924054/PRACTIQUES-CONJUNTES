


file  = open('observacions.txt',"rU")

class Data:
    #atributs de la clase 
    dia = 0
    mes = 0
    any = 0

    # constructor sense parametres 

    def __init__(self,data):
        self.dia = data%100
        data = data /100
        self.mes = data%100
        data = data /100
        self.any = data

    def __repr__(self):
        return '(' + str(self.dia) + '/' + str(self.mes) + '/' + str(self.any) + ')'
    

class Especie:
    nom = ''
    nIndividus = 0
    data = 0

    #constructor
    def __init__(self):
        self.nom = ''
        self.nIndividus = 0
        self.data = Data(0)

    def __init__(self,nom,nIndividus,data):
        self.nom = nom
        self.nIndividus = nIndividus
        self.data = Data(data)

    def getNom(self):
        return self.nom
    
    def getObservacions(self):
        return self.nObservacions
    
    def getData(self):
        return self.data

    def setData(self,data):
        self.data = data

    def afegirObservacions(self,nIndividus):
        self.nIndividus+=nIndividus

    def __repr__(self):
        return self.nom + ' ' + str(self.nIndividus) + ' ' + self.data.__repr__()



class Municipi:
    nom = ''
    nObservacions = 0


    #constructor
    def __init__(self):
        self.nom = ''
        self.nObservacions=0


    def __init__(self,nom,nObservacions):
        self.nom = nom
        self.nObservacions=nObservacions

    
    def __repr__(self):
        return self.nom + ' ' + str(self.nObservacions)

    def afegirObservacions(self,observacions):
        self.nObservacions += observacions

    def getNom(self):
        return self.nom
    
    def getObservacions(self):
        return self.nObservacions
    

    
       
llistaMunicipis = []
llistaEspecies = []
#retorna -1 si municipi no existeix a la llista , posicio altrament
def existeixMunicipi(nom):
    posicio = -1
    for x in llistaMunicipis:
        if x.getNom() == nom:
            posicio = llistaMunicipis.index(x)
            break
    return posicio

def existeixEspecie(nom):
    posicio = -1
    for x in llistaEspecies:
        if x.getNom() == nom:
            posicio = llistaEspecies.index(x)
            break
    return posicio

for line in file:
    llistaDeParaules = []
    for word in line.split():
        llistaDeParaules.append(word)
    #ara ja tinc la una llista amb la linia separada per paraules 

    
    index = existeixMunicipi(llistaDeParaules[1])
    index2 = existeixEspecie(llistaDeParaules[0])
    if index != -1:
        llistaMunicipis[index].afegirObservacions(int(llistaDeParaules[2]))
    else:
        llistaMunicipis.append(Municipi(llistaDeParaules[1],int(llistaDeParaules[2])))
    if index2 != -1:
        llistaEspecies[index].afegirObservacions(int(llistaDeParaules[2]))
    else:
        llistaEspecies.append(Especie(llistaDeParaules[0],int(llistaDeParaules[2]),int(llistaDeParaules[3])))

print('\n')
print('Llista de municipis ')
for x in llistaMunicipis:
    print(x)

print('\n')
print('Llista de Especies ')

for y in llistaEspecies:
    print(y)

print('\n')
        

