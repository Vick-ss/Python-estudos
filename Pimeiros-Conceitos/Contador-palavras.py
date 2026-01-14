# Contador de Palavras

print("=== Contador de Palavras ===")
frase = input("Informe em uma frase algo em que você pensou hoje:\n")

palavras = frase.split()
quantidade = len(palavras)

print(f"Legal! Você acabou de me dizer no que pensou usando {quantidade} palavras!")