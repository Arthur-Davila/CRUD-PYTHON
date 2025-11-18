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

def ver():
    print("\n--- Lista de Tarefas ---")
    if not lista_tarefas:
        print("A lista está vazia.")
    else:
        for i in range(len(lista_tarefas)):
            print(f"Registro {i+1}:")
            print("  Tarefa:", lista_tarefas[i]["Tarefa"])
            print("  Valor:", lista_tarefas[i]["Valor"])
            print("-----")


def edite():
    print("\n-Editar Tarefa")
    if not lista_tarefas:
        print("A lista está vazia. Nada para editar.")
        return
    
    tarefa_editar = input("Digite a tarefa que você quer editar: ")
    encontrada = False

    for i in range(len(lista_tarefas)):
        if lista_tarefas[i]["Tarefa"] == tarefa_editar:
            print("1. Editar descrição")
            print("2. Editar valor")
            opcao = input("Escolha (1 ou 2): ")
            
            if opcao == "1":
                nova_tar = input("Digite a nova tarefa: ")
                lista_tarefas[i]["Tarefa"] = nova_tar
                print("Tarefa atualizada.")
            elif opcao == "2":
                novo_valor = input("Digite o novo valor: ")
                lista_tarefas[i]["Valor"] = novo_valor
                print("Valor atualizado.")
            else:
                print("Opção inválida.")
            
            encontrada = True
            break

    if not encontrada:
        print(f"Tarefa '{tarefa_editar}' não encontrada.")
