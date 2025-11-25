import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

BG = "#F7F7FC"
CARD = "white"
ACC = "#6C5CE7"
DEL = "#FF6B6B"

eventos = []
prox_id = 1

def salvar_arquivo():
    with open("eventos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("--- Eventos, Datas e Tarefas ---\n")
        for evento in eventos:
            arquivo.write(f"{evento['nome']} ({evento['data']}) ({evento['tipo']}) - Orçamento: R$ {evento['orcamento']:.2f}\n")
            for tarefa in evento['tarefas']:
                arquivo.write(f"   Tarefa: {tarefa['nome']} - Valor: R$ {tarefa['valor']:.2f}\n")
            dias_restantes = (datetime.strptime(evento["data"], "%d/%m/%Y") - datetime.now()).days
            if dias_restantes < 0:
                arquivo.write("   Evento já ocorreu.\n")
            elif dias_restantes == 0:
                arquivo.write("   Evento acontece hoje!\n")
            else:
                arquivo.write(f"   Faltam {dias_restantes} dias.\n")
            arquivo.write("\n")

def checar_easter_egg():
    if len(eventos) == 10:
        janela_egg = tk.Toplevel()
        janela_egg.title("🎉 Easter Egg 🎉")
        janela_egg.geometry("1000x800")
        janela_egg.configure(bg="white")
        tk.Label(janela_egg, text="\n\n\n🎂 Parabéns, este é o décimo evento! 🎂", bg=BG, font=("Arial", 14)).pack(pady=10)
        mensagem = """
                              ██████                              
              ████████      ██                            
            ██░░░░██        ██████                        
          ██░░░░██        ██████████                      
        ██░░░░░░██      ██████████████                    
    ████░░░░░░████      ██████████████                    
  ██░░░░░░░░██████      ██████████████████                
  ██░░░░░░████████        ████████████████████            
  ██░░░░██████████          ████████████████████████      
██░░░░██████████████      ██████████████████████████████  
██░░░░████████████████████████████████████████████████████
██░░░░████████████████████████████████████████████████████
  ██░░████████████████████████████████████████████████████
  ██░░░░██████░░░░██████░░░░██████░░░░██████░░░░██████░░██
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
    ██░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░██
    ██░░░░░░░░░░██  ████░░░░░░░░░░░░░░██  ████░░░░░░░░░░██
    ██░░░░░░░░░░████████░░░░██░░██░░░░████████░░░░░░░░░░██
      ██░░░░░░░░░░████░░░░░░░░██░░░░░░░░████░░░░░░░░░░░░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
          ████████████████████████████████████████████████
        """
        tk.Label(janela_egg, text=mensagem, font=("Courier", 12), bg="white", justify="center").pack(expand=True)

def atualizar_eventos():
    tabela_eventos.delete(*tabela_eventos.get_children())
    for evento in eventos:
        dias_restantes = (datetime.strptime(evento["data"], "%d/%m/%Y") - datetime.now()).days
        tabela_eventos.insert("", tk.END, values=(
            evento["id"], evento["nome"], evento["tipo"], 
            evento["data"], evento["local"], f"{evento['orcamento']:.2f}", dias_restantes
        ))
    atualizar_combo_eventos()
    atualizar_tarefas()
    salvar_arquivo()
    checar_easter_egg()

def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    tipo_var.set("")
    entrada_local.delete(0, tk.END)
    entrada_orcamento.delete(0, tk.END)

def obter_evento_selecionado():
    selecao = tabela_eventos.selection()
    if not selecao: return None
    id_evento = int(tabela_eventos.item(selecao[0])["values"][0])
    for evento in eventos:
        if evento["id"] == id_evento:
            return evento

def adicionar_evento():
    global prox_id
    nome = entrada_nome.get().strip()
    tipo = tipo_var.get().strip()
    data = calendario.get_date()
    local = entrada_local.get().strip()
    try:
        orcamento = float(entrada_orcamento.get().strip())
    except:
        return
    
    if not nome or not tipo or not local:
        return
        
    eventos.append({
        "id": prox_id, "nome": nome, "tipo": tipo, 
        "data": data, "local": local, "orcamento": orcamento, "tarefas": []
    })
    prox_id += 1
    limpar_formulario()
    atualizar_eventos()

def excluir_evento():
    evento = obter_evento_selecionado()
    if evento:
        eventos.remove(evento)
        atualizar_eventos()

def editar_evento():
    evento = obter_evento_selecionado()
    if evento:
        entrada_nome.delete(0, tk.END)
        entrada_nome.insert(0, evento["nome"])
        tipo_var.set(evento["tipo"])
        calendario.selection_set(evento["data"])
        entrada_local.delete(0, tk.END)
        entrada_local.insert(0, evento["local"])
        entrada_orcamento.delete(0, tk.END)
        entrada_orcamento.insert(0, str(evento["orcamento"]))
        btn_adicionar_evento.config(text="Salvar", command=lambda: salvar_edicao(evento))

def salvar_edicao(evento):
    evento["nome"] = entrada_nome.get().strip()
    evento["tipo"] = tipo_var.get().strip()
    evento["data"] = calendario.get_date()
    evento["local"] = entrada_local.get().strip()
    try:
        evento["orcamento"] = float(entrada_orcamento.get().strip())
    except:
        return
    limpar_formulario()
    btn_adicionar_evento.config(text="Adicionar Evento", command=adicionar_evento)
    atualizar_eventos()

def atualizar_combo_eventos():
    combo_eventos['values'] = [f"{evento['id']}-{evento['nome']}" for evento in eventos]
    if combo_eventos.get() not in combo_eventos['values']:
        combo_eventos.set("")

def atualizar_tarefas():
    tabela_tarefas.delete(*tabela_tarefas.get_children())
    selecao = combo_eventos.get()
    if selecao:
        id_evento = int(selecao.split("-")[0])
        evento = next((x for x in eventos if x["id"]==id_evento), None)
        if evento:
            orcamento_disponivel = evento["orcamento"] - sum(t["valor"] for t in evento["tarefas"])
            label_orcamento.config(text=f"Orçamento disponível: R$ {orcamento_disponivel:.2f}")
            for tarefa in evento["tarefas"]:
                tabela_tarefas.insert("", tk.END, values=(tarefa["nome"], f"{tarefa['valor']:.2f}"))

def adicionar_tarefa():
    selecao = combo_eventos.get()
    if not selecao: return
    id_evento = int(selecao.split("-")[0])
    evento = next((x for x in eventos if x["id"]==id_evento), None)
    if evento:
        nome = entrada_tarefa.get().strip()
        try:
            valor = float(entrada_valor_tarefa.get().strip())
        except:
            return
        orcamento_disponivel = evento["orcamento"] - sum(t["valor"] for t in evento["tarefas"])
        if valor > orcamento_disponivel: return
        evento["tarefas"].append({"nome": nome, "valor": valor})
        entrada_tarefa.delete(0, tk.END)
        entrada_valor_tarefa.delete(0, tk.END)
        atualizar_tarefas()
        atualizar_eventos()

def excluir_tarefa():
    selecao_evento = combo_eventos.get()
    selecao_tarefa = tabela_tarefas.selection()
    if not selecao_evento or not selecao_tarefa: return
    id_evento = int(selecao_evento.split("-")[0])
    evento = next((x for x in eventos if x["id"]==id_evento), None)
    if evento:
        nome_tarefa = tabela_tarefas.item(selecao_tarefa[0])["values"][0]
        tarefa = next((x for x in evento["tarefas"] if x["nome"]==nome_tarefa), None)
        if tarefa:
            evento["tarefas"].remove(tarefa)
            atualizar_tarefas()
            atualizar_eventos()

def editar_tarefa():
    selecao_evento = combo_eventos.get()
    selecao_tarefa = tabela_tarefas.selection()
    if not selecao_evento or not selecao_tarefa: return
    id_evento = int(selecao_evento.split("-")[0])
    evento = next((x for x in eventos if x["id"]==id_evento), None)
    if evento:
        nome_tarefa = tabela_tarefas.item(selecao_tarefa[0])["values"][0]
        tarefa = next((x for x in evento["tarefas"] if x["nome"]==nome_tarefa), None)
        if tarefa:
            entrada_tarefa.delete(0, tk.END)
            entrada_tarefa.insert(0, tarefa["nome"])
            entrada_valor_tarefa.delete(0, tk.END)
            entrada_valor_tarefa.insert(0, str(tarefa["valor"]))
            btn_adicionar_tarefa.config(text="Salvar", command=lambda: salvar_tarefa(tarefa, evento))

def salvar_tarefa(tarefa, evento):
    tarefa["nome"] = entrada_tarefa.get().strip()
    try:
        tarefa["valor"] = float(entrada_valor_tarefa.get().strip())
    except:
        return
    entrada_tarefa.delete(0, tk.END)
    entrada_valor_tarefa.delete(0, tk.END)
    btn_adicionar_tarefa.config(text="Adicionar Tarefa", command=adicionar_tarefa)
    atualizar_tarefas()
    atualizar_eventos()

janela = tk.Tk()
janela.title("Agenda Simples")
janela.geometry("950x500")
janela.configure(bg=BG)

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)

aba_eventos = tk.Frame(abas, bg=BG)
abas.add(aba_eventos, text="Eventos")

frame_formulario = tk.Frame(aba_eventos, bg=CARD, padx=10, pady=10)
frame_formulario.pack(side="left", fill="y")

tk.Label(frame_formulario, text="Nome:", bg=CARD).pack(anchor="w")
entrada_nome = tk.Entry(frame_formulario)
entrada_nome.pack(fill="x", pady=2)

tk.Label(frame_formulario, text="Tipo:", bg=CARD).pack(anchor="w")
tipo_var = tk.StringVar()
combo_tipo = ttk.Combobox(frame_formulario, textvariable=tipo_var, values=["Aniversário","Casamento","Reunião"])
combo_tipo.pack(fill="x", pady=2)

tk.Label(frame_formulario, text="Data:", bg=CARD).pack(anchor="w")
calendario = Calendar(frame_formulario, date_pattern="dd/mm/yyyy")
calendario.pack(pady=2)

tk.Label(frame_formulario, text="Local:", bg=CARD).pack(anchor="w")
entrada_local = tk.Entry(frame_formulario)
entrada_local.pack(fill="x", pady=2)

tk.Label(frame_formulario, text="Orçamento:", bg=CARD).pack(anchor="w")
entrada_orcamento = tk.Entry(frame_formulario)
entrada_orcamento.pack(fill="x", pady=2)

frame_botoes = tk.Frame(aba_eventos, bg=CARD)
frame_botoes.pack(side="left", fill="y", padx=5, pady=10)

btn_adicionar_evento = tk.Button(frame_botoes, text="Adicionar Evento", bg=ACC, fg="white", command=adicionar_evento)
btn_adicionar_evento.pack(fill="x", pady=2)
tk.Button(frame_botoes, text="Editar Selecionado", bg=ACC, fg="white", command=editar_evento).pack(fill="x", pady=2)
tk.Button(frame_botoes, text="Excluir Selecionado", bg=DEL, fg="white", command=excluir_evento).pack(fill="x", pady=2)

tabela_eventos = ttk.Treeview(aba_eventos, columns=("id","nome","tipo","data","local","orcamento","dias"), show="headings")
colunas = ["id","nome","tipo","data","local","orcamento","dias"]
titulos = ["ID","Nome","Tipo","Data","Local","Orc","Dias"]
for col, tit in zip(colunas, titulos):
    tabela_eventos.heading(col, text=tit)
tabela_eventos.column("id", width=50, anchor="center")
tabela_eventos.column("nome", width=150, anchor="w")
tabela_eventos.column("tipo", width=100, anchor="center")
tabela_eventos.column("data", width=100, anchor="center")
tabela_eventos.column("local", width=120, anchor="w")
tabela_eventos.column("orcamento", width=80, anchor="e")
tabela_eventos.column("dias", width=80, anchor="center")
tabela_eventos.pack(side="left", fill="both", expand=True, padx=5, pady=5)

aba_tarefas = tk.Frame(abas, bg=BG)
abas.add(aba_tarefas, text="Tarefas")

frame_tarefas = tk.Frame(aba_tarefas, bg=CARD, padx=10, pady=10)
frame_tarefas.pack(side="left", fill="y")

tk.Label(frame_tarefas, text="Evento:", bg=CARD).pack(anchor="w")
combo_eventos = ttk.Combobox(frame_tarefas)
combo_eventos.pack(fill="x", pady=2)

tk.Label(frame_tarefas, text="Tarefa:", bg=CARD).pack(anchor="w")
entrada_tarefa = tk.Entry(frame_tarefas)
entrada_tarefa.pack(fill="x", pady=2)

tk.Label(frame_tarefas, text="Valor:", bg=CARD).pack(anchor="w")
entrada_valor_tarefa = tk.Entry(frame_tarefas)
entrada_valor_tarefa.pack(fill="x", pady=2)

btn_adicionar_tarefa = tk.Button(frame_tarefas, text="Adicionar Tarefa", bg=ACC, fg="white", command=adicionar_tarefa)
btn_adicionar_tarefa.pack(fill="x", pady=2)
tk.Button(frame_tarefas, text="Editar Selecionado", bg=ACC, fg="white", command=editar_tarefa).pack(fill="x", pady=2)
tk.Button(frame_tarefas, text="Excluir Selecionado", bg=DEL, fg="white", command=excluir_tarefa).pack(fill="x", pady=2)

label_orcamento = tk.Label(frame_tarefas, text="Orçamento disponível: R$ 0.00", bg=CARD)
label_orcamento.pack(pady=5)

tabela_tarefas = ttk.Treeview(aba_tarefas, columns=("nome","valor"), show="headings")
tabela_tarefas.heading("nome", text="Tarefa")
tabela_tarefas.heading("valor", text="Valor (R$)")
tabela_tarefas.column("nome", width=150, anchor="w")
tabela_tarefas.column("valor", width=80, anchor="e")
tabela_tarefas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

combo_eventos.bind("<<ComboboxSelected>>", lambda e: atualizar_tarefas())

janela.mainloop()