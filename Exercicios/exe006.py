#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
import math

x = int(input('Digite um número: '))

print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}'.format(x, x * 2, x, x * 3, x, math.sqrt(x)))

