//
//  FormView.swift
//  MosquitoNotes
//
//  Created by Lucas Telles on 26/10/25.
//

import SwiftUI

struct FormView: View {
    @State private var nome = ""
    @State private var dataHora = ""
    @State private var local = ""
    @State private var umidade = ""
    @State private var temperatura = ""
    @State private var modeloCelular = ""
    @State private var quantidade = ""
    @State private var especie = ""
    @State private var genero = ""
    @State private var container = ""
    @State private var idade = ""
    @State private var acasalando = ""
    @State private var metodoCriacao = ""
    @State private var luminosidade = ""
    @State private var observacoes = ""
    
    @StateObject private var viewModel = NotaViewModel()
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Anotações de Gravação")
                .font(.largeTitle)
                .bold()
                .frame(maxWidth: .infinity, alignment: .center)
            
            Form() {
                Section {
                    TextField("Nome da gravação:", text: $nome)
                    TextField("Data e hora:", text: $dataHora)
                    TextField("Umidade (%):", text: $umidade)
                    TextField("Temperatura (°C):", text: $temperatura)
                    TextField("Local (latitude e longitude):", text: $local)
                    TextField("Modelo do celular:", text: $modeloCelular)
                    TextField("Quantidade de mosquitos:", text: $quantidade)
                    TextField("Espécie:", text: $especie)
                    TextField("Genero:", text: $genero)
                    TextField("Container:", text: $container)
                }
            
                Section {
                    TextField("Idade (dias):", text: $idade)
                    Picker(selection: $acasalando, label: Text("Acasalando?")) {
                        Text("Sim").tag("Sim")
                        Text("Não").tag("Não")
                    }
                    .pickerStyle(.radioGroup)
                    .horizontalRadioGroupLayout()
                    TextField("Método de criação:", text: $metodoCriacao)
                    TextField("Luminosidade do ambiente:", text: $luminosidade)
                    
                    Text("Observações adicionais:")
                    TextEditor(text: $observacoes)
                        .frame(height: 100)
                }
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
                            
                Button("Adicionar nota") {
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
        .frame(width: 600, height: 700)
    }
    
    private func criarNota() -> Nota {
            Nota(
                nome: nome.isEmpty ? "Sem nome" : nome,
                dataHora: dataHora,
                modeloCelular: modeloCelular,
                especie: especie,
                genero: genero,
                container: container,
                quantidade: quantidade,
                idade: idade,
                umidade: umidade,
                temperatura: temperatura,
                luminosidade: luminosidade,
                local: local,
                acasalando: acasalando,
                metodoCriacao: metodoCriacao,
                observacoes: observacoes
            )
    }
    
    private func limparCampos() {
        nome = ""
        dataHora = ""
        // local = ""
        umidade = ""
        // modeloCelular = ""
        quantidade = ""
        // especie = ""
        genero = ""
        // container = ""
        idade = ""
        acasalando = ""
        metodoCriacao = ""
        // luminosidade = ""
        observacoes = ""
    }
    
}


struct FormView_Previews: PreviewProvider {
    static var previews: some View {
        FormView()
    }
}
