from numpy import exp, pi, sqrt, add
from q_math import *

I = [[1, 0],
     [0, 1]]

Id = lambda n: kron([I]*n)

X = [[0, 1],
     [1, 0]]

Y = [[0, -1j],
     [1j, 0]]

Z = [[1, 0],
     [0, -1]]

H = dot([1/sqrt(2), [[1, 1],
                     [1, -1]]])

R = lambda phi: [[1, 0],
                 [0, exp(1j*pi/phi)]]

def controlled(gate, size=1, c_bit="up"):
    if c_bit == "up":
        return add(kron([Up_l, Id(size)]), kron([Lo_r, gate]))
    elif c_bit == "down":
        return add(kron([Id(size), Up_l]), kron([gate, Lo_r]))

def double_controlled(gate, size=1, c_bit="up"):
    if c_bit == "up":
        return add(kron([Up_l, Id(size+1)]),
                   kron([Lo_r, controlled(gate, size, c_bit)]))
    elif c_bit == "down":
        return add(kron([Id(size+1), Up_l]),
                   kron([controlled(gate, size, c_bit), Lo_r]))

Not = X
CNot = controlled(X)
CCNot = controlled(CNot, size=2)
Toffoli = CCNot

Swap = [[1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]]

sqrtSwap = [[1, 0,          0,          0],
            [0, 0.5*(1+1j), 0.5*(1-1j), 0],
            [0, 0.5*(1-1j), 0.5*(1+1j), 0],
            [0, 0,          0,          1]]

Fredkin = controlled(Swap, size=2)

def Permutation(order):
    ind = indices(order)
    n = len(order)
    P = [[0 for x in range(2**n)] for x in range(2**n)]
    for i in range(2**n):
        P[i][ind[i]] = 1
    return P
