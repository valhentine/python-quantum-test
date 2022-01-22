from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor

import config

IBMQ.enable_account(config.api_key)
provider = IBMQ.get_provider(hub='ibm-q')

#50090
#49910

#0.5009

#200948
#199052

#0.50237

def getBits(n=5, monitor=False, backend='ibmq_belem'):
    #Init n qbits
    q = QuantumRegister(n,'q')
    c = ClassicalRegister(n,'c')
    circuit = QuantumCircuit(q,c)

    #Put qbits into superposition of 1 and 0
    circuit.x(q)
    circuit.ry(1.53999639882, q)

    circuit.measure(q,c) # Collapse wave function

    backend = provider.get_backend(backend)
    job = execute(circuit, backend, shots=20000, memory=True)

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

b0 = 0
b1 = 0
for bit in bitString:
    if bit == '0':
        b0 += 1
    elif bit == '1':
        b1 += 1
    else:
        print('HOW:? ', end='')
        print(bit)

print()
print(b0)
print(b1)

print()
print(b0 / (b0 + b1))