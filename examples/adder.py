from copy import copy as copy
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cirquits import *
import gates

# half-adder
# order of qubits in input register:
# | carry, a, b >
# order of qubits in output register:
# | carry, a, a+b >
Sum = Cirquit(3).add_controlled_gate(gates.Not, 2, 1)\
                .add_controlled_gate(gates.Not, 2, 0)

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
