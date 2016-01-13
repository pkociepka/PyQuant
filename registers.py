import random

from q_math import *
import gates

class Register():
    def __init__(self, size):
        self.size = size
        self.values = [0 for x in range(2**self.size)]
        self.values[0] = 1

    def get_values(self):
        return self.values

    def set_values(self, values):
        if not len(values) == 2**self.size:
            raise ValueError("Wrong quantum register size")
        self.values = values[:]
        return self

    def apply(self, gates):
        print("?")
        print(kron(gates))
        self.values = dot([self.values, kron(gates)])
        print("!")
        print(self.values)
        return self

    def apply_to_qubit(self, gate, qubit_number=0):
        gates = [gates.I for x in range(qubit_number)]
        gates.append(gate)
        gates.extend([gates.I for x in range(self.size - qubit_number - 1)])
        return self.apply(gates)

    def measure(self):
        probabilities = [x**2 for x in self.values]
        for i in range(1, 2**self.size):
            probabilities[i] += probabilities[i-1]
        p = random.random()
        i = 2**self.size - 1
        while i > 0 and probabilities[i-1] > p:
            i -= 1
        self.values = [0 for x in range(2**self.size)]
        self.values[i] = 1
        return self
