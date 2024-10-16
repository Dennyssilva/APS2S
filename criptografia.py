import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Função para gerar uma chave de criptografia
def generate_key():
    return os.urandom(16)

# Função para calcular o hash do arquivo
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Função para criptografar dados com AES
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + cipher_text

# Função para cadastrar votos
def register_votes(votes):
    votes_string = ""
    for candidate, vote in votes.items():
        votes_string += f"{candidate}:{vote}\n"
    return votes_string

# Exemplo de votos
votes = {
    "Candidate_A": 100,
    "Candidate_B": 200,
    "Candidate_C": 150
}

# Cadastro de votos em uma string
votes_data = register_votes(votes)

# Criação da chave e criptografia do arquivo
key = generate_key()
encrypted_data = encrypt_data(votes_data, key)
with open("votes_encrypted.bin", "wb") as file:
    file.write(encrypted_data)

# Cálculo do hash do arquivo criptografado
file_hash = calculate_hash("votes_encrypted.bin")
with open("votes_hash.txt", "w") as file:
    file.write(file_hash)

# Salva a chave em um arquivo separado
with open("key.bin", "wb") as key_file:
    key_file.write(key)

print("Arquivo criptografado e hash gerado com sucesso.")
