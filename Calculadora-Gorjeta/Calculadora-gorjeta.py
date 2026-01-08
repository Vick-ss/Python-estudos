print("=== Calculadora de Gorjeta ===")
conta = float(input("Qual o valor total da conta? R$ "))

opcoes = [18, 20, 25]

for porcentagem in opcoes:
    gorjeta = conta * (porcentagem / 100)
    total = conta + gorjeta
    print(f"{porcentagem}% de gorjeta equivale a R$ {gorjeta:.2f}; "
          f"total a pagar: R$ {total:.2f}")