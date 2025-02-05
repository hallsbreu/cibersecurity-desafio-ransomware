import os
from cryptography.fernet import Fernet, InvalidToken

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    try:
        with open(file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        original_path = file_path.replace(".encrypted", "")
        with open(original_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)
        os.remove(file_path)  # Remove o arquivo criptografado
        print(f"Arquivo {original_path} descriptografado.")
    except InvalidToken:
        print("Chave inválida!")

def decrypt_directory(directory, key):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".encrypted"):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

if __name__ == "__main__":
    target_dir = input("Digite o diretório criptografado: ")
    with open("key.txt", "rb") as key_file:
        key = key_file.read()
    decrypt_directory(target_dir, key)
