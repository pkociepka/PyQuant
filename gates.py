from numpy import exp, pi, sqrt
from q_math import *

I = [[1, 0],
     [0, 1]]

Id = lambda n: __kron([I]*n)

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

print(R(1))
print(R(2))
print(R(3))
print(R(4))
