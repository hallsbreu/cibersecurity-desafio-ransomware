import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    os.remove(file_path)  # Remove o arquivo original

def encrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

if __name__ == "__main__":
    target_dir = input("Digite o diretório alvo: ")
    key = generate_key()
    encrypt_directory(target_dir, key)
    with open("key.txt", "wb") as key_file:
        key_file.write(key)
    print("Arquivos criptografados. Chave salva em key.txt")
