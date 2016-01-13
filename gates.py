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
    Up_l = [[1,0],
            [0,0]]
    Lo_r = [[0,0],
            [0,1]]

    if c_bit == "up":
        return add(kron([Up_l, Id(size)]), kron([Lo_r, gate]))
    elif c_bit == "down":
        return add(kron([Id(size), Up_l]), kron([gate, Lo_r]))

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
