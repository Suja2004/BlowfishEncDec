Blowfish Encryption and Decryption
Overview
Blowfish is a symmetric-key block cipher that is designed to be fast and secure. It encrypts data in fixed-size blocks (64 bits) using a variable-length key, ranging from 32 bits to 448 bits. Blowfish is widely used for encrypting sensitive data due to its speed and effectiveness, making it a popular choice in various applications.

This repository contains a simple web application for Blowfish encryption and decryption using JavaScript for the frontend and Python for the backend (with optional Flask integration).

Features
Encrypts plaintext into ciphertext using the Blowfish algorithm.
Decrypts ciphertext back to the original plaintext.
User-friendly web interface for inputting keys, plaintext, and ciphertext.
Displays results in hexadecimal format for easy transfer and readability.
How Blowfish Works
Key Generation: The encryption key is derived from user input and is validated to ensure it meets the required length (4 to 56 bytes).
Initialization Vector (IV): Blowfish uses an IV to enhance security. A random IV is generated during encryption and is prepended to the ciphertext for use during decryption.
Padding: Since Blowfish operates on fixed-size blocks, plaintext that is not a multiple of the block size is padded before encryption.
Modes of Operation: The implementation uses CBC (Cipher Block Chaining) mode, which requires an IV and ensures that identical plaintext blocks will produce different ciphertexts.
Implementation
Frontend (HTML/CSS/JavaScript)
The web application is built using HTML for structure, CSS for styling, and JavaScript for the encryption and decryption logic. The main JavaScript functions are as follows:

encrypt(): This function takes user input for the key and plaintext, encrypts the plaintext using the Blowfish algorithm, and displays the ciphertext.
decrypt(): This function takes the ciphertext input, decrypts it using the provided key, and displays the original plaintext.
Backend (Python)
The backend can be implemented using Python. The main components are:

generate_key(key_text): Validates and converts the key input into bytes.
encrypt(plaintext, key_text): Encrypts the plaintext using the Blowfish algorithm and returns the ciphertext.
decrypt(ciphertext, key_text): Decrypts the provided ciphertext back into plaintext.

Usage
Encryption:

Enter your encryption key (4-56 characters).
Input the plaintext message to encrypt.
Click "Encrypt" to view the ciphertext in hexadecimal format.
Decryption:

Enter the same encryption key.
Paste the ciphertext (in hexadecimal format) into the input field.
Click "Decrypt" to view the original plaintext message.
Example
Key: mysecretkey
Plaintext: Hello, World!
Ciphertext (Hex): 1a2b3c4d5e6f7081...
Decrypted Text: Hello, World!
