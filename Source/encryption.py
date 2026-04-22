from cryptography.fernet import Fernet
import base64
import hashlib

def derive_key(password):
    # Step 1: convert password to bytes
    password_bytes = password.encode()

    # Step 1: SHA-256 hash
    hashed_password = hashlib.sha256(password_bytes).digest()

    # Step 2: convert to base64 (CORRECT WAY)
    key = base64.urlsafe_b64encode(hashed_password)

    return key

def encrypt_message(message, password):
    # Step 1: get key
    key = derive_key(password)

    # Step 2: create cipher
    cipher = Fernet(key)

    # Step 3: convert message to bytes
    message_bytes = message.encode()

    # Step 4: encrypt
    encrypted_bytes = cipher.encrypt(message_bytes)

    # Step 5: convert to string
    encrypted_text = encrypted_bytes.decode()

    return encrypted_text


def decrypt_message(encrypted_message, password):
    # Step 1: get key
    key = derive_key(password)

    # Step 2: create cipher
    cipher = Fernet(key)

    # Step 3: convert encrypted text to bytes
    encrypted_bytes = encrypted_message.encode()

    # Step 4: decrypt
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Step 5: convert back to string
    original_message = decrypted_bytes.decode()

    return original_message
