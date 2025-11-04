# A lista principal que vai guardar os pares de itens
lista_tarefas = []
#função de add tarefas:
def adicionar_tarefa():
    print("\n--- Adicionar Par ---")
    trf = input("Digite a tarefa a ser adicionada: ")
    vlr = input("Digite custo dessa tarefa: ")
    par = (trf, vlr)

    lista_tarefas.append(par)
    
    print(f"Tarefa {par} para o evento foi adicionado com sucesso!")



#função de remover a tarefa:
def remover_tarefa():
    
    print("\n--- Remover Item ---")
    if not lista_tarefas:
        print("A lista está vazia. Nada para remover.")
        return

    item_remover = input("Digite o item que você quer remover: ")
    
    nova_lista = [par for par in lista_tarefas if item_remover not in par]
    
    if len(nova_lista) < len(lista_tarefas):

        lista_tarefas = nova_lista
        print(f"A tarefa '{item_remover}' foi removida.")
    else:
        print(f"Item '{item_remover}' não foi adicionado anteriormente.")

