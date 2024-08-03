# 3. Faça um Programa que peça a quantidade de quilômetros, transforme
# em metros, centímetros e milímetros.

quilometros = float(input("Digite os quilômetros para conversão: "))


conversao_metros = quilometros * 1000
conversao_centimetros = quilometros * 100_000
conversao_milimetros = quilometros * 1_000_000


output = (
    f"{quilometros:.2f} quilômetros é equivalente a:\n"
    f"{conversao_metros:.2f} metros\n"
    f"{conversao_centimetros:.2f} centímetros\n"
    f"{conversao_milimetros:.2f} milímetros"
)

print(output)
