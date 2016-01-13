from numpy import dot, kron, exp, pi

def __kron(matrices):
    res = matrices[0]
    for m in matrices[1:]:
        res = kron(res, m)
    return res

def __dot(matrices):
    res = matrices[0]
    for m in matrices[1:]:
        res = dot(res, m)
    return res

I = [[1, 0],
     [0, 1]]

Id = lambda n: __kron([I]*n)

X = [[0, 1],
     [1, 0]]

Y = [[0, -1j],
     [1j, 0]]

Z = [[1, 0],
     [0, -1]]

H = [[0, 1],
     [1, 0]]

R = lambda phi: [[1, 0],
                 [0, exp(1j*pi/phi)]]
