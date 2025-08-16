import os

def ler_num(mensagem):
    while True:
        numero_str = input(mensagem)
        numero_str_corrigido = numero_str.replace(',', '.')
        try:
            numero_float = float(numero_str_corrigido)
            return numero_float
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número (ex: 7.5 ou 7,5).")


while True: 

    os.system('cls' if os.name == 'nt' else 'clear')

    num_1 = ler_num("Digite um número: ")
    operacao = input("Escolha uma operação: ")   
    num_2 = ler_num("Digite outro número: ")

    if operacao == '+':
        resultado = num_1 + num_2
    elif operacao == '-':
        resultado = num_1 - num_2
    elif operacao == '*':
        resultado = num_1 * num_2
    elif operacao == '/': 
        if num_2 == 0:
            print("\nErro: Não é possivel dividir por zero.")
            input("Precione Enter para tentar novamente.")
            continue
        else:
            resultado = num_1 / num_2
    else:
        print("\nOperação inválida! Por favor, use '+', '-', '*'ou '/'.")
        input("Precione Enter para tentar novamente.")
        continue

    if resultado.is_integer():
        print(f"\nO resultado de {int(num_1)} {operacao} {int(num_2)} é: {int(resultado)}")
    else:
        print(f"\nO resultado de {num_1} {operacao} {num_2} é: {resultado:.2f}")

    resposta = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
    if resposta == 'n': 
        break

print("\nE por hoje é isso pessoal! ;)")