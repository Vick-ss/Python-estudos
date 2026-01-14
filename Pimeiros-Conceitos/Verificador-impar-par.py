# Verificador Par ou Ímpar

print("=== Bem-vindo ao verificador de Par ou Ímpar! ===")

while True:
    numero = int(input("Digite um número de 1 a 1000: "))
    
    if numero % 2 == 0:
        print("Esse é um número PAR!")
    else:
        print("Esse é um número ÍMPAR!")
    
    repetir = input("Gostaria de verificar outro? (s/n): ").lower()
    if repetir != "s":
        print("Obrigado por jogar! Até mais :)")
        break