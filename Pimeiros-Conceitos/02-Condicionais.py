
#condicionais se(if) senão(else)

idade = int(input("Qual é a sua idade?"))
if idade >= 18:
    print("Tá liberado!")
else:
    print("Pode não!")


# >= maior ou igual -- <= menor ou igual
#Operadores de comparação > <

print(5 > 2)

#dados booleanos-- verifica se um dado é vdd ou não  ex:5>2 true

senha = "Chave01"
tentativa_senha = input ("Digite sua senha: ")
if senha == tentativa_senha:
    print("Acesso liberado!")
else:
   print ("Errou, tente noamente.")

# atribuir uma variavel a outra =  //  para comparar se uma coisa é igual a oura ==  // != verificar se alguma coisa é diferente da outra

#ex != se a senha for diferentee da tentativa vai printar errou senão Acertou

# != verificar se uma coisa é diferente da outra

senha = "Chave01"
tentativa_senha = input ("Digite sua senha: ")
if senha != tentativa_senha:
    print("Errou!")
else:
   print ("Acertou!.")


# elif = caso contrario
nota = float (input("Digite seu nota "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

    