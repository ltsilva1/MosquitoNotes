from tkinter import *
from tkinter import ttk, filedialog, messagebox
from models.nota import Nota
from . import layout

class MosquitoNotesApp:
    def __init__(self, root):
        root.title("Mosquito Notes - Versão em Python")
        root.geometry("600x700")

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(row=0, column=0, sticky=(N, W, E, S))

        self.nome_var = StringVar()
        self.dataHora_var = StringVar()
        self.idade_var = StringVar()
        self.observacoes_var = StringVar()
        self.modeloCelular_var = StringVar()
        self.especie_var = StringVar()
        self.genero_var = StringVar()
        self.container_var = StringVar()
        self.quantidade_var = StringVar()
        self.umidade_var = StringVar()
        self.temperatura_var = StringVar()
        self.luminosidade_var = StringVar()
        self.local_var = StringVar()
        self.acasalando_var = StringVar()
        self.metodoCriacao_var = StringVar()

        self.row_idx = 0

        self.arquivo_atual = None
        self.status_var = StringVar(value="Nenhum arquivo aberto.")

        layout.criar_formulario(self, mainframe)
        layout.criar_botoes(self, mainframe)
        layout.criar_barra_de_status(self, mainframe)

    # mesma lógica do ViewModel do swift
    def adicionar_nota(self):
        if not self.arquivo_atual:
            self.status_var.set("Nenhum arquivo aberto!")
            return

        # pega os dados das StringVars 
        nome_str = self.nome_var.get() or "Sem nome"
        data_str = self.dataHora_var.get()          
        idade_str = self.idade_var.get()            
        obs_str = self.observacoes_text.get("1.0", "end-1c")
        modelo_str = self.modeloCelular_var.get()
        especie_str = self.especie_var.get()
        genero_str = self.genero_var.get()
        container_str = self.container_var.get()
        quantidade_str = self.quantidade_var.get()
        umidade_str = self.umidade_var.get()
        temperatura_str = self.temperatura_var.get()
        luminosidade_str = self.luminosidade_var.get()
        local_str = self.local_var.get()
        acasalando_str = self.acasalando_var.get()
        metodoCriacao_str = self.metodoCriacao_var.get()
        
        nova_nota = Nota(
            nome=nome_str,
            dataHora=data_str,
            idade=idade_str,
            observacoes=obs_str,
            modeloCelular=modelo_str,
            especie=especie_str,
            genero=genero_str,
            container=container_str,
            quantidade=quantidade_str,
            umidade=umidade_str,
            temperatura=temperatura_str,
            luminosidade=luminosidade_str,
            local=local_str,
            acasalando=acasalando_str,
            metodoCriacao=metodoCriacao_str
        )

        bloco_formatado = self.formatar_nota(nova_nota)
        try:
            with open(self.arquivo_atual, "a", encoding="utf-8") as f:
                f.write(bloco_formatado)
            
            filename = self.arquivo_atual.split('/')[-1]
            self.status_var.set(f"Anotação adicionada em {filename}")
            self.limpar_campos()
        except Exception as e:
            self.status_var.set(f"Erro ao adicionar: {e}")
            messagebox.showerror("Erro ao Salvar", f"Não foi possível salvar a nota no arquivo:\n{e}")

    def formatar_nota(self, nota: Nota) -> str:
        return f""" ### Gravação - {nota.nome}
- Data e hora: {nota.dataHora}
- Latitude e longitude: {nota.local}
- Temperatura e umidade: {nota.temperatura}°C, {nota.umidade}%
- Marca / modelo do celular: {nota.modeloCelular}
- Quantidade de mosquitos: {nota.quantidade}
- Espécie dos mosquitos: {nota.especie}
- Gênero dos mosquitos: {nota.genero}
- Container utilizado: {nota.container}
- Idade dos mosquitos: {nota.idade}
- Acasalamento: {nota.acasalando}
- Método de criação: {nota.metodoCriacao}
- Luminosidade do ambiente: {nota.luminosidade}
- Outros dados / observações: {nota.observacoes}

---\n
"""

    def limpar_campos(self):
        self.nome_var.set("")
        #self.dataHora_var.set("")
        #self.idade_var.set("")
        self.observacoes_text.delete("1.0", "end")
        #self.modeloCelular_var.set("")
        #self.especie_var.set("")
        self.genero_var.set("")
        #self.container_var.set("")
        self.quantidade_var.set("")
        #self.umidade_var.set("")
        #self.temperatura_var.set("")
        #self.luminosidade_var.set("")
        #self.local_var.set("")
        #self.acasalando_var.set("")
        #self.metodoCriacao_var.set("")


    def abrir_arquivo(self):
        filepath = filedialog.askopenfilename(
            title="Selecionar arquivo existente",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not filepath:
            return
        
        self.arquivo_atual = filepath
        filename = filepath.split('/')[-1]
        self.status_var.set(f"Arquivo aberto: {filename}")
        self.add_button.config(state="normal") # habilita o botão de adicionar nota agora

    def criar_novo_arquivo(self):
        filepath = filedialog.asksaveasfilename(
            title="Criar novo arquivo",
            initialfile="notas",
            defaultextension=".txt",
            filetypes=[("Text files", ".txt"), ("All files", "*.*")]
        )
        if not filepath:
            return
            
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("") # cria arquivo vazio
            
            self.arquivo_atual = filepath
            filename = filepath.split('/')[-1]
            self.status_var.set(f"Novo arquivo criado: {filename}")
            self.add_button.config(state="normal") # # habilita o botão de adicionar nota agora 2
        except Exception as e:
            self.status_var.set(f"Erro ao criar: {e}")
            messagebox.showerror("Erro ao Criar", f"Não foi possível criar o arquivo:\n{e}")
