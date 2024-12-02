# Blowfish Encryption and Decryption with Flask

## Introduction

This project demonstrates the use of the Blowfish encryption algorithm for secure data encryption and decryption. The application is built using Python and Flask, allowing users to interact with encryption and decryption functionalities through a web interface.

---

## What is Blowfish?

Blowfish is a symmetric-key block cipher designed to provide fast and secure encryption. It is widely used due to its simplicity and efficiency. 

### Key Features of Blowfish:
1. **Symmetric Key**: Uses the same key for encryption and decryption.
2. **Variable Key Length**: Supports key lengths between 32 and 448 bits.
3. **Block Size**: Operates on 64-bit blocks of data.
4. **Security**: Known for being fast and secure when used with proper key management.

### How It Works:
- The plaintext is divided into fixed-size blocks (64 bits).
- Each block undergoes multiple rounds of transformation using the key.
- The result is a ciphertext that is difficult to reverse without the key.

---

## About This Project

### Features:
1. Encrypt plaintext using a key.
2. Decrypt ciphertext back into plaintext using the same key.
3. Web-based interface to input plaintext, keys, and view results.

### Code Highlights:
- **Key Management**: Ensures the key length is valid (4-56 characters) for simplicity.
- **Padding**: Adds padding to ensure data fits the block size (64 bits).
- **XOR-Based Implementation**: For educational purposes, a simple XOR operation is used instead of a real cryptographic library for encryption.
- **Hex Encoding**: Outputs ciphertext in hexadecimal format for easy sharing and readability.

---

## How to Use

### Prerequisites:
1. Python 3.x installed on your system.
2. Flask installed (`pip install flask`).

### Running the Application:
1. Clone this repository or download the project files.
2. Save the Python code in a file named `app.py`.
3. Create an `index.html` file inside a `templates` folder for the user interface.
4. Run the Flask application:
   ```bash
   python app.py
