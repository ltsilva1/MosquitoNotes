//
//  Nota.swift
//  MosquitoNotes
//
//  Created by Lucas Telles on 26/10/25.
//

import Foundation

struct Nota: Identifiable, Codable {
    var id = UUID()
    let nome: String
    let quantidade: String
    let idade: String
    let umidade: String
    let local: String
    let observacoes: String
}
