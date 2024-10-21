def ler_resultado_final(senha, nome_arquivo):
    senha_correta = "14112024"
    if senha == senha_correta:
        try:
            with open(nome_arquivo, 'r') as file:
                conteudo = file.read()
                print("Conteúdo do arquivo:")
                print(conteudo)
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
    else:
        print("Senha incorreta. Acesso negado.")

def main():
    senha = input("Digite a senha para acessar o resultado final: ").strip()
    ler_resultado_final(senha, 'resultado_final.txt')

if __name__ == "__main__":
    main()
