def inverse(tab):
    l = []
    for i in reversed(range(len(tab))):
        l.append(tab[i])
    return l


def inverse_2(tab):
    return list(reversed(tab))


liste = [1,2,3]
print(inverse_2(liste))


def maxDes2(tab1, tab2):
    return list(map(max, zip(tab1, tab2)))


liste1 = [1,2,5]
liste2 = [0,3,3]
print(maxDes2(liste1, liste2))