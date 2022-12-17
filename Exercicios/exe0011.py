# Faça um programa que leia a altura e largura de uma parede em metros e calcule a sua area
# E a quantidade de tinta necessaria para pintá-la sabendo que a cada litro de tinta pinta uma area de 2m²

opcao = -1  # Variavel de controle de fluxo
while opcao != 0:
    print('{}\n{}{:>8}SISTEMA GERENCIADOR DE TINTAS POR M²{:>5}\n{}'.format('=' * 50, '=', '', '=', '=' * 50))
    opcao = int(input('[1] - Calcular Tinta\n[0] - Sair\n > '))
    if opcao == 1:
        print('{}\n={:>10}CALCULANDO QUANTIDADE DE TINTA{:>8}=\n{}'.format('=' * 50, '', '', '-' * 50))
        print('={:>5}Entre com a largura e altura da parede: {:>3}=\n{}'.format('', '', '=' * 50))
        width = float(input('= Digite a largura: '))
        higth = float(input('= Digite a altura: '))
        # litros = float(input('Litros lata de tinta: '))

        # Calculo da area da parede
        area = width * higth
        # Calculo da quantidade de tinta necessaria

        tinta = area / 2

        print('=' * 50 +
              '\n={:>16}DADOS CALCULADOS{:>16}=\n{}'
              '\n= Largura: {:>30}{}{:>6}'
              '\n= Altura: {:>31}{}{:>6}'
              '\n= Area total: {:>27}{:.4} m²{:>3}'
              '\n= Quantidade em litros necessario {:>3}{:.2} litros{:>3} \n{}\n\n'
              .format('', '', '-' * 50, '', width, '=', '', higth, '=', '', area, '=', '', tinta, '=', '=' * 50))
        opcao = int(input('Deseja calcular novamente ? 1/S ou 0/N '))
        if opcao == 1:
            continue
        else:
            break
    else:
        print('Sistema Encerrado!')
        break
