class Pile:
    def __init__(self):
        self.liste = []
        
    def est_vide(self):
        return self.liste == []
    
    def empiler(self, x):
        self.liste.append(x)
        
    def depiler(self):
        return self.liste.pop()
    
    def afficher(self):
        nbe = 3
        if len(self.liste) > 0:
            wmax = max(len(str(self.liste[i])) for i in range(len(self.liste)))
            wmax = max(wmax + wmax % 2, len("***sommet***") - 2)
            nbe = max(nbe, (wmax - 2) // 2 - 1)
        print(nbe * "*" + "sommet" + nbe * "*")
        for i in range(-1, -len(self.liste) - 1, -1):
            w = len(str(self.liste[i]))
            padg, padd = (wmax - w) // 2 + (wmax - w) % 2, (wmax - w) // 2
            print("|" + padg * " " + str(self.liste[i]) + padd * " " + "|")
        print(nbe * "*" + " base " + nbe * "*")


class File0:
    def __init__(self):
        self.liste = []
        
    def est_vide(self):
        return self.liste == []
    
    def enfiler(self, x):
        self.liste.insert(0, x)
        
    def defiler(self):
        return self.liste.pop()
    
    def afficher(self):
        print("entrée", end = " -> ")
        for i in range(len(self.liste)):
            print(self.liste[i], end = " -> ")
        print("sortie")

class File:
    def __init__(self):
        self.entree = Pile()
        self.sortie = Pile()
        self.file = (self.entree, self.sortie)
        
    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()
    
    def enfiler(self, x):
        self.entree.empiler(x)
        
    def defiler(self):
        if self.sortie.est_vide():
            while not self.entree.est_vide():
                self.sortie.empiler(self.entree.depiler())
        return self.sortie.depiler()
    
    def afficher(self):
        print("entrée", end = " -> ")
        for i in range(-1, -len(self.entree.liste) - 1, -1):
            print(self.entree.liste[i], end = " -> ")
        for i in range(len(self.sortie.liste)):
            print(self.sortie.liste[i], end = " -> ")
        print("sortie")

