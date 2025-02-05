def decrypt_message(private_key_path, ciphertext_file_path):
  with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  # If the key is encrypted, provide the password here
        backend=default_backend()
    )

    # Read the ciphertext from a file
    with open(ciphertext_file_path, "rb") as f:
        ciphertext = f.read()

  plaintext = private_key.decrypt(
      ciphertext,
      padding.OAEP(
          mgf=padding.MGF1(algorithm=hashes.SHA256()),
          algorithm=hashes.SHA256(),
          label=None
      )
  )

  return plaintext

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

private_key_path = "./app/shared/owner_private_key.pem"
public_key_path = "./app/shared/owner_public_key.pem"
ciphertext = "./app/owner/encrypted_message_from_sender.bin"
decrypted_message = decrypt_message(private_key_path, ciphertext_file_path=ciphertext)
print(decrypted_message.decode('utf-8'))  # Decode the bytes to a string
