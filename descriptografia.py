import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Função para calcular o hash do arquivo
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Função para descriptografar dados com AES
def decrypt_data(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    return decrypted_data.decode()

# Função para validar o hash do arquivo
def validate_hash(file_path, provided_hash):
    calculated_hash = calculate_hash(file_path)
    return calculated_hash == provided_hash

# Função para mostrar os resultados
def show_results():
    encrypted_file_path = "votes_encrypted.bin"
    hash_file_path = "votes_hash.txt"
    key_file_path = "key.bin"

    # Leitura da chave
    with open(key_file_path, "rb") as key_file:
        key = key_file.read()

    # Validação do hash
    with open(hash_file_path, "r") as hash_file:
        provided_hash = hash_file.read()
    is_valid = validate_hash(encrypted_file_path, provided_hash)

    if is_valid:
        # Descriptografia dos dados
        with open(encrypted_file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = decrypt_data(encrypted_data, key)

        # Exibição dos resultados
        print("Resultados dos Votos:")
        print(decrypted_data)
    else:
        print("Arquivo inválido ou corrompido.")

# Chamando a função de apuração
show_results()
