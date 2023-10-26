liste1 = [0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0]
liste2 = [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
liste3 = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]

import math


def compare(a, b, c):
    return math.floor(((a + b + c) / 3) + 0.5)


def maximum(k1, k2, k3):
    max = -math.inf
    for e in [k1, k2, k3]:
        if e > max:
            max = e
    return max


def fusion(l1, l2, l3):
    maxLength = maximum(
        len(l1), len(l2), len(l3)
    )  # Les listes sont elles toutes de la même longeur??
    listF = []
    for i in range(0, maxLength):
        # On lit les listes et au cas ou il manque un élément on met 0.5 car ça change pas le calcule de compare(), pas besoin du if/else sinon
        e1 = l1[i] if len(l1) > i else 0.5
        e2 = l2[i] if len(l2) > i else 0.5
        e3 = l3[i] if len(l3) > i else 0.5
        listF.append(compare(e1, e2, e3))
    return listF


def nombre_erreurs(l1, l2, l3):
    listF = fusion(l1, l2, l3)
    erreurs = [0, 0, 0]
    listes = [l1, l2, l3]

    for indexListe in range(0, len(listes)):
        liste = listes[indexListe]
        for i in range(0, len(liste)):
            if len(liste) <= i:
                erreurs[indexListe] += 1
            else:
                if liste[i] != listF[i]:
                    erreurs[indexListe] += 1
    return erreurs


print(fusion(liste1, liste2, liste3))
print(nombre_erreurs(liste1, liste2, liste3))
