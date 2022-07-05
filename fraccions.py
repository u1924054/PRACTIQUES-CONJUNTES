# inici d'us de classes en python --> codi reutilitzat de @msarialp


def gcd(n, d):
    while n != d:
        if n > d:
            n = n - d
        else:
            d = d - n
    return n
class Fraction: # declaracio de la classe fraccio 
    def __init__(self, n, d): # Mitjançant __init__, es pot accedir fàcilment a totes les instàncies definides dins d'una classe, inclosos els seus mètodes i atributs.
        self.num = int(n / gcd(abs(n), abs(d))) # s'afageix al seu atribut --> es a dir la operacio es fa sobre el seu atribut (de la classe)
        self.denom = int(d / gcd(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom) # valor absolut
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError
    # definicio de les operacions 
    def Add(self, other): #suma
        return self.num*other.denom + self.denom*other.num, self.denom*other.denom
    def Sub(self, other): #resta
        return self.num*other.denom - self.denom*other.num, self.denom*other.denom
    def Mul(self, other): #multiplicacio
        return self.num*other.num, self.denom*other.denom
    def Div(self, other): #divisio 
        return self.num*other.denom, self.denom*other.num
    def __str__(self): # El mètode __str__ a Python representa els objectes de classe com una cadena
        if type(self) is tuple: # self es utilitzat per representar la instància de classe
            if self[1] < 0:
                return '%s/%s' %(self[0], -1*self[1])
            else:
                return '%s/%s' %(self[0], self[1])
        elif self.denom == 1:
            return str(self.num)
        else:
            return '%s/%s' %(self.num, self.denom)
    # implementat per la comparació entre dos objectes, retornant un valor negatiu si self < other , positiu si self > other i zero si eren iguals. 
    def __cmp__(self, arg):
        if self > arg:
            return -1
        elif self == arg:
            return 0
        else:
            return 1
    def __nonzero__(self):
        if self != 0:
            return True
        else:
            return False
# mirar si es una fraccio i realitzar les operacions que es criden que s'ha preestablert en la classe
def main(): # en aqui es on es cridaran les operacions, on s'iniciara l'objecte, doncs els objectes poden correspondre a coses que es troben al món real i per tant s'inicialitzen realitzen el proces i finalitzen
    f1 = Fraction(2,-2)
    f2 = Fraction(3,-4)
    f3 = Fraction.Add(f1,f2)
    f4 = Fraction.Sub(f1,f2)
    f5 = Fraction.Mul(f1,f2)
    f6 = Fraction.Div(f1,f2)
    f8 = 0
    print(Fraction.__cmp__(f4,f4),Fraction.__str__(f3),Fraction.__str__(f4),Fraction.__str__(f5),Fraction.__str__(f6), Fraction.__str__(f1), Fraction.__str__(f2))
    if Fraction.__nonzero__(f8):
        print("Es una fraccio")
    else:
        print("No es una fraccio!")
    return 0
if __name__ == '__main__':
    main()
