class Node:
    def __init__(self,valeur, suivant=None):
        self.suivant = suivant
        self.valeur = valeur

    def __iter__(self):
        L = self
        while L is not None:
            yield L.valeur
            L = L.suivant

    def __str__(self):
        return str(self.valeur) + "," + str(self.suivant)


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


class Couple:
    def __init__(self, L, R):
        self.left = L
        self.right = R

    def __repr__(self):
        return f"({self.left},{self.right})"


class Pile:
    def __init__(self, val=None):
        if val is None:
            self.pile = None
        else:
            self.pile = Node(val)

    def push(self, valeur):
        self.pile = Node(valeur, self.pile)
        return self

    def pop(self):
        if self.pile is None:
            return None
        else:
            tmp = self.pile.valeur
            self.pile = self.pile.suivant
            return tmp