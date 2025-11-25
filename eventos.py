eventos = []
event= open("eventos.txt","w", encoding='utf-8')
def criar_evento(eventos):
    evento = input("\nDigite o nome do evento: ")
    return eventos.append(evento)

def list_evento(eventos):
    return print(eventos)

def edit_evento(eventos):
    print(eventos)
    pos = int(input("\nDigite a posição do evento que deseja editar: "))
    novo = input("\nDigite o nome do novo evento: ")
    eventos[pos - 1] = novo
    return eventos

def ex_evento(eventos):
    print(eventos)
    pos = int(input("\nDigite a posição do evento que deseja excluir: "))
    eventos.pop(pos - 1)
    return eventos

cont = "oi"
while(cont != "n"):

    oper = input("\nDigite qual operação será feita com os eventos\n[c - Criar evento]\
                 \n[l - Listar eventos]"\
                 "\n[e - Editar evento]" \
                 "\n[x - Excluir evento]\n\n")

    if oper == "c":
        criar_evento(eventos)
    elif oper == "l":
        list_evento(eventos)
    elif oper == "e":
        edit_evento(eventos)
    elif oper == "x":
        ex_evento(eventos)
    else:
        print("\nComando não identificado.")

    cont = input("\nDeseja continuar a operação? [s / n] ")

print(eventos)
event.write(f"Tarefas dos eventos:\n {eventos} ")
event.close()

def save_edit():
    global botao
    nome_editado = eventName.get().strip()
    data_editada = cal.get_date()

    if nome_editado:
        btn_data.config(state="normal")
        tree.item(tree.selection()[0], values=(tree.item(tree.selection()[0], 'values')[0], nome_editado, data_editada, ''))
        btn_data.config(text="Selecionar Data", command=showDate, state="disabled")
        botao.config(text="Registrar", command= registrar_nome)
        eventName.delete(0, tk.END)
        edit_btn.config(state="normal")


def edit_evento():
    if tree.selection():
        edit_btn.config(state="disabled")
        selected_item = tree.selection()[0]
        item_values = tree.item(selected_item, 'values')
        event_id = int(item_values[0])
        eventName.insert(0, tree.item(selected_item, 'values')[1])   # Preenche o campo com o nome atual
        
        botao.config(text="Salvar Edição", command = save_edit)
        btn_data.config(text="Nova Data", command = save_edit, state="disabled")
        for record in records:
            if record['id'] == event_id:
                new_name = eventName.get().strip()
                if new_name:
                    record['nome'] = new_name
                    update_event_treeview()
                break

#---Espaço de edição de funções do main---
