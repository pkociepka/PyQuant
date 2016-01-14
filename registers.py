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
        gates_list = [gates.I for x in range(qubit_number)]
        gates_list.append(gate)
        gates_list.extend([gates.I for x in range(self.size - qubit_number - 1)])
        return self.apply(gates_list)

    def apply_cirquit(self, cirquit):
        if not self.size == cirquit.size:
            raise ValueError("Unproper cirquit size")
        for step in cirquit.steps:
            self.apply(step)
        return self

    def shuffle(self, order):
        if not len(order) == self.size:
            raise ValueError("Unproper order for Register.shuffle(): expected %s, got %s" % (self.size, len(order)))
        self.apply([gates.Permutation(order)])
        return self

    def measure(self):
        probabilities = [abs(x)**2 for x in self.values]
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
        print("\nProbabilities of states, %s-qubit register:" % self.size)
        for i in range(2**self.size):
            if abs(self.values[i]) > 10e-5:
                state = format(i, '0%sb' % self.size)
                prob = abs(self.values[i]) ** 2
                print("|%s> : %s" % (state, prob))
        print()
        return self
