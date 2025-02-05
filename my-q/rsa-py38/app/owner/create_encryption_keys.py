from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# THIS DEOS A BETTER JOB AT ENCAPSULATING SECRET DATA FOR MEMORY LEAKS

def make_private_pem(keyname="private_key.pem"):
  # Generate RSA private and public keys
  private_key = rsa.generate_private_key(
      public_exponent=65537,
      key_size=2048,
  )

  # Save the keys to files (optional)
  with open(keyname, "wb") as f:
      f.write(private_key.private_bytes(
          encoding=serialization.Encoding.PEM,
          format=serialization.PrivateFormat.PKCS8,
          encryption_algorithm=serialization.NoEncryption(),
      ))
  return keyname

def make_public_pem(private_key_path, public_key_path="public_key.pem"):
  with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  # If the key is encrypted, provide the password here
        backend=default_backend()
    )
    public_key = private_key.public_key()
    with open(public_key_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ))
  return public_key_path

def encrypt_message(public_key_path="./public_key.pem", ciphertext_file_path="ciphertext.bin", message=b"YourSecretPassword"):
    # Load the public key from a PEM file
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    # Encrypt a message with the public key
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        )
    )
    # Save the ciphertext to a file (optional)
    with open(ciphertext_file_path, "wb") as f:
        f.write(ciphertext)
    print("Encrypted message:", ciphertext)

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

private_key_path = "./app/shared/owner_private_key.pem"
public_key_path = "./app/shared/owner_public_key.pem"
private = make_private_pem(keyname=private_key_path)
public = make_public_pem(private_key_path, public_key_path)
print(f"Created {private} and {public}")


