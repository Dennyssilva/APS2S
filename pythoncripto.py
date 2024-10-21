def hash(texto):
    hash1 = ""
    for i in texto:
        hash1 += str(ord(i) % 11)
    return hash1

def opções(candidatos):
    for nome in candidatos:
        pass  # Removido print dos nomes dos candidatos

def registro_votos(candidatos, votos):
    urna = []
    for candidato, quantidade in votos.items():
        if candidato in candidatos:
            for _ in range(quantidade):
                urna.append(candidato)  # Removido print de confirmação de voto
    return urna

def salvar_arquivo(urna, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        for voto in urna:
            file.write(hash(voto) + '\n')

def somar_votos(urna1, urna2):
    total = {}
    for voto in urna1 + urna2:
        if voto in total:
            total[voto] += 1
        else:
            total[voto] = 1
    return total

def salvar_resultado_final(total_votos, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        for candidato, votos in total_votos.items():
            file.write(f'{candidato.capitalize()}: {votos} votos\n')
    print(f'Arquivo {nome_arquivo} gerado com sucesso.')

def main():
    candidatos = {'branco': 0, 'nulo': 0, 'gabriel': 0, 'teresa': 0, 'alfredo': 0}
    
    # Número de votos por urna
    votos_urna1 = {'branco': 2, 'nulo': 7, 'gabriel': 19, 'teresa': 10, 'alfredo': 7}
    votos_urna2 = {'branco': 0, 'nulo': 2, 'gabriel': 11, 'teresa': 11, 'alfredo': 21}

    # Urna 1
    opções(candidatos)
    urna1 = registro_votos(candidatos, votos_urna1)
    salvar_arquivo(urna1, 'votos_criptografados_urna1.txt')

    # Urna 2
    opções(candidatos)
    urna2 = registro_votos(candidatos, votos_urna2)
    salvar_arquivo(urna2, 'votos_criptografados_urna2.txt')

    # Somar de votos
    total_votos = somar_votos(urna1, urna2)
    salvar_resultado_final(total_votos, 'resultado_final.txt')

if __name__ == "__main__":
    main()
