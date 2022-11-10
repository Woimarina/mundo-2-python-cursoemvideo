#Exercício 41: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: até 9 anos - mirim, até 14 anos - infantil, até 19 anos - junior, até 20 anos - sênior, acima - master

aniversario = int(input('Em que ano o atleta nasceu? '))

if (2022-aniversario)<9:
    print('atleta da categoria mirim')
elif (2022-aniversario)<14:
    print('atleta da categoria infantil')
elif(2022-aniversario)<19:
    print('atleta da categoria sênior')
else:
     print('atleta da categoria master')
