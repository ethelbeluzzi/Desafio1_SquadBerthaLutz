import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


litros = float(input('Informe a quantidade de litros consumidos: '))
distancia = float(input('Informe a distância percorrida em Km: '))
    
#Calcula o cosumo médio de litros por distância percorrida:
consumo = distancia / litros

#Exibe o resultado:
print(f'O consumo médio é de: {Fore.MAGENTA}{consumo:.2f}{Style.RESET_ALL} Km/L')

