#Faça um algoritomo que leia o salario de um funcionario e mostre seu novo  salario com 15% de aumento

salario = float(input('{}\nDigite seu salario atual: \nR$ '.format('=' * 50)))

print('{}\nSalario atual: R$ {:.2f}\n'
      '{}\nSalario com 15% de aumento R$ {:.2f}\n'
      '{}\n'.format('=' * 50, salario, '=' * 50, (salario + (salario * 15) / 100), '=' * 50))

