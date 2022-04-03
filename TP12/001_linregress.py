# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
# https://numpy.org/doc/stable/reference/generated/numpy.interp.html

def s(n):
    s = 0 # variable locale s initialisée à 0
    for i in range(n):
        s = s + 1

def temps_min(f, n, m):
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        f(n)
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)    
    return tmin

def echantillonnage(a, b, c):
    L = []
    x = a
    while x < b + 1:
        L.append(x)
        x = x + c
    return L

from time import perf_counter
temps_debut = perf_counter() ## ajout pour obtenir le temps nécessaire à la simulation

N = 100000
Ln = echantillonnage(0, N, N // 100) ## la liste comporte 101 valeurs

Lt = []
for n in Ln:
    Lt.append(temps_min(s, n, 10))

print("Temps pris par la simulation :", perf_counter() - temps_debut)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

a, b, rho ,_ ,_ = linregress(Ln, Lt)  # Régression linéaire
print("a = ", a)                      # Affichage de coefficient directeur
print("b = ", b)                      # Affichage de l'ordonnée à l'origine
print("rho = ", rho)                  # Affichage du coefficient de corrélation

xnew = np.array(Ln)                               # Abscisses pour la fonction affine
ynew = a*xnew + b                     # Ordonnées de la fonction affine

plt.plot(xnew, ynew, '-')             # Tracé de la droite
plt.plot(Ln, Lt, '.')                   # Tracé des points et de la fonction affine
plt.title('Régression linéaire')      # Titre
plt.xlabel('x')                       # Etiquette en abscisse
#plt.xlim(-1,5)                        # Echelle en abscisse
plt.ylabel('y')                       # Etiquette en ordonnée
#plt.ylim(0, 12)                       # Echelle en ordonnée
plt.savefig('fig001.png')
plt.show()                            # Affichage


