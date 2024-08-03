exercicio_hora = float(input("Quantas horas de exercicio voce faz por semana ? "))

caloria_minut = 5 # esse e o numero pre defenido de calorias por minuto

minuto_semana = exercicio_hora *60 # considerando que e em minut tenho que converter o valor da exercicio_hora

caloria_semana = minuto_semana* caloria_minut # agr e o calculo ja feito a conversao vezes o vcalor da caloria

caloria_mes = caloria_semana * 4 # valor total do mes com a variavel da caloria_semana vezes 4 pq o mes 4 semana


print(f'As calorias queimadas em um mes sao de {caloria_mes:.2f}')
