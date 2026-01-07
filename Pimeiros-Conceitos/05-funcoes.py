
#Funções são códigos reservados , só vai ser executado quando chamarmos a função

def ola():
    print("Olá, Mundo!")

#ex para chamar essa função - ola()

ola()
ola()
ola()
ola()
ola()

#como colocar argumentos na função

def ola(nome):
    print(f"Olá, {nome}")

nome_inserido = input("Digite seu nome")

ola (nome_inserido)


#Chamou a função ola () passando como informação 


# pode colcar mais de 2 argumentos em ua função separando elas por ,

def somar(n1, n2):
    resultado = n1 + n2 
    return resultado

#sempre deve chamar a função
resultado_da_soma = somar(5, 6)
print(f"Resultado: {resultado_da_soma}")

#return >>retorne
#as variavel definidas dentro da funçã só podem ser usadas dentra da função isso ESCOPO tudo que é delcarado dentro da função só usavel dentro da função

# porém se por ex for criado uma variavel nome 

def somar(n1, n2):
    resultado = n1+n2
    return

def cumprimento(nome):
    print(f"Olá, {nome}!")

