
# códigos q ficam se repetindo (while-for)

# while -enquantoa  condição for vdd

# for dependem de alguma estrutura de dados

contador = 10
while contador >= 1:
    print(f"Contagem atual: {contador}")
    contador -= 1

# while (enquanto) contador maior ou igual a 1 vai printar contagem na tela e subtrair -1 e quando bater 0 sai do loop


senha = "watashi"
tentativa_senha = ""
while senha != tentativa_senha:
    tentativa_senha = input("Digite sua senha: ")
    if tentativa_senha != senha:
        print("Senha incorreta!tente novamente")
    else:
        print("Acertou!")

# enquanto a senha for != diferente da tentativa senha vai mostrar ao usuário senha incorreta


# inicializa 2 variaveis senha e tentatia senha,enquanto as senhas forem diferentes vai printar ao usuário senha errada tente novamente

# for
# for depende de outra estrutura para funcionar no caso para cada item da lista de compras , faça isso aqui

compras = ["Arroz", "Feijão", "Leite", "Pão"]
for item in compras:
    print(f"Você precisa comprar: {item}")


# Para cada numero em numeros exiba numeros

numeros = [5, 6, 2, 9, 8, 8, 2, 1, 5, 6]
for numero in numeros:
    if numero % 2 == 0:
        break
    print(numero)

# beak (quebra o loop) caso o resto da dividsão por 2 (for par)ele vai dar um break

# continue >>ir para proxima execução

numeros = [5, 6, 2, 9, 8, 8, 2, 1, 5, 6]
for numero in numeros:
    if numero % 2 == 0:
        continue

print(numero)
