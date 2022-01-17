from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor

import config

IBMQ.enable_account(config.api_key)
provider = IBMQ.get_provider(hub='ibm-q')


def getBits(n=4, monitor=False, backend='ibmq_belem'):
    #Init n qbits
    q = QuantumRegister(n,'q')
    c = ClassicalRegister(n,'c')
    circuit = QuantumCircuit(q,c)

    #Put qbits into superposition of 1 and 0
    circuit.h(q) 

    circuit.measure(q,c) # Collapse wave function

    backend = provider.get_backend(backend)
    job = execute(circuit, backend, shots=64, memory=True) #64 * 4 = 256

    if monitor:
        job_monitor(job)
    
    #Get list of bits as string EX: '1010' 
    bits = job.result().get_memory()

    if monitor:
        print(bits)

    bitString = ''

    for bit in bits:
        bitString += bit
    
    return bitString
    
bitString = getBits(monitor=True)
print('Private Key: ' + str(int(bitString, 2)))