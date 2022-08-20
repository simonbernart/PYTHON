numero = 20
tentativas = 3
rodada = 1
print('############################################')
print('#           jodo de adivinhação            #')
print('############################################')
while(tentativas > 0):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    chute = int(input('digite um numero \n'))
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero
    if (acertou):
        print('acertou miseravi!!')
        print('fim do jogo')
        
        exit()
        
    elif (menor):
        print('ERROUUUU!!! O numero que você chutou é menor que o número secreto')
    elif (maior):
        print('ERROOUUU!!!  O numero que você chutou é maior que o número secreto!!')
    rodada = rodada + 1
    if(rodada == 4):
        print('Fim do Jogo, Você perdeu!!')
       
        exit()
    



    

    

    

