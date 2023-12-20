from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)


def encrypt(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data


def decrypt(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data
