from flask import Flask, render_template, request
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)

def generate_key(key_text):
    key = key_text.encode('utf-8')
    if len(key) < 4 or len(key) > 56:
        raise ValueError("Key length must be between 4 and 56 bytes.")
    return key

def encrypt(plaintext, key_text):
    key = generate_key(key_text)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    iv = cipher.iv
    padded_text = pad(plaintext.encode(), Blowfish.block_size)
    ciphertext = iv + cipher.encrypt(padded_text)
    return ciphertext

def decrypt(ciphertext, key_text):
    key = generate_key(key_text)
    iv = ciphertext[:Blowfish.block_size]
    encrypted_message = ciphertext[Blowfish.block_size:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(encrypted_message)
    return unpad(decrypted_padded_text, Blowfish.block_size).decode()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        action = request.form["action"]
        key_text = request.form["key"]
        if action == "encrypt":
            plaintext = request.form["plaintext"]
            ciphertext = encrypt(plaintext, key_text)
            return render_template("index.html", ciphertext=ciphertext.hex())
        elif action == "decrypt":
            ciphertext_hex = request.form["ciphertext"]
            ciphertext = bytes.fromhex(ciphertext_hex)
            decrypted_text = decrypt(ciphertext, key_text)
            return render_template("index.html", decrypted=decrypted_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
