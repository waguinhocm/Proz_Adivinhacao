
alvo = 25
chances = 5
acertou = False

while chances > 0 and not acertou:
    try:
        chute = int(input("Digite um número inteiro entre 0 e 100 - "))
        chances-=1

        if chute == alvo:
            print("Parabéns! Adivinhou o número!")
            acetou = True
        else:
            if chute > alvo:
                print("Não acertou!O número é menor que o seu palpite")
            else:
                print("Não acertoumas. O número é maior que o seu palpite")
            

    except:
        print("Tente Novamente!")

if not acertou:
    print("Que pena, o número era - ", + alvo)

