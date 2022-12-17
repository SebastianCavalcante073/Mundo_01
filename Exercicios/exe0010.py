# Crie um programa que leia quanto de dinhero um pessoa tem na carteira e mostre
# quanto Dólares ela pode comprar
# Considerando que o valor do dolar é de 3,27

dolar = 3.27
print('=' * 42)
money = float(input('Quanto de dinheiro você tem na carteira ?\n> '))

print('=' * 50 + '\n={:>12} Valor do dolar: {}{:>15}='
                 '\n={:>12} Você tem R$ {:.2f}{:>18}='
                 '\n={:>12} Você pode comprar $ {:.4} Dolares{:>2}=\n{}'
      .format('', dolar, '', '', money, '', '', money / dolar, '', '=' * 50))
