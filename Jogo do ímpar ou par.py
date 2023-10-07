import random

print("*Jogo do par ou Impar*")


def jogo_par_ou_impar():
    escolha_usuario = input("Escolha 'par' ou 'ímpar': ").lower()

    if escolha_usuario not in ['par', 'ímpar']:
        print("Escolha inválida. Por favor, escolha 'par' ou 'ímpar'.")
        return

    numero_usuario = int(input("Digite um número qualquer: "))

    numero_computador = random.randint(1, 10)  # Computador escolhe um número aleatório entre 1 e 100
    resultado = numero_usuario + numero_computador

    print(f"O computador escolheu o número {numero_computador}.")
    print(f"A soma dos números é {resultado}.")

    if (resultado % 2 == 0 and escolha_usuario == 'par') or (resultado % 2 != 0 and escolha_usuario == 'ímpar'):
        print("Você ganhou!")
    else:
        print("Você perdeu!")


jogo_par_ou_impar()