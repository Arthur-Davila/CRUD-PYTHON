lista_tarefas = []

def add():
    print("\n--- Adicionar Tarefa ---")
    tarefa = input("Digite a tarefa: ")
    valor = input("Digite o valor da tarefa: ")
    nova_tarefa = {"Tarefa": tarefa, "Valor": valor}
    lista_tarefas.append(nova_tarefa)


def remover():
    print("\n-Remover Tarefa")
    if not lista_tarefas:
        print("A lista está vazia, nada para remover.")
        return
    
    remover_tarefa = input("Digite a tarefa que você quer remover: ")
    encontrada = False

    for i in range(len(lista_tarefas)):
        if lista_tarefas[i]["Tarefa"] == remover_tarefa:
            del lista_tarefas[i]
            print(f"Tarefa '{remover_tarefa}' foi removida.")
            encontrada = True
            break
    
    if not encontrada:
        print(f"Tarefa '{remover_tarefa}' não encontrada.")
