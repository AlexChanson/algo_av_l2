import random as rd
import math
import time


# Question 1

def rand(mini, maxi):
    return int((math.floor(rd.random() * (maxi - mini + 1))) + mini)


def test_rand():
    for i in range(1000000):
        a = rand(0, 100)
        if a < 0 or a > 100: print('error')
    print('done')


# test_rand()

def generation(nbval, mini, maxi):
    l = [rand(mini, maxi)]
    i = 1
    while i < nbval:
        l = l + [rand(mini, maxi)]  # l.append(rand(min, max))
        i += 1
    return l


# une solution purement Python
def generationPython(nbval, mini, maxi):
    return [rand(mini, maxi) for i in range(nbval)]


# Question 2
# pour le TP : petite evaluation du temps
# de calcul en faisant varier n
"""
n = 1000
start1 = time.time()
l1 = generation(n, 0, 50)
end1 = time.time()
l2 = generationPython(n, 0, 50)
end2 = time.time()
print("Solution 1 : %f ms vs solution 2 : %f ms" %(end1 - start1, end2 - end1))
"""


# Question 3

def inverse(L):
    res = [0 for i in range(len(L))]
    for i in range(len(L)):
        res[i] = L[len(L) - i - 1]
    return res


def inverse2(L):
    res = []
    for elem in L:
        res = [elem] + res
    return res


def inverse3(L):
    return L[::-1]


"""
n = 100
L = generation(n, 0, 50)

start1 = time.time()
r1 = inverse(L)
end1 = time.time()
r2 = inverse2(L)
end2 = time.time()
r3 = inverse3(L)
end3 = time.time()
print("Solution 1 : %f ms vs solution 2 : %f ms vs solution 3 : %f ms" %(end1 - start1, end2 - end1, end3 - end2))
"""


# Question 4

def unSurN(L, n):
    res = []
    indice = 0
    while indice < len(L):
        if indice % n == 0:
            res.append(L[indice])
        indice += 1
    return res


def unSurNPython(L, n):
    return L[::n]


"""
L = generation(10, 0, 50)
print(L)
print(unSurN(L, 2))
print(unSurN(L, 3))
print(unSurN(L, 10))
"""


# Question 5
def maxDes2(L1, L2):
    mx = [max(L1[0], L2[0])]
    for i in range(1, len(L1)):
        mx.append(max(L1[i], L2[i]))
    return mx


"""
L1 = generation(10,0,100)
print(L1)
L2 = generation(10,0,100)
print(L2)
L3 = maxDes2(L1, L2)
print(L3)
"""


# Question 6
def myzip(L1, L2):
    mx = [[L1[0], L2[0]]]
    for i in range(1, len(L1)):
        mx.append([L1[i], L2[i]])
    return mx


"""
L1 = generation(10,0,100)
print(L1)
L2 = generation(10,0,100)
print(L2)
L3 = myzip(L1, L2)
print(L3)
print(zip(L1,L2))
"""


# Question 7

def genMat(row, col, mini, maxi):
    return [[rand(mini, maxi) for c in range(col)] for r in range(row)]


# print(genMat(3,4, 0, 100))

# Question 8
def diagonale(M):
    diag = [M[0][0]]
    row = len(M)
    col = len(M[0])
    if row != col:
        print("matrice non carree")
        return None
    # matrice carree
    for i in range(1, row):
        diag = diag + [M[i][i]]
    return diag


"""
M1 = genMat(3,3,1,10)
print(M1)
print(diagonale(M1))
"""


# Question 9

def trace(M):
    tr = M[0][0]
    row = len(M)
    col = len(M[0])
    if row != col:
        print("matrice non carree")
        return None
    # matrice carree
    for i in range(1, row):
        tr = tr + M[i][i]
    return tr


"""
M1 = genMat(3,3,1,10)
print(M1)
print(trace(M1))
"""


# Question 10
def somme(M1, M2):
    """
    Hypothese:  M1 et M2 de meme taille
    """
    # creation d'une copie de M1
    # mais possibilite de partir d'une matrice
    # contenant des 0
    res = [[M1[i][j] for j in range(len(M1[i]))] for i in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            res[i][j] += M2[i][j]
    return res


def somme2(M1, M2):
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[i]))] for i in range(len(M1))]


"""
M1 = genMat(3,3,1,10)
print(M1)
M2 = genMat(3,3,1,10)
print(M2)
print(somme(M1, M2))
print(somme2(M1, M2))
"""


# Question 11

def terme(M1, M2, i, j):
    res = 0
    for k in range(len(M1[i])):
        res += (M1[i][k] * M2[k][j])
    return res


def produit(M1, M2):
    return [[terme(M1, M2, i, j) for j in range(len(M2[0]))] for i in range(len(M1))]


"""
M1 = genMat(3,3,0,4)
print(M1)
M2 = genMat(3,3,0,4)
print(M2)
print(produit(M1, M2))
"""


# Question 12

def estDivisible(n, m):
    if n == 0:  # opt. or n == m
        return True
    elif n < m:
        return False
    else:
        return estDivisible(n - m, m)


"""
for i in range(0,10):
    n = rand(0,100)
    m = rand(0,99) + 1
    res = estDivisible(n, m)
    print("%d divisible par %d : %d" %(n, m, res))
"""


# Question 13

def palin(L, deb, fin):
    if deb >= fin:
        return True
    else:
        return L[deb] == L[fin] and palin(L, deb + 1, fin - 1)


def palindrome(L):
    return palin(L, 0, len(L) - 1)


"""
L1 = [1,2,2,1]
L2 = [1,2,3,2,1]
L3 = [1,2,3,3,1]
print(palindrome(L1), palindrome(L2), palindrome(L3))
"""


# Question 14

def longueur(n):
    if n < 10:
        return 1
    else:
        return 1 + longueur(n // 10)


"""
for i in range(10):
    a = rand(0,1000)
    print("%d contient %d chiffre(s)" %(a, longueur(a)))
"""


# Question 15

def combienInf4(n):
    if n < 10:
        if n <= 4:
            return 1
        else:
            return 0
    else:
        m = n % 10
        inc = 0
        if m <= 4:
            inc = 1
        return inc + combienInf4(n // 10)


"""
for i in range(10):
    a = rand(0,10000)
    print("%d contient %d chiffre(s)" %(a, combienInf4(a)))
"""