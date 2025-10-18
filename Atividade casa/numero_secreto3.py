print ('\nJogo: Número Secreto!')

print ('\nTente adivinhar o número entre 10 e 100:')

import random
numSecreto = random.randint(10,100)

print(' ')

pontos = 100

dificuldade = input('Escolha a dificuldade( 1 - Fácil / 2 - Médio / 3 - Dificil ): ')

if dificuldade == '1':

    tentativas = 30  

    print(f'\nTentativas: {tentativas} / Pontos atuais: {pontos} ( -10 Pontos cada erro )')

    while True:

            numDigitado = int(input('\nDigite um número: '))

            if numDigitado < 10 or numDigitado> 100:
                print('Digite um número entre 10 e 100.')
                continue
                        
            if numDigitado == numSecreto:
                    print('Parabéns, você acertou! Fim de jogo :)')
                    print(' ')
                    break

            elif numDigitado > numSecreto:
                    tentativas -= 1
                    pontos -= 10
                    print('Errou, o número secreto é menor que o digitado. -10 pontos')
                    print(f'\nLhe resta {tentativas} tentativas, Pontos atuais: {pontos}')

                    if tentativas == 0:
                        print(f'\nSuas tentativas acabaram! Fim de jogo, o número era {numSecreto} :(')
                        print(' ')
                        break
                        
                    elif pontos == 0:
                        print(f'\nSeus pontos acabaram! Fim de jogo, o número era {numSecreto} :(')
                        print(' ')
                        break

            else:
                
                tentativas -= 1
                pontos -= 10
                print('Errou! O número secreto é maior que o digitado. -10 pontos')
                print(f'\nLhe resta {tentativas} tentativas, Pontos atuais: {pontos}')

                if tentativas == 0:
                    print(f'\nSuas tentativas acabaram! Fim de jogo, o número era {numSecreto} :(')
                    print(' ')
                    break
                
                elif pontos == 0:
                    print(f'\nSeus pontos acabaram! Fim de jogo, o número era {numSecreto} :(')
                    print(' ')
                    break 
                  
elif dificuldade == '2':

    tentativas = 15 
            
    print(f'\nTentativas: {tentativas} / Pontos atuais: {pontos} ( -20 Pontos cada erro )')

    while True:

            numDigitado = int(input('\nDigite um número: '))

            if numDigitado < 10 or numDigitado> 100:
                print('Digite um número entre 10 e 100.')
                continue

            if numDigitado == numSecreto:
                    print('Parabéns, você acertou! Fim de jogo :)')
                    print(' ')
                    break

            elif numDigitado > numSecreto:
                    tentativas -= 1
                    pontos -= 20
                    print('Errou, o número secreto é menor que o digitado. -20 pontos')
                    print(f'\nLhe resta {tentativas} tentativas, Pontos atuais: {pontos}')

                    if tentativas == 0:
                        print(f'\nSuas tentativas acabaram! Fim de jogo, o número era {numSecreto} :(')
                        print(' ')
                        break
                        
                    elif pontos == 0:
                        print(f'\nSeus pontos acabaram! Fim de jogo, o número era {numSecreto} :(')
                        print(' ')
                        break

            elif numDigitado <= 10:
                  print('Digite um número entre 10 e 100.')
            
            elif numDigitado >=100:
                  print('Digite um número entre 10 e 100.')
    
            else:
                
                tentativas -= 1
                pontos -= 20
                print('Errou! O número secreto é maior que o digitado. -20 pontos')
                print(f'\nLhe resta {tentativas} tentativas, Pontos atuais: {pontos}')

                if tentativas == 0:
                    print(f'\nSuas tentativas acabaram! Fim de jogo, o número era {numSecreto} :(')
                    print(' ')
                    break
                
                elif pontos == 0:
                    print(f'\nSeus pontos acabaram! Fim de jogo, o número era {numSecreto} :(')
                    print(' ')
                    break

elif dificuldade == '3':

    tentativas = 5
            
    print(f'\nTentativas: {tentativas} / Pontos atuais: {pontos} ( -50 Pontos cada erro )')

    while True:

            numDigitado = int(input('\nDigite um número: '))

            if numDigitado < 10 or numDigitado> 100:
                print('Digite um número entre 10 e 100.')
                continue

            if numDigitado == numSecreto:
                    print('\nParabéns, você acertou!  Fim de jogo :)')
                    print(' ')
                    break

            elif numDigitado > numSecreto:
                    tentativas -= 1
                    pontos -= 50
                    print('Errou, o número secreto é menor que o digitado. -50 pontos')
                    print(f'\nLhe resta {tentativas} tentativas, Pontos atuais: {pontos}')
                
                    if tentativas == 0:
                        print(f'\nSuas tentativas acabaram! Fim de jogo, o número era {numSecreto} :(')
                        print(' ')
                        break
                    
                    elif pontos == 0:
                        print(f'\nSeus pontos acabaram! Fim de jogo, o número era {numSecreto} :(')
                        print(' ')
                        break
            
            elif numDigitado <= 10:
                  print('Digite um número entre 10 e 100.')
            
            elif numDigitado >=100:
                  print('Digite um número entre 10 e 100.')
            
            else:
                
                tentativas -= 1
                pontos -= 50
                print('Errou! O número secreto é maior que o digitado. -50 pontos')
                print(f'\nLhe resta {tentativas} tentativas, Pontos atuais: {pontos}')

                if tentativas == 0:
                    print(f'\nSuas tentativas acabaram! Fim de jogo, o número era {numSecreto} :(')
                    print(' ')
                    break
                    
                elif pontos == 0:
                    print(f'\nSeus pontos acabaram! Fim de jogo, o número era {numSecreto} :(')
                    print(' ')
                    break
else:
          print('Erro, digite uma dificuldade válida.')

    