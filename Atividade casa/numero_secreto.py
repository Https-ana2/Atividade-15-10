print ('\nJogo: Número Secreto!')

while True:
    tentativa = int(input('\nDigite um número: '))

    if tentativa == 12:
        print('Parabéns, você acertou!')
        break

    elif tentativa > 12:
        print('Errou, o número é menor que o digitado.')

    else:
        print('Errou! O número é maior que o digitado.')