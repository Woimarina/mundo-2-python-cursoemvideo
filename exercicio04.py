#Exercício 39: Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade: -Se ele ainda vai se alistar ao serviço militar; -Se é hora de se alistar; - Se ja passou do tempo de alistamento. Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

aniversario = int(input('em que ano voce nasceu? '))

if((2022-aniversario)>=18):
    print('já passou da hora de se alistar!')
elif((2022-aniversario)>16):
    print('voce ja pode se alistar!')
else: 
    print('Voce ainda não pode se alistar!')