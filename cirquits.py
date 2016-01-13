class Cirquit():
    def __init__(self, size):
        self.size = size
        self.steps = []

    def add_step(self, gates):
        self.steps.append(gates)
        return self

    def print(self):
        print("Size: %s" % self.size)
        print("Steps: %s" % self.steps)
        return self
