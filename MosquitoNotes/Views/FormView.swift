//
//  FormView.swift
//  MosquitoNotes
//
//  Created by Lucas Telles on 26/10/25.
//

import SwiftUI

struct FormView: View {
    @State private var nome = ""
    @State private var quantidade = ""
    @State private var idade = ""
    @State private var umidade = ""
    @State private var local = ""
    @State private var observacoes = ""
    
    @StateObject private var viewModel = NotaViewModel()
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("🦟 Anotações de Gravação")
                .font(.largeTitle)
                .bold()
            
            Form {
                TextField("Nome da gravação:", text: $nome)
                TextField("Quantidade de mosquitos:", text: $quantidade)
                TextField("Idade (dias):", text: $idade)
                TextField("Umidade (%):", text: $umidade)
                TextField("Local (latitude e longitude):", text: $local)
                Text("Observações adicionais:")
                TextEditor(text: $observacoes)
                    .frame(height: 100)
            }
            
            HStack(spacing: 12) {
                Button("Novo arquivo") {
                    let nota = criarNota()
                    viewModel.criarNovoArquivo(nota)
                    limparCampos()
                }
                .buttonStyle(.borderedProminent)
                            
                Button("Abrir arquivo") {
                    viewModel.abrirArquivo()
                }
                .buttonStyle(.bordered)
                            
                Button("Adicionar anotação") {
                    let nota = criarNota()
                    viewModel.adicionarAnotacao(nota)
                    limparCampos()
                }
                .buttonStyle(.bordered)
                .disabled(viewModel.arquivoAtual == nil) // desativa se não há arquivo aberto
            }
            
            Divider()
            
            VStack(alignment: .leading, spacing: 4) {
                if let url = viewModel.arquivoAtual {
                    Text("Arquivo atual: \(url.lastPathComponent)")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                } else {
                    Text("Nenhum arquivo aberto.")
                        .font(.caption)
                        .foregroundColor(.secondary)
                }
                            
                if !viewModel.status.isEmpty {
                                Text(viewModel.status)
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                        }
        }
        .padding()
        .frame(width: 420, height: 500)
    }
    
    private func criarNota() -> Nota {
            Nota(
                nome: nome.isEmpty ? "Gravação sem nome" : nome,
                quantidade: quantidade,
                idade: idade,
                umidade: umidade,
                local: local,
                observacoes: observacoes
            )
    }
    
    private func limparCampos() {
        nome = ""
        quantidade = ""
        idade = ""
        umidade = ""
        local = ""
        observacoes = ""
    }
}


struct FormView_Previews: PreviewProvider {
    static var previews: some View {
        FormView()
    }
}
