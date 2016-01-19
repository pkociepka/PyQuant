from copy import deepcopy as deepcopy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cirquits import *
import gates
from registers import *

# half-adder
# order of qubits in input register:
# | carry, a, b >
# order of qubits in output register:
# | carry, a, a+b >
Sum = Cirquit(3).add_controlled_gate(gates.Not, 2, 1)\
                .add_controlled_gate(gates.Not, 2, 0)

sum = lambda: deepcopy(Sum)

# carry gate
# order of qubits in input register:
#   | lower_, a, b, 0 >
# order of qubits in output register:
#   | lower_carry, a, a+b, upper_carry >
# Please, ensure you won't input |1> value
#   for upper_carry qubit
Carry = Cirquit(4).add_double_controlled_gate(gates.Not, 3, [1, 2])\
                  .add_controlled_gate(gates.Not, 2, 1)\
                  .add_double_controlled_gate(gates.Not, 3, [0, 2])

carry = lambda: deepcopy(Carry)

# 1-qubit full adder
# order of qubits in input register:
#   | 0, a, b, 0 >
# order of qubits in output register:
#   | lower_carry, a, a+b+lower_carry, upper_carry >
# Please, ensure you won't input |1> value
#   for upper_carry qubit
Adder = Cirquit(4).add_cirquit(Carry)\
                  .add_controlled_gate(gates.Not, 2, 1)\
                  .add_cirquit(sum().extend(1, location="bottom"))

def adder(n=1):
    Ad = Cirquit(3*n + 1)
    for i in range(n):
        Ad.add_cirquit(carry().extend(3*i, "top")\
                             .extend(3*(n-i-1), "bottom"))
    Ad.add_controlled_gate(gates.Not, qubit_number=3*n-1, control_qubit=3*n-2)
    for i in range(n):
        Ad.add_cirquit(sum().extend(3*(n-i-1), "top")\
                           .extend(3*i+1, "bottom"))
    return Ad

def add(a, b, size):
    # gets two registers of given size
    # returns register of size (size+1) with (a+b) results
    rev_order = list(reversed(range(size)))
    big_rev_order = [size] + rev_order
    c_a_b_order = []
    for i in range(size):
        c_a_b_order += [i+2*size, i, i+size]
    c_a_indices = []
    for i in range(size):
        c_a_indices += [3*i, 3*i+1]

    reg = a.shuffle(rev_order)
    reg.extend(b.shuffle(rev_order))
    reg.extend(Register(size))
    reg.shuffle(c_a_b_order)
    reg.extend(Register(1))
    reg.apply_cirquit(adder(size))
    reg.remove_qubits(c_a_indices)
    reg.shuffle(big_rev_order)
    return reg
