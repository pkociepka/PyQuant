import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cirquits import *
import gates

def QFT(n):
    cirq = Cirquit(n)
    for i in range(n):
        cirq.add_gate(gates.H, qubit_number=i)
        for j in range(2, n-i):
            cirq.add_controlled_gate(gates.R(j), qubit_number=i, control_qubit=i+j)
    cirq.add_step([gates.Permutation(list(reversed(range(n))))])
    return cirq
