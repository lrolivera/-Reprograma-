repetir = True
while repetir:
    jogador1 = input ("Jogador 1 digite: pedra, papel ou tesoura:")
    jogador1 =str(jogador1)
    jogador2 = input ("Jogador 2 digite: pedra, papel ou tesoura:")
    jogador2 =str(jogador2)

    if (jogador1 == jogador2) :
        print("Empate!")

    elif (jogador1 == 'pedra' and jogador2 == 'papael') :
        print ("Jogador 2 ganhou!")

    elif (jogador1 == 'papel' and jogador2 == 'tesoura') :
        print("Jogador 2 ganhou!")

    elif (jogador1 == 'tesoura' and jogador2 =='pedra') :
        print("Jogador 2 ganhou!")

    elif (jogador2 == 'pedra' and jogador1 == 'papael') :
        print ("Jogador 1tesoura ganhou!")

    elif (jogador2 == 'papel' and jogador1 == 'tesoura') :
        print("Jogador 1 ganhou!")

    elif (jogador2 == 'tesoura' and jogador1 =='pedra') :
        print("Jogador 1 ganhou!")

    else: 
        print("Valor incorreto")


    resposta = input ('Deseja repetir? (s/n)')
    if resposta == 's' and 'S':
            repetir = True
    elif resposta == 'n' and 'N':
        repetir = False
    else: 
        repetir = print("Tente novamente")
    