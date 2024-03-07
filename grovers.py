# imports from Builtin
import math

# imports from Qiskit
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit.visualization import plot_distribution

# imports from Qiskit Runtime
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Batch

# Run on hardware
service = QiskitRuntimeService(channel="ibm_quantum")
backend = service.least_busy(operational=True, simulator=False)
print(backend.name)


###Background###
"""
Amplitude amplification is a general purpose quantum algo.
(or subroutine).It is used to obtain a quadratic speedup
over a handful of classical algorithms.

Gover's Algo. was first to demonstrate this speedup on
unstructured search problems. Formulating a Grover's Search
problem requires:
1. an oracle function which marks one or more
computational basis states as the target states,
2. an amplification circuit which increases the amplitude
of marked states (consequently suppressing the remaining
states).

The code below demonstrates:
1. how to construct Grover oracles,
2. how to use the GroverOperator from Qiskit circuit
library to easily set up a Grover's search instance

The runtime Sampler primive allows:
1. seamless execution of Grover circuits,
2. including automatic compilation,
3. error suppression,
4. readout error mitigation techniques

source: https://learning.quantum.ibm.com/tutorial/grovers-algorithm
"""
