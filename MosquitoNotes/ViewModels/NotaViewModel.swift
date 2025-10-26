//
//  NotaViewModel.swift
//  MosquitoNotes
//
//  Created by Lucas Telles on 26/10/25.
//

import Foundation
import AppKit

@MainActor
final class NotaViewModel: ObservableObject {
    @Published var status = ""
    @Published var arquivoAtual: URL? = nil
    
    // MARK: - Cria nova anotação
    func criarNovoArquivo(_ nota: Nota) {
        let bloco = formatarNota(nota)
        
        let savePanel = NSSavePanel()
        savePanel.title = "Criar novo arquivo"
        savePanel.nameFieldStringValue = "notas.md"
        savePanel.allowedContentTypes = [.plainText]
        
        if savePanel.runModal() == .OK, let url = savePanel.url {
            do {
                try bloco.write(to: url, atomically: true, encoding: .utf8)
                arquivoAtual = url
                status = "Novo arquivo criado: \(url.lastPathComponent)"
            } catch {
                status = "Erro ao criar: \(error.localizedDescription)"
            }
        }
    }
    
    // MARK: - Abre arquivo existente
    func abrirArquivo() {
        let openPanel = NSOpenPanel()
        openPanel.title = "Selecionar arquivo existente"
        openPanel.allowedContentTypes = [.plainText]
        openPanel.allowsMultipleSelection = false
        
        if openPanel.runModal() == .OK, let url = openPanel.url {
            arquivoAtual = url
            status = "Arquivo aberto: \(url.lastPathComponent)"
        }
    }
    
    // MARK: - Adiciona anotação ao arquivo atual
    func adicionarAnotacao(_ nota: Nota) {
        guard let url = arquivoAtual else {
            status = "Nenhum arquivo aberto!"
            return
        }
        
        let bloco = formatarNota(nota)
        
        do {
            if FileManager.default.fileExists(atPath: url.path) {
                let handle = try FileHandle(forWritingTo: url)
                handle.seekToEndOfFile()
                if let data = bloco.data(using: .utf8) {
                    handle.write(data)
                    handle.closeFile()
                }
                status = "Anotação adicionada em \(url.lastPathComponent)"
            } else {
                try bloco.write(to: url, atomically: true, encoding: .utf8)
                status = "Arquivo não existia, foi criado novamente"
            }
        } catch {
            status = "Erro ao adicionar: \(error.localizedDescription)"
        }
    }
    
    // MARK: - Formatação Markdown
    private func formatarNota(_ nota: Nota) -> String {
        """
        ### Gravação - \(nota.nome)
        - Quantidade de mosquitos: \(nota.quantidade)
        - Idade: \(nota.idade)
        - Umidade: \(nota.umidade)%
        - Local: \(nota.local)
        - Observações: \(nota.observacoes)
        
        """
    }
}
