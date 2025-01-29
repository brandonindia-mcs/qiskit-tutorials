from qiskit import IBMQ
from qiskit.aqua import QuantumInstance
from qiskit.aqua.algorithms import Shor

# Load your IBMQ account
IBMQ.enable_account('YOUR_API_TOKEN')  # Enter your API token here
provider = IBMQ.get_provider(hub='ibm-q')

# Specify the quantum backend
backend = provider.get_backend('ibmq_qasm_simulator')

# Define the integer to be factored
N = 21

# Create an instance of Shor's algorithm
shor = Shor(N)

# Run the algorithm
quantum_instance = QuantumInstance(backend, shots=1, skip_qobj_validation=False)
result_dict = shor.run(quantum_instance)

# Get the factors from the results
factors = result_dict['factors']
print(f"Factors of {N} are {factors}")

##################################################
##################################################
##################################################
# CLASSICAL CODE

# Function to generate RSA keys
def generate_rsa_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used prime number for e
    d = pow(e, -1, phi)
    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Example usage
p = 61
q = 53
public_key, private_key = generate_rsa_keys(p, q)
message = "HELLO"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")


# Function to decrypt a message using Qiskit
def quantum_decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Example usage
encrypted_message = [2790, 2790, 2790, 2790, 2790]  # Example encrypted message
private_key = (2753, 3233)  # Example private key
decrypted_message = quantum_decrypt(encrypted_message, private_key)

print(f"Decrypted Message: {decrypted_message}")
##################################################
##################################################
##################################################
# QUANTUM

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import numpy as np

# Function to generate RSA keys
def generate_rsa_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used prime number for e
    d = pow(e, -1, phi)
    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

# Example usage
p = 61
q = 53
public_key, private_key = generate_rsa_keys(p, q)
message = "HELLO"
encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")

# Shor's Algorithm Implementation with Logical Qubits
# Now, let's use Qiskit to implement Shor's algorithm to factorize the RSA modulus and decrypt the message.

from qiskit import Aer, execute
from qiskit.circuit.library import QFT
from qiskit.circuit import QuantumCircuit
from qiskit.aqua.algorithms import Shor

# Define the integer to be factored (RSA modulus)
N = 61 * 53  # Example modulus from the RSA keys

# Create an instance of Shor's algorithm
shor = Shor(N)

# Run the algorithm on a quantum simulator
backend = Aer.get_backend('qasm_simulator')
result = shor.run(backend)

# Get the factors from the results
factors = result['factors']
print(f"Factors of {N} are {factors}")

# Decrypt the message using the factors
p, q = factors
public_key, private_key = generate_rsa_keys(p, q)
decrypted_message = decrypt(encrypted_message, private_key)

print(f"Decrypted Message: {decrypted_message}")