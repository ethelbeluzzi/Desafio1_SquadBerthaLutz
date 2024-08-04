'''
Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
● RendaatéR$1.903,98:isentodeimpostoderenda;
● RendaentreR$1.903,99eR$2.826,65:alíquotade7,5%; ● RendaentreR$2.826,66eR$3.751,05:alíquotade15%; ● RendaentreR$3.751,06eR$4.664,68:alíquotade22,5%; ● RendaacimadeR$4.664,68:alíquotamáximade27,5%.
'''

salario = float(input("Qual o seu salário em reais? "))
if salario <= 1903.98:
    print(f"Salário líquido de R$ {salario:.2f}")
elif salario <= 2826.65:
    imposto = salario * (75/1000)
    salario = salario - imposto
    print(f"Salário líquido de R$ {salario:.2f}")
elif salario <= 3751.05:
    imposto = salario * (15/100)
    salario = salario - imposto
    print(f"Salário líquido de R$ {salario:.2f}")
elif salario <= 4664.68:
    imposto = salario * (225/1000)
    salario = salario - imposto
    print(f"Salário líquido de R$ {salario:.2f}")
else:
    imposto = salario * (275/1000)
    salario = salario - imposto
    print(f"Salário líquido de R$ {salario:.2f}")
