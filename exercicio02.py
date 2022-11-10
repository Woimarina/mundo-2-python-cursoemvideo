#Exercicio 37: Escreva um programa que leia uma numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1- binário, 2 - octal, 3 - hexadecimal.

numero = int(input("escreva um inteiro decimal qualquer que deseja converter: "))
base = int(input("Escolha a base para ser convertida\n1 - binário\n2 - octal\n3 - hexadecimal\n"))

if (base == 1):
    print("O seu número convertido para binário é {}".format(bin(numero)))

elif (base == 2):
    print("O seu número convertido para octal é {}".format(oct(numero)))
elif (base == 3):
    print("O seu número convertido para hexadecimal é {}".format(hex(numero)))
else: print("base inválida!")