import os
import bcrypt

def clear_terminal():
    os.system("clear")

def encrypt_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed

def verify_hash(password: str, hashed: str) -> bool:
    password_bytes = password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed)
