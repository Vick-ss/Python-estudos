
# Coleções são variaveis que guardam mais de um valor
#Estruturas de dados que permitem que possamos inserir mais de um valor em uma variavel 

# listas
#variavel fruta recebe uma lista 

frutas = ["Banana","Maça","Uva"]
frutas[1] = "Abacaxi"
frutas.append("Morango")
frutas.insert(0, "Kiwi")
frutas.remove("Abacaxi")

if "Uva" in frutas:
    print ("Tem Uva nas frutas")

print(frutas)


#Substituição de Maça por Abacaaxi e, frutas [1]= Abacaxi


# . append  >>Para adicionar 
# insert >>Para inserir 
# .remove >>Para remover


#Tuplas () -->Não podem ser mudadas

cores = ("Vermelho", "verde", "azul")
print(cores)


minhas_Tuplas = [("Maçã", "Banana"), ("Verde", "Vermelho")]
print(minhas_Tuplas[1][0])

# contagem sempre se incia no 0 ent vai pagar cores e apos 1 vai pegar o verde 

#Dicionários > Chave q vai ser como vamos nomear algo, valor q iremos gaurdar na chave

#chave nome com valor vick e chave idade com valor 22

dados = {"nome" :"Vick", "idade":22}
print(dados["nome"])

#Para alterar

dados = {"nome": "Vick-San" , "idade":23}
dados["idade"] = 23
print(dados)

