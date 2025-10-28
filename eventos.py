eventos = []

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
