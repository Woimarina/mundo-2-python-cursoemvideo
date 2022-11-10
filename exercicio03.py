#Exercicio 38: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior ou não existe valor maior, os dois são iguais.

print('Saiba qual valor é maior')
numA = int(input('insira um inteiro: '))
numB = int(input('insira outro inteiro: '))

if (numA>numB):
    print('{} é maior que {}!'.format(numA, numB))
elif(numB>numA):
    print('{} é maior que {}'.format(numB, numA))
else:
    print('ambos os números são iguais!')