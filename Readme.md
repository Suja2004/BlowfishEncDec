# Blowfish Encryption and Decryption in Python

This project demonstrates how to use the Blowfish encryption algorithm to securely encrypt and decrypt messages in Python. The implementation includes padding to handle variable-length plaintext and a secure cipher block chaining (CBC) mode for encryption.

## How It Works

### 1. Key Generation
- A valid encryption key must be between **4 and 56 bytes** in length.
- The user provides a key as a string, which is then encoded into bytes for encryption and decryption.

### 2. Encryption Process
- The plaintext message is converted to bytes and padded to ensure its length is a multiple of the Blowfish block size (8 bytes).
- A random **Initialization Vector (IV)** is generated to make the encryption secure and unique.
- The Blowfish cipher, in CBC mode, encrypts the padded plaintext.
- The resulting ciphertext includes the IV prepended to the encrypted message for use during decryption.

### 3. Decryption Process
- The IV is extracted from the first 8 bytes of the ciphertext.
- The remaining bytes represent the actual encrypted message.
- The Blowfish cipher is recreated with the same key and IV to decrypt the message.
- The decrypted message is unpadded to retrieve the original plaintext.

---

## Prerequisites

To run this project, you need:
- Python 3.x
- `pycryptodome` library (for Blowfish encryption)

Install the required library using pip:
```bash
pip install pycryptodome
