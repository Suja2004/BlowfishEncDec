from flask import Flask, render_template, request
import binascii

app = Flask(__name__)

def generate_key(key_text):
    """
    Generate a key for encryption.
    Ensures the key length is between 4 and 56 bytes.
    """
    key = key_text.encode('utf-8')
    if len(key) < 4 or len(key) > 56:
        raise ValueError("Key length must be between 4 and 56 bytes.")
    return key

def pad(data, block_size):
    """
    Add padding to the plaintext to make its length a multiple of block_size.
    """
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

def unpad(data):
    """
    Remove padding from the decrypted plaintext.
    """
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt(plaintext, key_text):
    """
    Encrypt plaintext using a basic XOR encryption (for demo purposes).
    Returns ciphertext (for educational use, not production-grade).
    """
    key = generate_key(key_text)
    block_size = 8
    iv = b"12345678"  # Example fixed IV (not secure in real scenarios)
    plaintext = pad(plaintext.encode('utf-8'), block_size)

    ciphertext = bytearray()
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i+block_size]
        # Basic XOR encryption
        encrypted_block = bytes(a ^ b for a, b in zip(block, iv))
        ciphertext.extend(encrypted_block)
        iv = encrypted_block  # Update IV for CBC mode

    return ciphertext

def decrypt(ciphertext, key_text):
    """
    Decrypt ciphertext using a basic XOR encryption (for demo purposes).
    Returns the original plaintext.
    """
    key = generate_key(key_text)
    block_size = 8
    iv = b"12345678"  # Example fixed IV (must match encryption IV)

    plaintext = bytearray()
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = bytes(a ^ b for a, b in zip(block, iv))
        plaintext.extend(decrypted_block)
        iv = block  # Update IV for CBC mode

    return unpad(plaintext).decode('utf-8')


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form["action"]
        key_text = request.form["key"]
        
        if action == "encrypt":
            plaintext = request.form["plaintext"]
            try:
                ciphertext = encrypt(plaintext, key_text)
                return render_template("index.html", ciphertext=binascii.hexlify(ciphertext).decode())
            except ValueError as e:
                return render_template("index.html", error=str(e))
        elif action == "decrypt":
            ciphertext_hex = request.form["ciphertext"]
            try:
                ciphertext = binascii.unhexlify(ciphertext_hex)
                decrypted_text = decrypt(ciphertext, key_text)
                return render_template("index.html", decrypted=decrypted_text)
            except Exception as e:
                return render_template("index.html", error="Decryption failed: " + str(e))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
