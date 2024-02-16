from collection import Node


def Lfilter(L:Node, f):
    res = None # tete de liste resultat
    w = None # pointeur construction liste resultat
    while L is not None:
        if f(L.valeur):
            if res is None:
                res = Node(L.valeur)
                w = res
            else:
                w.suivant = Node(L.valeur)
                w = w.suivant
        L = L.suivant # element suivant
    return res


def Lmap(L:Node, f):
    res = None # tete de liste resultat
    w = None # pointeur construction liste resultat
    while L is not None:
        if res is None:
            res = Node(f(L.valeur))
            w = res
        else:
            w.suivant = Node(f(L.valeur))
            w = w.suivant
        L = L.suivant # element suivant
    return res


def Lreduce(L:Node, f, neutre):
    tally = neutre
    while L is not None:
        tally = f(tally, L.valeur)
        L = L.suivant
    return tally

