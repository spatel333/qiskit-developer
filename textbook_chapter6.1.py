# import qiskit
from qiskit import QuantumCircuit, Aer, execute
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# from qiskit.visualization import *
# from qiskit_aer import AerSimulator
# from qiskit_aer import AerSimulator

# from qiskit_aer import Aer

def main():
    # create a 1 qubit circuit with 1 classic register
    qc = QuantumCircuit(1, 1)

    # Pauli X gate
    qc.x(0)

    # measure gate from qubit 0 to classical bit 0
    qc.measure(0, 0)

    # print circuit
    print(qc)

    # backend simulator
    backend = 'qasm_simulator'

    # run in simulator
    job = execute(qc, Aer.get_backend(backend))

    # Show result counts
    print(job.result().get_counts())

    # aersim = AerSimulator()
    # result_ideal = qiskit.execute(qc, aersim).result()
    # print(result_ideal.get_counts(0))

    # Aersimulator()
    # job = execute(qc, Aer.get_backen)
    

    # run in simulator
    # job = execute(qc, Aer.get_backend(backend))

    # # Show result counts
    # print (job.result().get_counts())


if __name__ == '__main__':
    main()