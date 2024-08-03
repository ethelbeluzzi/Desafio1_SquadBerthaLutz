""" 
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
"""
#o valor recebido pelo úsuario foi armazenado como string e depois transformado em float caso o úsuario informe o valor usando ","
peso = input("Qual é o seu peso?").replace(',','.')
peso  = float(peso)

altura = input("Qual é a sua altura?").replace(',','.')
altura = float(altura)

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f"O seu IMC é {IMC:,.2f}. Você está abaixo do peso normal. Consulte um nutricionista. Cuide-se!")
elif IMC < 25.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com o peso normal. Parabéns!")
elif IMC < 30.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com excesso de peso. Cuidado, equilibre a sua dieta e faça mais atividade física.")
elif IMC < 35.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com obesidade classe I. Consulte um médico e adote hábitos saudáveis. Faça exercícios regulares e comece com uma alimentação equilibrada.")
elif IMC < 40.0:
    print(f"O seu IMC é {IMC:,.2f}. Você está com obesidade classe II. Consulte um médico e adote hábitos saudáveis. Faça exercícios regulares e comece com uma alimentação equilibrada.")
else:
    print(f"O seu IMC é {IMC:,.2f}. Você está com obesidade classe III. Atenção!!! Consulte um médico e adote hábitos saudáveis. Faça exercícios regulares e comece com uma alimentação equilibrada.")