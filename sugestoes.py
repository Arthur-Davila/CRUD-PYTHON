import os
os.system('cls')
import datetime
from datetime import datetime
arquivo = open("eventos.txt","w",encoding='utf-8')
eventos=[]
datas=[]
name=input("digite o nome do evento:")
eventos.append(name)
date =int(input("digite o dia do evento aa/mm/dd: "))
datas.append(date)
data_obj=datetime.strptime(str(date),"%d/%m/%y)" )
a=len(eventos)

arquivo.write(f"---Eventos  e Datas---\n {eventos}\t\t\t\t{datas}\n")
for i in range(a):
    restante=datas[i]-datetime.today(()).days
    
    if restante<0:
        arquivo.write(f'O evento {eventos[i]} já ocorreu na data {datas[i]} \n')
    elif restante==0:
        arquivo.write(f"O evento {eventos[i]} acontecerá na data de hoje {datas[i]} \n")
    else:
        arquivo.write(f"Faltam {restante} dias para o evento {eventos[i]} que ocorrera na data {datas[i]} \n")

arquivo.close()

