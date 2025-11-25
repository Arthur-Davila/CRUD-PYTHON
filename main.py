import os
os.system('cls')
import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk

# --- ESTRUTURA DE DADOS UNIFICADA ---
records = [] # Lista principal que armazena dicionários: [{'id': 1, 'nome': '...', 'data': '...'}]
next_id = 1 
# --- FIM ESTRUTURA DE DADOS UNIFICADA ---

# Configuração da Janela (Permanece a mesma)
window = tk.Tk()
window.configure(bg="#FFFFFF")
window.title("FazAí - Agenda")
window.geometry("1280x720")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Variável para armazenar o nome temporariamente
window.temp_event_name = None 

# --- FUNÇÕES CORE (CREATE / READ) ---

def update_event_treeview():
    """Limpa e preenche o Treeview com os dados de 'records'."""
    # 1. Limpar registros existentes
    for iid in tree.get_children():
        tree.delete(iid)
    
    # 2. Inserir os novos registros
    for record in records:
        # A ordem deve ser: 'id', 'nome', 'data', 'ações'
        tree.insert('', tk.END, values=(record['id'], record['nome'], record['data'], ''))

def registrar_nome():
    """Valida o nome do evento e libera a seleção da data."""
    global window
    nome = eventName.get().strip()
    if nome:
        window.temp_event_name = nome # Armazena o nome
        btn_data.config(state="normal")
        botao.config(state="disabled") # Desativa o Registrar até a data ser escolhida
    # Não há necessidade de 'eventList.append(nome)' nem 'lista_eventos.insert()' aqui.

def showDate():
    """Registra o evento completo (Nome + Data) e atualiza o Treeview."""
    global next_id, window
    
    if window.temp_event_name is None:
        # Garante que o nome foi registrado antes
        return 

    btn_data.config(state="disabled")
    selectedDate = cal.get_date()
    
    # Cria o novo registro unificado
    new_record = {
        'id': next_id,
        'nome': window.temp_event_name,
        'data': selectedDate
    }
    records.append(new_record)
    next_id += 1
    
    # Atualiza a interface
    eventName.delete(0, tk.END)
    update_event_treeview() # Chama a função de preenchimento do Treeview
    
    label_data.config(text=f"Data selecionada: {selectedDate}")
    window.temp_event_name = None # Limpa o nome temporário
    botao.config(state="normal")

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

# --- FUNÇÕES DE ESTILOS (Para o design da tabela) ---

style = ttk.Style(window)
style.theme_use("clam")

# Configuração de Estilos para o Calendário (mantido)
style.configure("my.TCalendar",
                background="#282A36", 
                foreground="#F8F8F2", 
                fieldbackground="#282A36",
                bordercolor="#44475A",
                lightcolor="#44475A",
                darkcolor="#44475A",
                arrowcolor="#BD93F9")

# Configuração de Estilos para o Treeview
style.configure("Treeview.Heading", 
                font=("Arial", 10, "bold"),
                background="#F0F0F0") 
style.configure("Treeview",
                rowheight=25,
                fieldbackground='#FFFFFF') 


# --- Título, Calendário e Botões de Data (Mantidos) ---
label1 = tk.Label(window, text="FazAí", bg="#FFFFFF", fg='black', font=("Arial", 48))
label1.grid(row=0, column=0, columnspan=2, pady=20)

cal = Calendar(window, selectmode="day", year=2025, month=11, day=4, date_pattern="dd/mm/yyyy",
    background="#000000", disabledbackground="#A9A9A9", bordercolor="#000000", headersbackground="#FFFFFF", 
    headersforeground="#000000", normalbackground="#FFFFFF", normalforeground="#000000", 
    weekendbackground="#000000", weekendforeground="#FFFFFF", othermonthbackground="#A9A9A9", 
    othermonthwebackground="#696969", othermonthforeground="#D3D3D3", othermonthweforeground="#A9A9A9", 
    selectbackground="#2E2E2E", selectforeground="#FFFFFF", font=("Helvetica", 11, "bold"), cursor="hand1", style="my.TCalendar")
cal.grid(row=1, column=0, padx=20, pady=10, sticky="n")

btn_data = tk.Button(window, text="Selecionar Data", command=showDate, font=("Arial", 12))
btn_data.grid(row=2, column=0, pady=5)
btn_data.config(state="disabled")

label_data = tk.Label(window, text="", bg="#FFFFFF", font=("Arial", 14))
label_data.grid(row=3, column=0, pady=5)

# --- FRAME: Painel de Eventos ---
frame_eventos = tk.Frame(window, bg="#F8F8F8", bd=3, relief="groove", padx=20, pady=20)
frame_eventos.grid(row=1, column=1, rowspan=4, padx=40, pady=20, sticky="n")

# Widgets dentro do frame
label2 = tk.Label(frame_eventos, text="Nome do evento:", bg="#F8F8F8", fg='black', font=("Arial", 20))
label2.grid(row=0, column=0, sticky="w", pady=(0,10))

eventName = tk.Entry(frame_eventos, fg='black', font=("Arial", 18), width=25)
eventName.grid(row=1, column=0, pady=5)

botao = tk.Button(frame_eventos, text="Registrar", width=20, height=2, font=("Arial", 14), command= registrar_nome)
botao.grid(row=2, column=0, pady=15)

# Removendo o botão "Editar" de onde ele estava
edit_btn = tk.Button(frame_eventos, text="Editar", width=10, height=1, font=("Arial", 14), command= edit_evento)
edit_btn.grid(row=2, column=1) # Desabilitado por enquanto
edit_btn.config(state="normal")

label3 = tk.Label(frame_eventos, text="Eventos Registrados:", bg="#F8F8F8", fg='black', font=("Arial", 18, "bold"))
label3.grid(row=3, column=0, columnspan=3, pady=(10,5), sticky="w") # Sticky W para alinhar à esquerda

# --- IMPLEMENTAÇÃO DO TREEVIEW ---
columns = ('id', 'nome', 'data', 'acoes') 
tree = ttk.Treeview(frame_eventos, 
                    columns=columns, 
                    show='headings', 
                    height=10)

# Configurando os Cabeçalhos
tree.heading('id', text='ID')
tree.heading('nome', text='Nome do Evento')
tree.heading('data', text='Data')
tree.heading('acoes', text='') # Coluna para os botões

# Configurando as Larguras
tree.column('id', width=40, anchor='center', stretch=tk.NO)
tree.column('nome', width=180, anchor='w')
tree.column('data', width=100, anchor='center')
tree.column('acoes', width=80, anchor='center', stretch=tk.NO) 

# Posicionamento do Treeview
tree.grid(row=4, column=0, columnspan=3, pady=5, sticky="ew")

# Adicionando uma Scrollbar para melhorar o uso
scrollbar = ttk.Scrollbar(frame_eventos, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=4, column=3, sticky='ns')

# --- Rodapé ---
assinatura = tk.Label(window, text="Design assinado por Gus <3", bg="#FFFFFF", fg="#777777", font=("Arial", 10))
assinatura.grid(row=6, column=0, columnspan=2, pady=10)

# Resultado Final
window.mainloop()
