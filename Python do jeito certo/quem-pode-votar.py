
repetir = True
while repetir:
    idade = input ('Digite sua idade: ')
    idade = int(idade)

    if (idade >= 18 and idade <= 69):
        print(f"Como você tem {idade} anos, o voto obrigatório")

    elif (idade >= 16 and idade >= 17):
        print(f"Como você tem {idade} anos, o voto facultativo")

    elif (idade >= 70):
        print(f"Como você tem {idade} anos, o voto facultativo")

    else :
        print(f"Como você tem {idade} anos, não pode votar")

    resposta = input ('Deseja repetir? (s/n)')
    if resposta == 's' and 'S':
        repetir = True
    elif resposta == 'n' and 'N':
        repetir = False
    else: 
        repetir = print("Tente novamente")


