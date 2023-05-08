from random import *
jogando = True
score = 0

print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma dessas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

      __________     __________     __________

     |          |   |          |   |          |
     |          |   |          |   |          |
     |          |   |          |   |          |
     |   [1] o  |   |   [2]  o |   |   [3]  o |
     |          |   |          |   |          |
     |          |   |          |   |          |
     |          |   |          |   |          |
      __________     ___________    ___________
''')

while jogando == True:
    print("\nEscolha uma porta (1,2 ou 3):")
    
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1,3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score += 1
    if portaEscolhida != portaCerta:
        print("Que peninha!")
        score = 0
        
    print("Sua pontuação foi",score)
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input().lower()
    if resposta == "n" or resposta == "nao":
        jogando = False
print("Obrigado por jogar.")
print("Sua pontuação final foi", score)


