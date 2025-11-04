# 📝 MosquitoNotes 🦟
Aplicativo para uso pessoal, feito em Python, com interface em Tkinter, para gerar rapidamente notas padronizadas das gravações de mosquitos na bolsa de Iniciação Científica.

Permite registrar informações como idade, umidade, método de criação e observações adicionais, exportando tudo para uma planilha do Excel (`.xlsx`) de forma cumulativa.

Esta é uma reescrita da [versão original em Swift](https://github.com/ltsilva1/MosquitoNotes/tree/swiftui-old), agora focada em ser multiplataforma e exportar dados diretamente para planilhas.

## Uso
```bash
    git clone https://github.com/ltsilva1/MosquitoNotes.git
    cd MosquitoNotes
    pip install pandas openpyxl
    python main.py
```
1.  Com o app aberto, clique em **"Novo arquivo"** para criar sua planilha `.xlsx` ou em **"Abrir arquivo"** para selecionar uma existente.
2.  Preencha os campos de anotação.
3.  Clique em **"Adicionar nota"**.
4.  Sua nota será salva como uma nova linha na planilha Excel selecionada.

### Requisitos
* Python 3.7+
* Dependências: `pandas` e `openpyxl`
