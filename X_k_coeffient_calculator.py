import time
import numpy as np
import sympy
from sympy import symbols
from sympy.combinatorics import Permutation
from functools import lru_cache
from itertools import permutations

@lru_cache(maxsize=None)
def factorial(n):
    if n:
        return n * factorial(n-1)
    return 1
@lru_cache(maxsize=None)
def get_list_of_integer_partition(n):
    assert n >= 0, f"n={n} must be positive integer."
    if n == 0:
        return [[]]
    if n == 1:
        return [[1]]
    partitions = []
    for i in range(1, n+1):
        for p in get_list_of_integer_partition(n-i):
            try:
                if p[0] >= i:
                    partitions.append([i] + p)
            except:
                partitions.append([i] + p)
    return partitions

def partition2text(L):
    count = 1
    record = L[0]
    s = "A["
    s += f"{record}"
    for i in L[1:] + [0]:
        if i == record:
            count += 1
        else:
            record = i
            s += f";{count}|{record}"
            count = 1
    return s[:-2] + "]"
    # count = 1
    # record = L[0]
    # s = "∑"
    # s += f"a_{record}"
    # for i in L[1:] + [0]:
    #     if i == record:
    #         count += 1
    #     else:
    #         record = i
    #         s += (f"^{count}" if count > 1 else "") + f"a_{record}"
    #         count = 1
    # return s[:-3]

def get_list_of_permutations(m): # S_m
    for p in permutations(range(m)):
        yield  Permutation(p)
        # yield  Permutation(p).full_cyclic_form

def sort_aux(L): # sort the list of lists
    L = [sorted(a) for a in L]
    return sorted(L)
def set_partition(sigma, L):
    list_ = []
    for ids in sigma:
        list_.append([L[i] for i in ids])
    return sort_aux(list_)
def A_sigma_L(sigma, L):
    A = sympy.S(1)
    P = set_partition(sigma, L)
    for ell in P:
        A *= symbols(partition2text(ell))
    return A

def Cstb(L):
    ans = sympy.S(1)
    dL = np.diff(L)
    for count in np.diff([0] + list(np.argwhere(dL > 0).reshape(-1) + 1) + [len(L)]):
        ans *= factorial(count)
    return sympy.S(ans)

def lemma35(L):
    L = L.copy()
    L = [[i] for i in L]
    return lemma35_aux(L).simplify()
def lemma35_aux(L):
    l = len(L)
    if l == 0:
        return []
    if l == 1:
        return symbols(partition2text(L[0]))
    L1 = L[:-1]
    L_last = L[-1]
    temp = lemma35_aux(L1) * symbols(partition2text(L_last))
    for i in range(l - 1):
        L2 = [a.copy() for a in L1]
        L2[i] += L_last.copy()
        temp -= lemma35_aux(sort_aux(L2))
    return temp

def X_k(k, use_lemma35 = False):
    outer_sum = sympy.S(0)
    for L in get_list_of_integer_partition(k):
        if use_lemma35:
            inner_sum = lemma35(L) # use the algorithm in Lemma 3.5.
        else:
            inner_sum = sympy.S(0)
            for p in get_list_of_permutations(len(L)):
                inner_sum += sympy.S(p.signature()) * A_sigma_L(p.full_cyclic_form, L)
        outer_sum += inner_sum / sympy.S(Cstb(L))
    return outer_sum.simplify()

for k in range(1, 6+1):
    print(k, ":")
    print(X_k(k))
    print("-----------------------")

'''
    Ex:
    For k = 3,
    A[1;1]**3/6 - A[1;1]*A[1;2]/2 + A[1;1]*A[2;1] - A[1;1|2;1] + A[1;3]/3 + A[3;1]
    means
    $
    +\left(\sum\limits_{n=1}^{\infty}a_{n,1}\right)^3/6
    -\left(\sum\limits_{n=1}^{\infty}a_{n,1}\right)\left(\sum\limits_{n=1}^{\infty}a_{n,1}^2\right)/2
    +\left(\sum\limits_{n=1}^{\infty}a_{n,1}\right)\left(\sum\limits_{n=1}^{\infty}a_{n,2}\right)
    -\left(\sum\limits_{n=1}^{\infty}a_{n,1}a_{n,2}\right)
    +\left(\sum\limits_{n=1}^{\infty}a_{n,1}^3\right)/3
    +\left(\sum\limits_{n=1}^{\infty}a_{n,3}\right)
    $
    (this is latex code).
'''


