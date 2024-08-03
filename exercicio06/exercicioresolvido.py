#recebe a entrada do usuário em km
distancia = float(input("Digite a distância da viagem em km: "))

#divide a distância pelo tempo
tempo_aviao = distancia / 600

#separa a parte inteira da decimal
horas_aviao = int(tempo_aviao)
minutos_aviao = (tempo_aviao - horas_aviao) * 60

#repete para os outros modais
tempo_carro = distancia / 100
horas_carro = int(tempo_carro)
minutos_carro = (tempo_carro - horas_carro) * 60

tempo_onibus = distancia / 80
horas_onibus = int(tempo_onibus)
minutos_onibus = (tempo_onibus - horas_onibus) * 60

#devolve de uma forma mais palatável
print(
    f"Tempo de viagem de avião: {horas_aviao}h e {minutos_aviao:.0f}m\n"
    f"Tempo de viagem de carro: {horas_carro}h e {minutos_carro:.0f}m\n"
    f"Tempo de viagem de ônibus: {horas_onibus}h e {minutos_onibus:.0f}m"
    )
