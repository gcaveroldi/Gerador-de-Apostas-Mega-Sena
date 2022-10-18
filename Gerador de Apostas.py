from random import *
def geranumeros():
    aposta = []
    i = 1
    while i <= 6:
        numero = randrange(1, 60)
        if not numero in aposta:
            aposta.append(numero)
            i+= 1
    aposta.sort()
    return aposta
i = 1
while i <= 10:
    aposta = tuple(geranumeros())
    print(f"Aposta {i}: {aposta}")
    i+= 1

