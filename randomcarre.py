# CAMPAGNA Léo #

import matplotlib.pyplot as plt
import random as rd

class Sommet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "".join(("(" , str(self.x) , "," , str(self.y), ")" ))
       
    def __eq__(self, som):
       return (self.x == som.x and self.y == som.y)          

class SommetNom(Sommet):
    def __init__(self, x, y, name):
        super().__init__(x, y)
        self.name= name
       
    def __str__ (self):
        return "".join((self.name, "", "(", str(self.x), ",", str(self.y),")"))

# Oui on peut comparer un Sommet et un SommetNom #

class Polygone:
    def __init__(self, *sommet):
        self.sommet = []

    def __add__(self, sommet):
        new_polygone = Polygone()
        new_polygone.sommet = self.sommet + [sommet]
        return new_polygone
     
    def __iadd__(self, sommet):
        self.sommet.append(sommet)
        return self
   
    def __str__(self):
        res = ""
        for sommet in self.sommet:
            res += str(sommet)+";"
        return f"[{res}]"

    def __len__(self):
        return len(self.sommet)

    def __contains__(self, sommet):
        return sommet in self.sommet
   
    def plot(self):
        x= [sommet.x for sommet in self.sommet]
        y= [sommet.y for sommet in self.sommet]
        x.append(self.sommet[0].x)
        y.append(self.sommet[0].y)
        plt.plot(x,y)
        plt.show()
       
       
class Carré(Polygone):
    def __init__(self, x, y, L):
        self.x = x
        self.y = y
        self.L = L
        self.sommet = [Sommet(x,y), Sommet(x+L,y), Sommet(x+L, y+L), Sommet(x, y+L)]
    
def random_polygone(nsommet, xmax= 10, ymax=10):
    polygone = Polygone()
    for __ in range (nsommet):
        x = rd.uniform(0, xmax)
        y = rd.uniform(0, ymax)
        polygone += Sommet(x, y)
    return polygone 
    
def random_carre(xmax=10, ymax=10, Lmax=6):
    x = rd.uniform(0, xmax)
    y = rd.uniform(0,ymax)
    L = rd.uniform(0, Lmax)
    return Carré(x,y,L)

a = SommetNom(1, 2, "A")
b = Sommet(1, 2)
c = Sommet(26, 8496)

print(a == b)
print(b)
print(a)

P1 = Polygone()
P1 += b
P1 += c

print(P1)
print(len(P1))
print(b in P1)

C = Carré(1,2,2)
C.plot()

carre = random_carre()
carre.plot()