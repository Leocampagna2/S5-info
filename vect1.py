# CAMPAGNA LEO

# Imports éventuels



# Déclarations des classes et fonctions

class Vecteur:

    def __init__(self, liste):
        self.list = liste
        print('Vecteur crée')

    def dimension(self):
        return len(self.list)

    def get(self, i):
        return self.list[i]

    def afficher(self):
        n = 0
        print("[", end=" ")
        while n < len(self.list):
            print(self.list[n], end=";")
            n += 1
        print("]")

    def somme(self, vect2):
        if self.dimension() != vect2.dimension():
            raise ValueError("Problème, pas la même dimension")
        else:
            Z = []
            for i in range(self.dimension()):
                Z.append(self.get(i) + vect2.get(i))
            return __class__(Z)


class Polynome(Vecteur):

    def __init__(self, scal):
        super().__init__(scal)

    def degre(self):
        return self.dimension

    def afficher(self):
        print("p(x) =", end=" ")
        for i in range(self.dimension()):
            print(self.get(i), 'x', i, end=" ")
            if i != self.dimension() - 1:
                if self.get(i + 1 >= 0):
                    print('+', end=' ')
                    
    def evaluer(self, x):
        res = 0
        for coeff in reversed(self.list):
            res = res * x + coeff
        return res
    
    
# Programme principal

a = Vecteur([10, 20])
b = Vecteur((5, -2, 1, 5))
c = Vecteur(range(4, 8))
d = Vecteur([5, 10])
print(a.dimension())
print(a.get(1))
a.afficher()
b.afficher()
a.somme(d).afficher()   
a = Polynome([10, 20])
b = Polynome([3,8])
a.somme(b).afficher()
print(a.evaluer(0))
a.afficher()

