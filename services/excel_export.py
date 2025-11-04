
import pandas as pd
import os
from models.nota import Nota

COLUNAS = [
        "Nome", "Data e Hora", "Umidade", "Temperatura", "Local", "Modelo do Celular",
        "Quantidade", "Espécie", "Gênero", "Container", "Idade",  "Acasalando", "Método de Criação", "Luminosidade", "Observações"
    ]

MAPA_DE_COLUNAS = { # mapeia os atributos da classe para os nomes das colunas
    'nome': 'Nome',
    'dataHora': 'Data e Hora',
    'umidade': 'Umidade',
    'temperatura': 'Temperatura',
    'local': 'Local',
    'modeloCelular': 'Modelo do Celular',
    'quantidade': 'Quantidade',
    'especie': 'Espécie',
    'genero': 'Gênero',
    'container': 'Container',
    'idade': 'Idade',
    'acasalando': 'Acasalando',
    'metodoCriacao': 'Método de Criação',
    'luminosidade': 'Luminosidade',
    'observacoes': 'Observações'
}

def salvar_nota_excel(nota: Nota, filepath: str):
    nova_linha_dict = nota.__dict__ 

    # formatações básicas pra alguns campos
    temp_val = nova_linha_dict.get('temperatura')
    if temp_val:
        nova_linha_dict['temperatura'] = f"{temp_val}°C"

    umid_val = nova_linha_dict.get('umidade')
    if umid_val:
        nova_linha_dict['umidade'] = f"{umid_val}%"

    df_nova_nota = pd.DataFrame(nova_linha_dict, index=[0])
    df_nova_nota.rename(columns=MAPA_DE_COLUNAS, inplace=True) # magica para renomear as colunas

    try:
        if not os.path.exists(filepath): # arquivo novo
            df_para_salvar = df_nova_nota
            
        else: # arquivo existente, concatena o antigo com o novo
            df_antigo = pd.read_excel(filepath, engine='openpyxl')
            df_para_salvar = pd.concat([df_antigo, df_nova_nota], ignore_index=True)

        df_para_salvar = df_para_salvar.reindex(columns=COLUNAS) # garantiazinha de que as colunas estão na ordem correta

        with pd.ExcelWriter(filepath, engine='openpyxl') as writer: # OBSERVAÇÃO: Essa lógica pra ajustar a largura das colunas PRECISA estar na função que salva o excel, pq se não o openpyxl zera as larguras personalizadas
            df_para_salvar.to_excel(writer, sheet_name='Notas', index=False)
            worksheet = writer.sheets['Notas']
            
            for coluna in worksheet.columns:
                coluna_letra = coluna[0].column_letter
                header_texto = worksheet[f'{coluna_letra}1'].value

                if header_texto == "Nome":
                    worksheet.column_dimensions[coluna_letra].width = 30

                elif header_texto == "Observações":
                    worksheet.column_dimensions[coluna_letra].width = 50

                elif header_texto == "Local":
                    worksheet.column_dimensions[coluna_letra].width = 25

                elif header_texto == "Modelo do Celular":
                    worksheet.column_dimensions[coluna_letra].width = 20

                elif header_texto == "Método de Criação":
                    worksheet.column_dimensions[coluna_letra].width = 20

                else:
                    new_width = len(str(header_texto)) + 2
                    worksheet.column_dimensions[coluna_letra].width = new_width

        return True, None

    except Exception as e:
        return False, str(e)