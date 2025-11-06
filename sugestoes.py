import os
os.system('cls')
import datetime
from datetime import datetime
file=open("eventos.txt","w","encoding='utf-8'")
eventos=[]
datas=[]
name=input("digite o nome do evento:")
date=(int(input("digite o dia do evento: aa/mm/dd")))
tarefas=input("digite as tarefas do evento:")
eventos.append(name)
datas.append(date)
a=len(eventos)
for i in range(a):
    restante=datas[i]-datetime.today(()).days
    file.write(f"Faltam{restante}dias para o evento{eventos[i]} que ocorrera na data{datas[i]}\n")
    






