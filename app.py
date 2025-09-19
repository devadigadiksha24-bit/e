from flask import Flask, request, jsonify
from flask_cors import CORS
from Crypto.Cipher import AES
import base64

app = Flask(__name__)
CORS(app)

def pkcs7_pad(b: bytes, block_size=16) -> bytes:
    pad_len = block_size - (len(b) % block_size)
    return b + bytes([pad_len]) * pad_len

def pkcs7_unpad(b: bytes) -> bytes:
    pad_len = b[-1]
    return b[:-pad_len]

KEY = b"ThisIsA16ByteKey"

@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.json.get("text", "")
    cipher = AES.new(KEY, AES.MODE_ECB)
    enc = cipher.encrypt(pkcs7_pad(text.encode()))
    return jsonify({"result": base64.b64encode(enc).decode()})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    try:
        data = base64.b64decode(request.json.get("text", ""))
        cipher = AES.new(KEY, AES.MODE_ECB)
        dec = pkcs7_unpad(cipher.decrypt(data)).decode()
        return jsonify({"result": dec})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    
