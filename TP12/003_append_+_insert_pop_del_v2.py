def temps_min1L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        L.append(0)
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.pop()
        assert len(L) == n
    return tmin

def temps_min2L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        L = L + [0]
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.pop()
        assert len(L) == n
    return tmin

def temps_min3L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        L.insert(0, 0) ## le premier zéro donne la position d'insertion, le second la valeur à insérer
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.pop()
        assert len(L) == n
    return tmin

def temps_min4L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        L.pop()
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.append(0)
        assert len(L) == n
    return tmin

def temps_min5L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        L.pop(0)
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.append(0)
        assert len(L) == n
    return tmin

def temps_min6L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        del L[-1] ## del L[-1] équivaut à del L[len(L) - 1]
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.append(0)
        assert len(L) == n
    return tmin

def temps_min7L(L, n, m):
    assert len(L) == n
    from time import perf_counter
    tmin = float('inf')
    for i in range(m):
        t0 = perf_counter()
        del L[0]
        t1 = perf_counter()
        tmin = min(tmin, t1 - t0)
        L.append(0)
        assert len(L) == n
    return tmin

#Simulations
from time import time
temps_debut = time() ## ajout pour obtenir le temps nécessaire à la simulation

N = 10 * 10**6
m = 10
#Ln = echantillonnage(N // 100, N, N // 100) ## la liste comporte 101 valeurs avec un pas de N // 100 = 100 000
Ln = [n for n in range(N // 100, N + 1, N // 100)]


Lt1, Lt2, Lt3, Lt4, Lt5, Lt6, Lt7 = [], [], [], [], [], [], []
Lts  = [Lt1, Lt2, Lt3, Lt4, Lt5, Lt6, Lt7]
Lf = [temps_min1L, temps_min2L, temps_min3L, temps_min4L, temps_min5L, temps_min6L, temps_min7L]

L = []
for n in Ln:
    L.extend([0] * (N // 100)) 
    for j in range(len(Lts)):
        Lts[j].append(Lf[j](L, n, m)) ## ajout à la liste Lts[j]=Ltj du temps pour la simulation avec Lfj = temps_minjL

tsim = time() - temps_debut
print("Temps pris par la simulation :", tsim)

#Affichages
import matplotlib.pyplot as plt

#fig, ax = plt.subplots(figsize = (10, 3))
fig, ax = plt.subplots()

Llabels = ["append", "insert", "concaténation", "pop en fin", "pop en début", "del en fin", "del en début"]

for i in range(len(Lts)):
    plt.plot(Ln, Lts[i], label = Llabels[i])

plt.legend()
plt.savefig(f'fig003_v2_N={N}-step={N // 100}-m={m}-tsim={tsim:.2f}.png')
plt.show()
