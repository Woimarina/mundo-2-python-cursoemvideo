#Exercicio 36: Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print("Simulador de financiamento\n")
salario = float(input("Qual o valor do seu salário? "))
valor = float(input("Qual o valor da casa que voce deseja comprar? "))
anos = int(input("em quantos anos deseja pagar a sua casa? "))
meses = anos*12
parcela = valor/meses

if (parcela<0.3*salario):
    print("Parabéns, seu financiamento foi aprovado com parcelas de {} por mes durante {} anos".format(parcela, anos))
else:
    print("Seu financiamento não foi aprovado. Tente novamente com um tempo de pagamento maior.")