import os
os.system('cls')
import tkinter as tk

eventList = []

#Configuração da Janela

window = tk.Tk()
window.configure(bg='#E0218A')
window.title("FazAí")
window.geometry("1920x1080")

#Conteúdo da Janela
label1 = tk.Label(window, text="FazAí", bg='#E0218A', fg='white', font=("Arial", 48))
label1.pack(pady=20)
label2 = tk.Label(window, text="Nome do evento:", bg='#E0218A', fg='white', font=("Arial", 28))
label2.pack(pady=20)

def registrar_nome():
    nome = eventName.get().strip()
    if nome:
        eventList.append(nome)
        eventName.delete(0, tk.END)
        print("Nomes registrados:", nome)  
    else:
        print("Digite um nome antes de registrar.")

eventName = tk.Entry(window,fg='black', font=("Arial", 24))
eventName.pack(pady=10)
botao = tk.Button(window, text="Registrar", width=20, height=2, font=("Arial", 14), command=registrar_nome)
botao.pack(pady=20)

label3 = tk.Label(window, text="Eventos Registrados:", bg='#E0218A', fg='white', font=("Arial", 28))
label3.pack(pady=20)
label4= tk.Label(window, text=eventList, bg='#E0218A', fg='white', font=("Arial", 24))
label4.pack(pady=10)

lista_eventos = tk.Listbox(window, width=40, height=10)
lista_eventos.pack(pady=10)

#Resultado Final
window.mainloop()

#Design assinado por Gus <3,
