from random import *

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

pontos = 0
for attempt in range(5):
    print("\nEscolha uma porta (1,2 ou 3):")
    
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1,3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        pontos += 1
        print("Parabéns!")
    else:
        print("Que peninha!")
print("Sua pontuação foi",pontos)
