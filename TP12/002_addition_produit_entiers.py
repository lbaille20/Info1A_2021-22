## https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python
## https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.lagrange.html


from time import time, perf_counter
from random import randrange

temps_debut = time()

pmax = 1000000
Lp, Lta, Ltm = [], [], []

p = 0
while p < pmax:
    p += pmax // 100
    Lp.append(p)
    a1, a2 = randrange(2**(p-1), 2**p), randrange(2**(p-1), 2**p)
    dmin = float('inf')
    for k in range(20):
        t0 = perf_counter()
        a1 + a2
        t1 = perf_counter()
        d = t1 - t0
        dmin = min(dmin, d)
    Lta.append(dmin)
    
    dmin = float('inf')
    for k in range(20):
        t0 = perf_counter()
        a1 * a2
        t1 = perf_counter()
        d = t1 - t0
        dmin = min(dmin, d)
    Ltm.append(dmin)

tsim = time() - temps_debut
print("Durée de la simulation :", tsim)

import matplotlib.pyplot as plt

# https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.subplots.html
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (9.8, 3))

ax1.plot(Lp, Lta, 'r', label = "addition")
ax1.legend()

ax2.plot(Lp, Lta, 'r', label = "addition")
ax2.plot(Lp, Ltm, 'b', label = "multiplication")
ax2.legend()
plt.savefig(f'fig002_p_max={pmax}_tsim={tsim:.2f}.png')
plt.show()

## Rapports

Lta_sur_p = [Lta[i] / Lp[i] for i in range(len(Lp))]
Ltm_sur_p2 = [Ltm[i] / Lp[i] ** 2 for i in range(len(Lp))]

## représentations graphiques

import matplotlib.pyplot as plt

# https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.subplots.html
fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (9.8, 3))

ax1.plot(Lp, Lta_sur_p, 'r', label = "rapports $T_a(p)/p$")
ax1.legend()

ax2.plot(Lp, Ltm_sur_p2, 'r', label = "rapports $T_m(p)/p^2$")
ax2.legend()
plt.savefig(f'fig002_rapports_p_max={pmax}_tsim={tsim:.2f}.png')
plt.show()


