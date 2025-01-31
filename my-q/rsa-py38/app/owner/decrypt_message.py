import shutil
# Source path
source = 'owner_public_key.pem'

# Destination path
destination = '../sender/owner_public_key.pem'

# Copy the file
shutil.copy(source, destination)

print(f"File copied from {source} to {destination}")
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

ciphertext = "encrypted_message_from_sender.bin"
decrypted_message = decrypt_message(private_key_path, ciphertext_file_path=ciphertext)
print(decrypted_message.decode('utf-8'))  # Decode the bytes to a string
