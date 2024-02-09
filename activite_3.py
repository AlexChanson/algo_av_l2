from cm.collection import LinkedList, Node

def begaieRec(L:Node):
    if L is None:
        return None
    else:
        return Node(L.valeur, Node(L.valeur, begaieRec(L.suivant)))


L = Node(1, Node(2, Node(3, Node(4))))
print(L)
l2 = begaieRec(L)
print(l2)