from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

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


# byte_text = b"magellic!"  # Replace with your actual ciphertext

def main():
    public_key_path = "./app/shared/owner_public_key.pem"
    ciphertext = "./app/owner/encrypted_message_from_sender.bin"
    try:
        # Read input from the terminal as bytes
        byte_text = input("Enter a string: ").encode('utf-8')
        encrypt_message(public_key_path=public_key_path, ciphertext_file_path=ciphertext, message=byte_text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
