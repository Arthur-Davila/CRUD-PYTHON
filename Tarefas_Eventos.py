import os
os.system('cls')

lista_tarefas = [] 
eventos = [] 


def criar_evento(eventos):
    evento = input("\nDigite o nome do evento: ")
    eventos.append(evento)

def list_evento(eventos):
    if not eventos: 
        print("A lista está vazia")
        return
    print("\n--- Lista de Eventos ---")
    for i, e in enumerate(eventos):
        print(f"[{i + 1}] - {e}")

def edit_evento(eventos):
    global lista_tarefas
    list_evento(eventos)
    if not eventos: return
    try:
        pos = int(input("\nDigite a posição do evento que deseja editar: "))
        if 1 <= pos <= len(eventos):
            evento_antigo = eventos[pos - 1]
            novo = input("\nDigite o nome do novo evento: ")
            
            eventos[pos - 1] = novo
            for tarefa in lista_tarefas:
                if tarefa.get("Evento_Associado") == evento_antigo:
                    tarefa["Evento_Associado"] = novo
            print(f"Evento atualizado de '{evento_antigo}' para '{novo}'.")
        else:
            print("Posição inválida.")
    except ValueError:
        print("Entrada inválida.")

def ex_evento(eventos):
    global lista_tarefas
    list_evento(eventos)
    if not eventos: return
    try:
        pos = int(input("\nDigite a posição do evento que deseja excluir: "))
        if 1 <= pos <= len(eventos):
            evento_removido = eventos[pos - 1]
            tarefas_dependentes = [t for t in lista_tarefas if t.get("Evento_Associado") == evento_removido]
            if tarefas_dependentes:
                print(f"ATENÇÃO: O evento possui {len(tarefas_dependentes)} tarefas associadas que serão excluídas.")
                if input("Confirma a exclusão de evento e tarefas? [s/n]: ").lower() != 's':
                    return
                lista_tarefas = [t for t in lista_tarefas if t.get("Evento_Associado") != evento_removido]
            eventos.pop(pos - 1)
            print(f"Evento '{evento_removido}' excluído.")
        else:
            print("Posição inválida.")
    except ValueError:
        print("Entrada inválida.")

def add():
    if not eventos: return print("\n :Voce deve criar um evento primeiro. :")
    
    print("\n    Adicionar Tarefa    ")
    
    list_evento(eventos)
    try:
        escolha = int(input("Digite o NÚMERO do evento para associar a esta tarefa: "))
        if 1 <= escolha <= len(eventos):
            evento_selecionado = eventos[escolha - 1]
        else:
            print("Número de evento inválido. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return

    tarefa = input("Digite a tarefa: ")
    valor = input("Digite o valor da tarefa: ")
    nova_tarefa = {"Tarefa": tarefa, "Valor": valor, "Evento_Associado": evento_selecionado}
    lista_tarefas.append(nova_tarefa)
    print(f"Tarefa adicionada e associada a '{evento_selecionado}'.")

def remover():
    print("\n-Remover Tarefa")
    if not lista_tarefas:
        print("A lista está vazia, nada para remover.")
        return
    ver()
    remover_tarefa = input("Digite a TAREFA que você quer remover: ")
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
    print("\n   Lista de Tarefas  ")
    if not lista_tarefas:
        print("A lista está vazia.")
    else:
        for i in range(len(lista_tarefas)):
            print(f"Registro {i+1}:")
            print(f"  EVENTO ASSOCIADO: {lista_tarefas[i].get('Evento_Associado', 'N/A')}")
            print("  Tarefa:", lista_tarefas[i]["Tarefa"])
            print("  Valor:", lista_tarefas[i]["Valor"])

def edite():
    print("\n-Editar Tarefa")
    if not lista_tarefas:
        print("A lista está vazia. Nada para editar.")
        return
    
    ver() 
    tarefa_editar = input("Digite a tarefa que você quer editar: ")
    encontrada = False

    for i in range(len(lista_tarefas)):
        if lista_tarefas[i]["Tarefa"] == tarefa_editar:
            print("1. Editar descrição")
            print("2. Editar valor")
            print("3. Reassociar Evento")
            opcao = input("Escolha (1, 2 ou 3): ")
            
            if opcao == "1":
                nova_tar = input("Digite a nova tarefa: ")
                lista_tarefas[i]["Tarefa"] = nova_tar
                print("Tarefa atualizada.")
            elif opcao == "2":
                novo_valor = input("Digite o novo valor: ")
                lista_tarefas[i]["Valor"] = novo_valor
                print("Valor atualizado.")
            elif opcao == "3":
                list_evento(eventos)
                try:
                    escolha = int(input("Digite o NÚMERO do novo evento: "))
                    if 1 <= escolha <= len(eventos):
                        lista_tarefas[i]["Evento_Associado"] = eventos[escolha - 1]
                        print("Evento reassociado.")
                    else:
                        print("Número de evento inválido.")
                except ValueError:
                    print("Entrada inválida.")
            else:
                print("Opção inválida.")
            
            encontrada = True
            break

    if not encontrada:
        print(f"Tarefa '{tarefa_editar}' não encontrada.")

def menu_eventos():
    while True:
        oper = input("\nDigite qual operação será feita com os eventos\n[c - Criar evento]\
                     \n[l - Listar eventos]"\
                     "\n[e - Editar evento]" \
                     "\n[x - Excluir evento]" \
                     "\n[v - Voltar ao Menu Principal]\n\n")

        if oper == "c":
            criar_evento(eventos)
        elif oper == "l":
            list_evento(eventos)
        elif oper == "e":
            edit_evento(eventos)
        elif oper == "x":
            ex_evento(eventos)
        elif oper == "v":
            break  
        else:
            print("\nComando não identificado.")
        
def menu_tarefas():
    while True:
        print("\n MENU DE TAREFAS")
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Editar Tarefa")
        print("4. Remover Tarefa")
        print("5. Voltar ao Menu Principal")

        escolha = input("Digite sua escolha (1-5): ")

        if escolha == "1":
            add()
        elif escolha == "2":
            ver()
        elif escolha == "3":
            edite()
        elif escolha == "4":
            remover()
        elif escolha == "5":
            break 
        else:
            print("Opção inválida. Tente novamente.")


print("Bem-vindo ao Gerenciador Unificado!")

while True:
    print("\n MENU PRINCIPAL")
    print("1. Gerenciar Eventos") 
    print("2. Gerenciar Tarefas")
    print("3. Sair")

    principal_escolha = input("O que você deseja gerenciar? (1-3): ")

    if principal_escolha == "1":
        menu_eventos() 
    elif principal_escolha == "2":
        menu_tarefas() 
    elif principal_escolha == "3":
        print("\nSaindo... Obrigada por usar o Gerenciador Unificado!")
        break
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")
    os.system('cls')

