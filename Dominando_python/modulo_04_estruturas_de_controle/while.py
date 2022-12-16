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

while numero_secreto != int(numero_escolhido):
    numero_escolhido = input('Escolha um número de 1 a 5: ')
    
print(f'Parabéns! Você descobriu que o número secreto era o {numero_secreto}!')