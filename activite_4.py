from cm.collection import Node, Couple, python_to_linked

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


# Liste des frequences
def LFreqRec(L):
    '''
    Hypothese: L non vide
    '''
    if L.suivant is None:
        return Node(Couple(L.valeur, 1))
    else:
        tmp = LFreqRec(L.suivant)
        p = tmp
        update = False  # do we still need to update list
        while p != None and not (update):
            if p.valeur.valeur == L.valeur:
                p.valeur.suivant.valeur = p.valeur.suivant.valeur + 1
                update = True
            p = p.suivant
        if not (update):
            # add a new couple for this new value 
            # at the beginning of the association list
            tmp = Node(Couple(L.valeur, 1), tmp)
        return tmp


# Liste des frequences en iteratif
def LFreq(L):
    '''
    Hypothese: L non vide
    '''
    res = Node(Couple(L.valeur, 1))
    L = L.suivant
    while L != None:
        # update res or insert (L.valeur,1)
        update = False
        p = res
        while p != None and not (update):
            if p.valeur.left == L.valeur:
                p.valeur.right = p.valeur.right + 1
                update = True
            p = p.suivant
        if not (update):
            res = Node(Couple(L.valeur, 1), res)
        L = L.suivant
    return res


# En iteratif
# retourne la liste des elements plus frequents que elem
# dans la liste de frequences
def plusFrequents(L, elem):
    if L is None:
        return None
    else:
        R = None
        p = None
        while L != None:
            if L.valeur.right >= elem:
                if R is None:
                    R = Node(L.valeur)
                    p = R
                else:
                    p.suivant = Node(L.valeur)
                    p = p.suivant
            L = L.suivant
        return R


# En recursif
def plusFrequentsRec(L, elem):
    if L is None:
        return None
    else:
        tmp = plusFrequentsRec(L.suivant, elem)
        if L.valeur.suivant.valeur >= elem:
            tmp = Node(L.valeur, tmp)
        return tmp


# Avec fonctionnelle filter
def plusFrequentsFonc(L, elem):
    def plusFq(cple):
        return cple.right >= elem

    return Lfilter(L, plusFq)


def removeAllF(L, elem):
    '''
    Liste[alpha] * alpha -> Liste[alpha]
    Remove all occurrences of elem in L
    '''
    def isNotElem(x):
        '''
        alpha -> boolean
        Compares the value of an element x of L
        to the argument 'elem' value
        '''
        return x != elem
    return Lfilter(L,isNotElem)

if __name__ == '__main__':


    L = python_to_linked([3,1,2,3,3,4,5,3,9])
    F = LFreq(L)
    print(F)
    # afficherA(LFreq(L))
    print(plusFrequents(F, 1))
    print(plusFrequents(F, 2))

    #afficherA(plusFrequentsRec(F, 1))
    #afficherA(plusFrequentsRec(F, 2))

    print(plusFrequentsFonc(F, 1))
    print(plusFrequentsFonc(F, 2))