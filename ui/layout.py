from tkinter import *
from tkinter import ttk

def criar_formulario(app, mainframe):
        # Título da janela
        ttk.Label(mainframe, text="Anotações de Gravação", font=("Helvetica", 16, "bold")).grid(row=app.row_idx, column=0, columnspan=2, pady=10)
        app.row_idx += 1

        # Nome da gravação
        ttk.Label(mainframe, text="Nome da gravação:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.nome_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Data e Hora
        ttk.Label(mainframe, text="Data e hora:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.dataHora_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Umidade
        ttk.Label(mainframe, text="Umidade (%):").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.umidade_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Temperatura
        ttk.Label(mainframe, text="Temperatura (°C):").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.temperatura_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Local
        ttk.Label(mainframe, text="Local (latitude e longitude):").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.local_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Modelo do celular
        ttk.Label(mainframe, text="Modelo do celular:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.modeloCelular_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Quantidade de mosquitos
        ttk.Label(mainframe, text="Quantidade de mosquitos:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.quantidade_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Espécie
        ttk.Label(mainframe, text="Espécie:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.especie_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Gênero
        ttk.Label(mainframe, text="Gênero:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.genero_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Container
        ttk.Label(mainframe, text="Container utilizado:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.container_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Idade
        ttk.Label(mainframe, text="Idade (dias):").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.idade_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Acasalando
        ttk.Label(mainframe, text="Acasalando?").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=3)
        radio_frame = ttk.Frame(mainframe)
        ttk.Radiobutton(radio_frame, text="Sim", variable=app.acasalando_var, value="Sim").pack(side=LEFT, padx=5)
        ttk.Radiobutton(radio_frame, text="Não", variable=app.acasalando_var, value="Não").pack(side=LEFT, padx=5)
        radio_frame.grid(row=app.row_idx, column=1, sticky=W, padx=5, pady=3)
        app.row_idx += 1

        # Método de criação
        ttk.Label(mainframe, text="Método de criação:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.metodoCriacao_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Luminosidade
        ttk.Label(mainframe, text="Luminosidade do ambiente:").grid(row=app.row_idx, column=0, sticky=W, padx=5, pady=2)
        ttk.Entry(mainframe, textvariable=app.luminosidade_var, width=40).grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1

        # Observações
        ttk.Label(mainframe, text="Observações adicionais:").grid(row=app.row_idx, column=0, sticky=NW, padx=5, pady=2)
        app.observacoes_text = Text(mainframe, height=5, width=40)
        app.observacoes_text.grid(row=app.row_idx, column=1, sticky=(W, E), padx=5, pady=2)
        app.row_idx += 1


def criar_botoes(app, mainframe):
        btn_frame = ttk.Frame(mainframe)
        btn_frame.grid(row=app.row_idx, column=0, columnspan=2, pady=10)
        app.row_idx += 1

        ttk.Button(btn_frame, text="Novo arquivo", command=app.criar_novo_arquivo).pack(side=LEFT, padx=5) # Sem tk.
        ttk.Button(btn_frame, text="Abrir arquivo", command=app.abrir_arquivo).pack(side=LEFT, padx=5) # Sem tk.

        # o botão "Adicionar nota" é desabilitado no início
        app.add_button = ttk.Button(btn_frame, text="Adicionar nota", command=app.adicionar_nota, state="disabled")
        app.add_button.pack(side=LEFT, padx=5)

def criar_barra_de_status(app, mainframe):
        ttk.Separator(mainframe).grid(row=app.row_idx, column=0, columnspan=2, sticky="ew", pady=5)
        ttk.Label(mainframe, textvariable=app.status_var, font=("Helvetica", 9), foreground="gray").grid(row=app.row_idx + 1, column=0, columnspan=2, sticky=W, padx=5)
        app.row_idx += 2