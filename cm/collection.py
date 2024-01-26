class Node:
    def __init__(self,valeur, suivant=None):
        self.suivant = suivant
        self.valeur = valeur


class LinkedList:

    def __init__(self, head=None):
        self.head: Node = head

    def append(self, valeur):
        """
        append(): LinkedList * valeur -> LinkedList
        """
        p = self.head
        if p is None:
            self.head = Node(valeur)
        else:
            while p.suivant is not None:
                p = p.suivant
            p.suivant = Node(valeur)

    def __str__(self):
        """
        str(): LinkedList -> chaine de caracteres
        """
        buf = "["
        p = self.head
        while p is not None:
            buf = buf + str(p.valeur)
            if p.suivant is not None:
                buf = buf + ", "
            p = p.suivant

        buf = buf + "]"
        return buf
