# 🎉 CRUD-PYTHON – Projeto *Organiza Festa*  
**Sistema de Planejamento de Eventos**

---

## 🧩 Descrição do Problema

Cláudia adora organizar festas e eventos, mas enfrenta dificuldades para controlar **convidados, pagamentos, fornecedores** e **tarefas**.  
Pensando nisso, o sistema **“Organiza Festa”** foi criado para ajudar Cláudia (e outros organizadores) a **planejar eventos de forma prática**, mantendo tudo **dentro do prazo e do orçamento**.

---

## ⚙️ Requisitos Funcionais

### 1. CRUD de Eventos  
O usuário poderá **adicionar, visualizar, editar e excluir** eventos com as seguintes informações:  
- Nome do evento  
- Tipo (aniversário, casamento, reunião, etc.)  
- Data  
- Local  
- Orçamento disponível  

### 2. Tarefas e Orçamento  
O usuário poderá **cadastrar tarefas** (ex: decoração, buffet, música ao vivo) e definir seus **custos**.  
Esses valores serão **descontados automaticamente** do orçamento do evento.

### 3. Contagem Regressiva  
Ao visualizar um evento, o sistema exibirá **quantos dias faltam** para sua realização.

### 4. Armazenamento de Dados  
Todos os registros serão **salvos em arquivos `.csv` ou `.txt`**, garantindo histórico e persistência das informações.

### 5. Sugestões Personalizadas  
Com base no **tipo do evento** e no **número de convidados**, o sistema poderá sugerir:  
- Fornecedores  
- Decoração adequada  
- Cardápio recomendado  
- Atividades e entretenimento  

### 6. Funcionalidade Extra  
Os grupos poderão propor **funcionalidades criativas adicionais** que complementem o projeto.

---

## 🧱 Requisitos Não Funcionais

1. **Tecnologia:**  
   - Desenvolvido em **Python**, **sem uso de bibliotecas externas**.  
   - Interação via **linha de comando (terminal)**.  
   - Bibliotecas permitidas:  
     - `os` → para `os.system("clear")` ou `os.system("cls")`  
     - `datetime`  
     - `random`  
     - Outras bibliotecas apenas com **autorização dos professores**.

2. **Trabalho em Equipe:**  
   - O projeto deve ser feito **em grupo**.  
   - **Trabalhos individuais** terão **redução de 50%** na nota.

3. **Organização do Código:**  
   - Uso de **funções** para modularizar e evitar repetições.  
   - **Tratamento de exceções** para lidar com erros e entradas inválidas.  
   - **Boas práticas de legibilidade**, com nomes claros para variáveis e funções.
