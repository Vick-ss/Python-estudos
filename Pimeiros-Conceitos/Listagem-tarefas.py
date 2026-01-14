print ("Projeto de tarefas")

tarefas = []

while True:
    acao = input("Adicionar, listar ou sair? ")
    if acao == "adicionar":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
    elif acao == "listar":
        print("Suas tarefas:", tarefas)
    elif acao == "sair":
        break