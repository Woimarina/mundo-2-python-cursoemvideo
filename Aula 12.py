nome = str(input('Qual é o seu nome? '))
nome = nome.lower()
if nome == 'marina':
    print('Belo nome!')
elif nome == 'alyne':
    print('oh, hi!!!! The love of my life is here <3')
else:
    print('sai daqui mané... ninguém te chamou')
print('Tenha um bom dia, {} '.format(nome.capitalize()))
