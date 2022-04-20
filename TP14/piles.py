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



