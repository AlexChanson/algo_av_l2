from cm.tree import AB
from cm.collection import Pile

def abTest():
    D = AB("D")
    F = AB("F")
    G = AB("G")
    E = AB("E", F, G)
    C = AB("C", D, None)
    B = AB("B")
    A = AB("A", C, B)
    return AB("0", A, E)

def abrTest():
    D = AB(6)
    F = AB(23)
    G = AB(45)
    E = AB(26, F, G)
    C = AB(5, D, None)
    B = AB(10)
    A = AB(9, C, B)
    return AB(12, A, E)


def strahler(A):
    if A is None:
        return 0
    else:
        Sg = strahler(A.g)
        Sd = strahler(A.d)
        if Sg == Sd:
            return 1 + Sg
        else:
            return max(Sg, Sd)

def afficherA(AB):
    def aff(AB, decalage):
        if AB is None:
            print(decalage * "  " + "x")
        elif AB.estFeuille():
            print(decalage * "  " + "|-->"
			+ str(AB.etiquette))
        else:
            print(decalage * "  " + "|-->"
			+ str(AB.etiquette))
            aff(AB.g, decalage + 1)
            aff(AB.d, decalage + 1)
    aff(AB,0)

def prefix(A : AB):
    l = []
    f = Pile()
    f.push(A)
    while len(f) > 0:
        candidat = f.pop()
        l.append(candidat.etiquette)
        if candidat.d is not None:
            f.push(candidat.d)
        if candidat.g is not None:
            f.push(candidat.g)

    return l


#(0, A, C, D, B, E, F, G)
print(prefix(abTest()))


def egalite(A, B):
    return (A is None and B is None) or (A.etiquette == B.etiquette and egalite(A.g, B.g) and egalite(A.d, B.d))

def abrCoupure(A, x):
    if A is None:
        return None, None
    elif A.etiquette == x:
        return A.g, A.d
    else:
        if A.etiquette > x:
            gg, gd = abrCoupure(A.g, x)
            return gg, AB(A.etiquette, gd, A.d)
        else:
            dg, dd = abrCoupure(A.d, x)
            return AB(A.etiquette, A.g, dg), dd


g, d = abrCoupure(abrTest(), 23)
afficherA(abrTest())
afficherA(g)
afficherA(d)