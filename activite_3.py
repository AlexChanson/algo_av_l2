from cm.collection import Pile, Node, Couple

def begaieRec(L:Node):
    if L is None:
        return None
    else:
        return Node(L.valeur, Node(L.valeur, begaieRec(L.suivant)))


def zip(L, M):
    '''
    Hypothese : L et M de meme taille et non vides
    '''
    R = Node(Couple(L.valeur, M.valeur))
    p = R
    L = L.suivant
    M = M.suivant
    while L != None:
        p.suivant = Node(Couple(L.valeur, M.valeur))
        p = p.suivant
        L = L.suivant
        M = M.suivant
    return R

def zipRec(L, M):
    if L is None:
        return None
    else:
        return Node(Couple(L.valeur, M.valeur), zip(L.suivant, M.suivant))

def afficherLC(L):
    '''
    Affichage d'une liste de couples
    '''
    print("[")
    while L != None:
        print(L.valeur)
        L = L.suivant
    print("]")


def interStrict(L, M):
    R = None
    p = None
    while L != None and M != None:
        if R is None:
            R = Node(L.valeur, Node(M.valeur))
            p = R.suivant
        else:
            p.suivant = Node(L.valeur, Node(M.valeur))
            p = p.suivant.suivant
        L = L.suivant
        M = M.suivant
    # test quelle liste vide
    if L is None:
        while M != None:
            if R is None:
                R = Node(M.valeur)
                p = R
            else:
                p.suivant = Node(M.valeur)
                p = p.suivant
            M = M.suivant
    else:
        while L != None:
            if R is None:
                R = Node(L.valeur)
                p = R
            else:
                p.suivant = Node(L.valeur)
                p = p.suivant
            L = L.suivant
    return R


def interStrictRec(L, M):
    if L is None:
        return M
    elif M is None:
        return L
    else:
        return Node(L.valeur, Node(M.valeur, interStrictRec(L.suivant, M.suivant)))


def interCroissant(L, M):
    R = None
    p = None
    while L != None and M != None:
        if (L.valeur <= M.valeur):
            if R is None:
                R = Node(L.valeur)
                p = R
            else:
                p.suivant = Node(L.valeur)
                p = p.suivant
            L = L.suivant
        else:  # M has the smallest value
            if R is None:
                R = Node(M.valeur)
                p = R
            else:
                p.suivant = Node(M.valeur)
                p = p.suivant
            M = M.suivant
    # test quelle liste vide
    if L is None:
        while M != None:
            if R is None:
                R = Node(M.valeur)
                p = R
            else:
                p.suivant = Node(M.valeur)
                p = p.suivant
            M = M.suivant
    else:
        while L != None:
            if R is None:
                R = Node(L.valeur)
                p = R
            else:
                p.suivant = Node(L.valeur)
                p = p.suivant
            L = L.suivant
    return R


def interCroissantRec(L, M):
    if L is None:
        return M
    elif M is None:
        return L
    else:
        if L.valeur <= M.valeur:
            return Node(L.valeur, interCroissantRec(L.suivant, M))
        else:
            return Node(M.valeur, interCroissantRec(L, M.suivant))


# realisation d'une calculatrice
# a l'aide d'une structure de pile

def isoperateur(c):
    '''
    char -> boolean
    Determine si un caractere est un operateur
    reconnu
    '''
    return c in '+-*/n'


def calcul(c, op1, op2):
    '''
    char * float * float -> float + None
    Retourne le resultat du calcul
    "op1 c op2" ou None si div par 0
    '''
    if c =='+':
        return float(op1) + float(op2)
    elif c == '-':
        return float(op1) - float(op2)
    elif c == '*':
        return float(op1) * float(op2)
    else:
        if op2 == 0:
            print("Erreur de division par zero")
            return None
        else:
            return float(op1) / float(op2)

def calculatrice():
    '''
    Programme principal de la calculatrice
    '''
    c = ''
    pile = Pile()
    while c != '=':
        c = input("Saisir un nombre ou un operateur : ")
        if c == '=':
            continue
        elif not isoperateur(c):
            pile.push(float(c))
        else:
            if c=='n':
                v = pile.pop() # recuperation de la premiere valeur et maj pile
                pile.push(-1 * v)
            else:
                op2 = pile.pop() # recuperation des 2 operandes
                op1 = pile.pop() # attention operateur 1 stocke
                                     # apres op2 dans la pile
                if op2 is None or op1 is None:
                    print("Operation impossible")
                else:
                    res = calcul(c, op1, op2)
                    # sortie si div par 0
                    if res is None:
                        c = '='
                    else:
                        pile.push(res)
    # au moment du egal, il ne doit y avoir qu'une valeur dans la pile
    if len(pile) == 1:
        v = pile.pop()
        print(" = %d" %(v))
    else:
        print("Formule incorrecte")

calculatrice()