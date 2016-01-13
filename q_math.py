import math
from numpy import dot as npdot, kron as npkron, array as array

def kron(matrices):
    res = matrices[0]
    for m in matrices[1:]:
        res = npkron(res, m)
    return res

def dot(matrices):
    res = matrices[0]
    for m in matrices[1:]:
        res = npdot(res, m)
    return res

def shuffle(x, order=None):
    """Reorganizes the given string according the order - list of character indices.
    """
    if order == None:
        return x

    res = ""
    for o in order:
        res += x[o]
    return res

def indices(order):
    """Returns list of all 2^n binary indices sorted by given order - positions of digits.
    """
    n = len(order)
    states = [format(x, '0%sb' % n) for x in range(2**n)]
    return [int(x, base=2) for x in sorted(states, key=lambda x: shuffle(x, order))]
