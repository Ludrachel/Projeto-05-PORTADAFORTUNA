from random import *
#o usuário muda esta variável para terminar o jogo
jogando = True
pontos = 0

#imprime as instruções do jogo
print('''
Vinte e um !
============
Tente fazer exatamente 21 pontos !
''')
#repete o jogo enquanto a variável 'jogando' for verdadeira
while jogando:
#escolhe aleatoriamente um número entre 1 e 10
    num_aleatorio = randint(1,10)
#mostra ao jogador o número aleatorio para a soma dos pontos dele
    print("Seu próximo número é", num_aleatorio)
#faz a soma dos pontos para verificar se da 21
    pontos += num_aleatorio
#mostra ao jogador sua pontuação atual
    print("Sua pontuação agora é", pontos)
#o jogador ganha se o número aleatorio somados juntos formam 21 pontos , se não, então aparece a pontuação final dele
    if pontos == 21:
        print("Parabéns!")
        jogando = False
    elif pontos > 21:
        print("Você ultrapassou a pontuação desejada! Sua pontuação é", pontos)
        jogando = False
    else:
#pergunta ao jogador se ele quer somar mais um número a sua pontuação final
        print("Gostaria de somar mais um número ? (s/n) ")
#dependendo da resposta o jogo continua ou acaba
    resposta = input().lower()
    if resposta == "n" or resposta == "nao":
        jogando = False
print("FIM DE JOGO !")



