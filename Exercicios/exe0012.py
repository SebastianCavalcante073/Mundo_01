#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('{}\nDigite o preço do produto: \n> '.format('=' * 50)))

print('{}\nPreço do produto: R$ {}\n{}'
      '\nPreço do produto com 5% de desconto: R$ {}\n{}'
      ''.format('=' * 50, produto, '=' * 50, (produto + (produto * 5) / 100), '=' * 50))
