import os
os.system('cls')
import tkinter as tk
from tkcalendar import Calendar

# Lista de eventos
eventList = []

# Configuração da Janela
window = tk.Tk()
window.configure(bg="#FFFFFF")
window.title("FazAí")
window.geometry("1280x720")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Função para exibir data selecionada
def showDate():
    selectedDate = cal.get_date()
    label_data.config(text=f"Data selecionada: {selectedDate}")

# Função para registrar evento
def registrar_nome():
    nome = eventName.get().strip()
    if nome:
        eventList.append(nome)
        lista_eventos.insert(tk.END, nome)
        eventName.delete(0, tk.END)
        print("Evento registrado:", nome)
    else:
        print("Digite um nome antes de registrar.")

# --- Título ---
label1 = tk.Label(window, text="FazAí", bg="#FFFFFF", fg='black', font=("Arial", 48))
label1.grid(row=0, column=0, columnspan=2, pady=20)

# --- Calendário ---
cal = Calendar(window, selectmode='day', year=2025, month=10, day=28, locale='pt_BR')
cal.grid(row=1, column=0, padx=20, pady=10, sticky="n")

btn_data = tk.Button(window, text="Selecionar Data", command=showDate, font=("Arial", 12))
btn_data.grid(row=2, column=0, pady=5)

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

botao = tk.Button(frame_eventos, text="Registrar", width=20, height=2, font=("Arial", 14), command=registrar_nome)
botao.grid(row=2, column=0, pady=15)

label3 = tk.Label(frame_eventos, text="Eventos Registrados:", bg="#F8F8F8", fg='black', font=("Arial", 18, "bold"))
label3.grid(row=3, column=0, pady=(10,5))

lista_eventos = tk.Listbox(frame_eventos, width=40, height=10, font=("Arial", 14))
lista_eventos.grid(row=4, column=0, pady=5)

# --- Rodapé ---
assinatura = tk.Label(window, text="Design assinado por Gus <3", bg="#FFFFFF", fg="#777777", font=("Arial", 10))
assinatura.grid(row=6, column=0, columnspan=2, pady=10)

# Resultado Final
window.mainloop()
