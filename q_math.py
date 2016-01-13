from numpy import dot as npdot, kron as npkron

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
