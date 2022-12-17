#Desafio 4 faça um programa que leia algo digitado pelo usuario e seja impreso os tipos primitivos

x = input("Digite algo: ")
print("O tipo primitivo é  {}".format(type(x)))
print("É um numero ?  {} ".format(x.isnumeric()))
print("É uma String ?  {} ".format(x.isalpha()))
print("É alfanumerico ? [ {} ".format(x.isalnum()))
print("Está em maiuscula ?  {}".format(x.isupper()))
print("Está em minuscula ?  {}".format(x.islower()))
print("Só tem espaços  ?  {} ".format(x.isspace()))
print("É um numero decimal ?  {}  ".format(x.isdecimal()))
print("Pode ser imprimido na tela ?  {}".format(x.isprintable()))
print("É um digito ? {}".format(x.isdigit()))
print("É tem caracter da tabela ansil  ?  {}".format(x.isascii()))
print("É um identificado de variavel permitido ?  {}".format(x.isidentifier()))
print("Esta capitalizada ?  {} ".format(x.istitle()))




