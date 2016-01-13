from q_math import *
import gates

class Register():
    def __init__(self, size):
        self.size = size
        self.values = [0 for x in range(2**size)]
        self.values[0] = 1

    def get_values(self):
        return self.values

    def apply(self, gates):
        print("?")
        print(kron(gates))
        self.values = dot([self.values, kron(gates)])
        print("!")
        print(self.values)
        return self

    def apply_to_qubit(self, gate, qubit_number):
        gates = [gates.I for x in range(qubit_number)]
        gates.append(gate)
        gates.extend([gates.I for x in range(self.size - qubit_number - 1)])
        return self.apply(gates)
