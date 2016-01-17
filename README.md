# PyQuant
Library for simulating quantum computations

## Get started

Create a cirquit:
```python
from cirquits import *

n = 2 # number of qubits in register
cirq = Cirquit(2)
```

Add some gates to it:
```python
import gates

cirq.add_gate(gates.Not) # apply Not operation to the first qubit
cirq.add_gate(gates.H, 1) # apply Hadamard operation to the second qubit
```

Create register:
```python
from registers import *

reg = Register(n)
```

Apply your cirquit to the register:
```python
reg.apply_cirquit(cirq)
```

Read the results:
```python
reg.print()
```
```console
Probabilities of states, 2-qubit register:
|10> : 0.5
|11> : 0.5
```

## More features:

Add controlled gate:
```python
cirq.add_controlled_gate(gates.Y) # apply Y operation to 1-st qubit
                                  # controlled by 0-th qubit
cirq.add_controlled_gate(gates.Z, qubit_number=1, control_qubit=0)
                                  # you can personalize this operation
```
and controlled-controlled gate:
```python
cirq.add_controlled_gate(gates.Z, qubit_number=2, control_qubits=[0, 1])
                                  # by default, parameters are given these values
```

##### Quantum measurement:
```python
reg.measure()
reg.print()
```
Previously we had two states, |10> and |11>, with 50% chance to measure each. Measurement collapses it to only one state. Example output:
```console
Probabilities of states, 2-qubit register:
|11> : 1
```

##### Operations chaining:
```python
Register(2).add_gate(gates.X).add_gate(gates.H).measure().print()
```
##### Set the register to be in a certain state:
```python
reg = Register(3).fix_state(5)
# or equivalently
reg = Register(3).fix_state(0b101)

reg.print()
```
```console
Probabilities of states, 2-qubit register:
|101> : 1
```

##### Compose cirquits:
```python
c1 = Cirquit(2).add_gate(gates.Swap)
c2 = Cirquit(2).add_gate(gates.sqrtSwap)
c2.add_cirquit(c1)
```

##### Each quantum operation is reversible:
```python
cirq.reversed() # this operation returns reversed cirq
                # but doesn't cange cirq itself
```

##### Resize a cirquit:
Sometimes we need to compose cirquits with different sizes. We can increase number of qubits in the cirquit:

```python
Cirquit(2).extend(3) # this will make cirquit to operate on
                     # 5-qubits registers
Cirquit(2).extend(1, "top") # you could add new qubits
                            # on the top (more significant bits)
                            # or bottom (less significant)
```

##### Change qubits order in your register:
```python
Register(3).shuffle([2, 0, 1]) # converts a register |abc> into |cab>
```
