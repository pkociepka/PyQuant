import random

from q_math import *
from cirquits import *
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
        self.values = dot([self.values, kron(gates)])
        return self

    def apply_to_qubit(self, gate, qubit_number=0):
        gates = [gates.I for x in range(qubit_number)]
        gates.append(gate)
        gates.extend([gates.I for x in range(self.size - qubit_number - 1)])
        return self.apply(gates)

    def apply_cirquit(self, cirquit):
        if not self.size == cirquit.size:
            raise ValueError("Unproper cirquit size")
        for step in cirquit.steps:
            self.apply(step)
        return self

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

    def print(self):
        print("Size: %s" % self.size)
        print("Values: %s" % self.values)
        return self
