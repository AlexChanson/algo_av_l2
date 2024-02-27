class AB:
    def __init__(self, etiquette, gauche=None, droite=None):
        self.etiquette = etiquette
        self.g = gauche
        self.d = droite

    def estFeuille(self):
        return self.d is None and self.g is None


def estVide(A):
    return A is None

