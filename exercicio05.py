#Exercício 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando um mensagem no final de acordo com a média atingida: média abaixo de 5 - REPROVADO, média entre 5 e 6.9 - RECUPERAÇÃO, média 7 ou superior - APROVADO

nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))
media = (nota2 + nota1)/2

if(media<5):
    print('Sua média é {} você foi REPROVADO.'.format(media))
elif(media<7):
    print('Sua média é {} você está de RECUPERAÇÃO.'.format(media))
else: 
    print('Sua média é {} você foi APROVADO.'.format(media))