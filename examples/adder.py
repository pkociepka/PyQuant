import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cirquits import *
import gates

# half-adder
Sum = Cirquit(3).add_controlled_gate(gates.Not, 2, 1)\
                .add_controlled_gate(gates.Not, 2, 0)
