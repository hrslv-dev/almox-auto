#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Simplificado - Processar Tabela de Materiais Elétricos
"""

import pandas as pd
import sys
import os

# Importa o gerador
from gerador_codigos_eletrica import GeradorCodigosEletrica


def processar_arquivo(arquivo_entrada):
    """
    Processa arquivo Excel ou CSV com materiais elétricos
    
    Args:
        arquivo_entrada: caminho do arquivo (Excel .xlsx ou CSV .csv)
    """
    print("\n" + "="*70)
    print("🔌 PROCESSADOR DE CÓDIGOS - MATERIAIS ELÉTRICOS")
    print("="*70 + "\n")
    
    # Verifica se arquivo existe
    if not os.path.exists(arquivo_entrada):
        print(f"❌ ERRO: Arquivo '{arquivo_entrada}' não encontrado!")
        return
    
    # Lê o arquivo
    print(f"📂 Lendo arquivo: {arquivo_entrada}")
    try:
        if arquivo_entrada.endswith('.xlsx') or arquivo_entrada.endswith('.xls'):
            df = pd.read_excel(arquivo_entrada)
        elif arquivo_entrada.endswith('.csv'):
            df = pd.read_csv(arquivo_entrada)
        else:
            print("❌ ERRO: Formato não suportado. Use .xlsx ou .csv")
            return
    except Exception as e:
        print(f"❌ ERRO ao ler arquivo: {e}")
        return
    
    print(f"✅ Arquivo lido com sucesso! Total de itens: {len(df)}")
    print(f"📋 Colunas encontradas: {', '.join(df.columns)}\n")
    
    # Gera códigos
    print("⚙️  Gerando códigos de identificação...")
    try:
        gerador = GeradorCodigosEletrica()
        df_resultado = gerador.processar_tabela(df)
        print("✅ Códigos gerados com sucesso!\n")
    except Exception as e:
        print(f"❌ ERRO ao gerar códigos: {e}")
        return
    
    # Salva resultado
    nome_saida = arquivo_entrada.rsplit('.', 1)[0] + '_com_codigos.' + arquivo_entrada.rsplit('.', 1)[1]
    
    print(f"💾 Salvando resultado em: {nome_saida}")
    try:
        if nome_saida.endswith('.xlsx') or nome_saida.endswith('.xls'):
            df_resultado.to_excel(nome_saida, index=False)
        else:
            df_resultado.to_csv(nome_saida, index=False)
        print("✅ Arquivo salvo com sucesso!")
    except Exception as e:
        print(f"❌ ERRO ao salvar arquivo: {e}")
        return
    
    # Mostra preview
    print("\n" + "="*70)
    print("📊 PREVIEW DOS RESULTADOS (primeiras 10 linhas):")
    print("="*70)
    print(df_resultado[['categoria', 'nome', 'codigo']].head(10).to_string(index=False))
    print("\n" + "="*70)
    print(f"✅ PROCESSO CONCLUÍDO! Arquivo salvo: {nome_saida}")
    print("="*70 + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Se passou arquivo como argumento
        processar_arquivo(sys.argv[1])
    else:
        # Procura por arquivos na pasta atual
        print("\n🔍 Procurando arquivos Excel/CSV na pasta atual...\n")
        arquivos = [f for f in os.listdir('.') if f.endswith(('.xlsx', '.xls', '.csv')) 
                   and not f.startswith('~') and 'com_codigos' not in f]
        
        if not arquivos:
            print("❌ Nenhum arquivo Excel ou CSV encontrado!")
            print("\n💡 COMO USAR:")
            print("   python processar_tabela.py seu_arquivo.xlsx")
            print("   ou")
            print("   python processar_tabela.py seu_arquivo.csv")
        else:
            print("📁 Arquivos encontrados:")
            for i, arquivo in enumerate(arquivos, 1):
                print(f"   {i}. {arquivo}")
            
            if len(arquivos) == 1:
                print(f"\n⚙️  Processando '{arquivos[0]}'...\n")
                processar_arquivo(arquivos[0])
            else:
                print("\n💡 Para processar um arquivo específico:")
                print("   python processar_tabela.py nome_do_arquivo.xlsx")
