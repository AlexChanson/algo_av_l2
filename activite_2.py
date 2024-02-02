from cm.collection import Node, LinkedList
import random as rd


def inversion(L : Node):
    res = None
    while L != None:
        res = Node(L.valeur, res)
        L = L.suivant
    return res



def carre(L:Node):
    '''
    Node[Nombre] -> None
    '''
    while L != None:
        L.valeur = L.valeur * L.valeur
        L = L.suivant


def carre_lst(L:LinkedList): # Version Linked List
    '''
    LinkedList[Nombre] -> None
    '''
    p = L.head
    while p != None:
        p.valeur = p.valeur * p.valeur
        p = p.suivant


def carre_fin(L:Node):
    if L == None:
        return None
    else:
        P = Node(L.valeur * L.valeur)
        Mem = P
        while L.suivant != None:
            L = L.suivant
            v = L.valeur * L.valeur
            P.suivant = Node(v)
            P = P.suivant
        return Mem
