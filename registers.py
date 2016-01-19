import random
from math import sqrt

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
        return self.normalize()
        # return self

    def normalize(self):
        s = sqrt(sum([abs(x)**2 for x in self.values]))
        if not s == 1:
            for i in range(len(self.values)):
                self.values[i] = self.values[i]/s
        return self

    def fix_state(self, state):
        self.values = [0 for i in range(2**self.size)]
        self.values[state] = 1
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

    def add_qubits(self, n, location="bottom"):
        self.size += n
        extension = [0 for z in range(2**n)]
        extension[0] = 1
        if location == "top":
            self.values = kron([extension, self.values])
        elif location == "bottom":
            self.values = kron([self.values, extension])
        return self

    def extend(self, register, location="bottom"):
        self.size += register.size
        if location == "top":
            self.values = kron([register.values, self.values])
        elif location == "bottom":
            self.values = kron([self.values, register.values])
        return self

    def remove_qubit(self, qubit):
        new_vals = []
        for i in range(2**(self.size-1)):
            state = format(i, '0%sb' % (self.size-1))
            # states of the register with our qubit set to 0 and 1
            state0 = int(state[:qubit] + "0" + state[qubit:], base=2)
            state1 = int(state[:qubit] + "1" + state[qubit:], base=2)
            new_vals.append(sqrt(abs(self.values[state0])**2 + abs(self.values[state1])**2))

        self.size -= 1
        self.values = new_vals[:]
        return self

    def remove_qubits(self, qubits):
        for qubit in reversed(sorted(qubits)):
            self.remove_qubit(qubit)
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
