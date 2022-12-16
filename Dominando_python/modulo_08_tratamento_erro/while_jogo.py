# jogo da adivinhação
from random import randint
import os

os.system('cls')

print('**************************************')
print('Seja bem vindo ao jogo de adivinhação!')
print('**************************************')

# o \n é um caracter de escape, utilizado para quebra de linha
print('\n')

numero_secreto = randint(1, 5)
numero_escolhido = 0

while True:
    try:
        numero_escolhido = int(input('Escolha um número de 1 a 5: '))
    except:
        print('Você escolheu um número inválido!')
    else:
        if numero_escolhido not in range(1,6):
            print('Número precisa estar entre 1 e 5!')
            continue
        elif numero_escolhido == numero_secreto:
            print(f'Parabéns! Você acertou o número secreto: {numero_secreto}!')
            break
        else:
            print('Você errou!')  