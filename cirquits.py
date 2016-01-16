from q_math import *
import gates

class Cirquit():
    def __init__(self, size):
        self.size = size
        self.steps = []

    def add_step(self, gates):
        self.steps.append(gates)
        return self

    def add_gate(self, gate, qubit_number=0):
        step = [gates.I] * qubit_number
        step.append(gate)
        step.extend([gates.I] * (self.size - qubit_number - 1))
        self.add_step(step)
        return self

    def add_controlled_gate(self, gate, qubit_number=1, control_qubit=0):
        ret = []
        if not control_qubit == 0:
            order = swap(list(range(self.size)), 0, control_qubit)
            self.add_step([gates.Permutation(order)])
            ret.append(gates.Permutation(order))
            if qubit_number == 0:
                qubit_number = control_qubit
        if not qubit_number == 1:
            order = swap(list(range(self.size)), 1, qubit_number)
            self.add_step([gates.Permutation(order)])
            ret.append(gates.Permutation(order))

        step = [gates.controlled(gate)]
        step.extend([gates.I] * (self.size - 2))
        self.add_step(step)

        for step in reversed(ret):
            self.add_step([step])

        return self

    def add_double_controlled_gate(self, gate, qubit_number=2, control_qubits=[0, 1]):
        ret = []
        # 1st control qubit
        order = swap(list(range(self.size)), 0, control_qubits[0])
        self.add_step([gates.Permutation(order)])
        ret.append(gates.Permutation(order))
        # 2nd control qubit
        if control_qubits[1] == 0:
            control_qubits[1] = control_qubits[0]
        order = swap(list(range(self.size)), 1, control_qubits[1])
        self.add_step([gates.Permutation(order)])
        ret.append(gates.Permutation(order))

        if qubit_number == 0:
            qubit_number = control_qubits[0]
        elif qubit_number == 1:
            qubit_number = control_qubits[1]
        if not qubit_number == 2:
            order = swap(list(range(self.size)), 2, qubit_number)
            self.add_step([gates.Permutation(order)])
            ret.append(gates.Permutation(order))

        step = [gates.double_controlled(gate)]
        step.extend([gates.I] * (self.size - 3))
        self.add_step(step)

        for step in reversed(ret):
            self.add_step([step])

        return self

    def add_cirquit(self, cirquit):
        if not cirquit.size == self.size:
                raise ValueError("Unproper cirquit size")
        for step in cirquit.steps:
            self.add_step(step)
        return self

    def reversed(self):
        return Cirquit(size=self.size, steps=list(reversed(self.steps)))

    def extend(self, n, location="bottom"):
        self.size += n
        if location == "bottom":
            for s in self.steps:
                s.append(gates.Id(n))
        elif location == "top":
            for s in self.steps:
                s.insert(0, gates.Id(n))
        return self

    def print(self):
        print("Size: %s" % self.size)
        print("Steps: %s" % self.steps)
        return self
