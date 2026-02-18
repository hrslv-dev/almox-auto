#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Processador Simplificado - Análise Inteligente de Materiais
Input: Tabela com coluna de DESCRIÇÃO
Output: Tabela completa com CATEGORIA + UNIDADE + NOME + CÓDIGO
"""

import pandas as pd
import sys
import os
from analisador_inteligente import AnalisadorMaterialEletrico


def processar_arquivo_inteligente(arquivo_entrada, coluna_descricao='descricao'):
    """
    Processa arquivo Excel ou CSV com análise inteligente
    
    Args:
        arquivo_entrada: caminho do arquivo (.xlsx ou .csv)
        coluna_descricao: nome da coluna com descrições
    """
    print("\n" + "="*80)
    print("🤖 ANÁLISE INTELIGENTE - MATERIAIS ELÉTRICOS")
    print("="*80 + "\n")
    
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
    
    print(f"✅ Arquivo lido! Total de linhas: {len(df)}")
    print(f"📋 Colunas encontradas: {', '.join(df.columns)}\n")
    
    # Tenta encontrar coluna de descrição
    colunas_lower = {col.lower(): col for col in df.columns}
    
    if coluna_descricao.lower() not in colunas_lower:
        print("⚠️  Coluna de descrição não encontrada com o nome padrão.")
        print("📋 Colunas disponíveis:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i}. {col}")
        print()
        
        # Tenta detectar automaticamente
        possiveis = ['descricao', 'descrição', 'desc', 'material', 'produto']
        for possivel in possiveis:
            if possivel in colunas_lower:
                coluna_descricao = colunas_lower[possivel]
                print(f"✅ Detectado automaticamente: '{coluna_descricao}'")
                break
        else:
            print("❌ Não foi possível detectar a coluna de descrição.")
            print("💡 Renomeie a coluna para 'descricao' ou especifique o nome correto.")
            return
    else:
        coluna_descricao = colunas_lower[coluna_descricao.lower()]
    
    # Analisa materiais
    print(f"\n⚙️  Analisando {len(df)} materiais com IA...")
    print("    └─ Extraindo categoria automaticamente")
    print("    └─ Determinando unidade de medida")
    print("    └─ Gerando códigos inteligentes")
    print()
    
    try:
        analisador = AnalisadorMaterialEletrico()
        df_resultado = analisador.processar_tabela(df, coluna_descricao=coluna_descricao)
        print("✅ Análise concluída com sucesso!\n")
    except Exception as e:
        print(f"❌ ERRO ao processar: {e}")
        return
    
    # Salva resultado
    nome_base = arquivo_entrada.rsplit('.', 1)[0]
    extensao = arquivo_entrada.rsplit('.', 1)[1]
    nome_saida = f"{nome_base}_completo.{extensao}"
    
    print(f"💾 Salvando resultado em: {nome_saida}")
    try:
        if nome_saida.endswith('.xlsx') or nome_saida.endswith('.xls'):
            df_resultado.to_excel(nome_saida, index=False)
        else:
            df_resultado.to_csv(nome_saida, index=False)
        print("✅ Arquivo salvo com sucesso!")
    except Exception as e:
        print(f"❌ ERRO ao salvar: {e}")
        return
    
    # Estatísticas
    print("\n" + "="*80)
    print("📊 ESTATÍSTICAS DA ANÁLISE:")
    print("-"*80)
    
    print(f"\n📦 Total de materiais processados: {len(df_resultado)}")
    
    print(f"\n📁 Categorias identificadas:")
    categorias_count = df_resultado['categoria'].value_counts()
    for cat, count in categorias_count.items():
        print(f"   • {cat}: {count} item(s)")
    
    print(f"\n📏 Unidades detectadas:")
    unidades_count = df_resultado['unidade'].value_counts()
    for unid, count in unidades_count.items():
        print(f"   • {unid}: {count} item(s)")
    
    # Preview
    print("\n" + "="*80)
    print("🔍 PREVIEW DOS RESULTADOS (primeiras 5 linhas):")
    print("-"*80)
    
    for idx, row in df_resultado.head(5).iterrows():
        print(f"\n{idx + 1}. {row['descricao'][:70]}...")
        print(f"   ├─ Categoria: {row['categoria']}")
        print(f"   ├─ Unidade:   {row['unidade']}")
        print(f"   ├─ Nome:      {row['nome']}")
        print(f"   └─ Código:    {row['codigo']}")
    
    if len(df_resultado) > 5:
        print(f"\n   ... e mais {len(df_resultado) - 5} itens")
    
    print("\n" + "="*80)
    print(f"✅ PROCESSO CONCLUÍDO!")
    print(f"📄 Arquivo gerado: {nome_saida}")
    print("="*80 + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Argumento 1: arquivo
        arquivo = sys.argv[1]
        # Argumento 2 (opcional): nome da coluna
        coluna = sys.argv[2] if len(sys.argv) > 2 else 'descricao'
        processar_arquivo_inteligente(arquivo, coluna)
    else:
        # Procura arquivos na pasta
        print("\n🔍 Procurando arquivos Excel/CSV na pasta atual...\n")
        arquivos = [f for f in os.listdir('.') 
                   if f.endswith(('.xlsx', '.xls', '.csv')) 
                   and not f.startswith('~') 
                   and '_completo' not in f
                   and '_com_codigos' not in f]
        
        if not arquivos:
            print("❌ Nenhum arquivo encontrado!")
            print("\n💡 COMO USAR:")
            print("="*80)
            print()
            print("   python processar_inteligente.py seu_arquivo.xlsx")
            print()
            print("   OU (se sua coluna tiver outro nome):")
            print()
            print("   python processar_inteligente.py seu_arquivo.xlsx nome_da_coluna")
            print()
            print("="*80)
            print()
            print("📋 FORMATO DO ARQUIVO:")
            print("   Sua tabela precisa ter UMA coluna com as descrições dos materiais")
            print("   Exemplo:")
            print()
            print("   | descricao                              |")
            print("   |----------------------------------------|")
            print("   | Cabo PP preto 2x2.5mm rolo 100 metros |")
            print("   | Disjuntor monopolar 20A 220V          |")
            print("   | Lâmpada LED 9W branca                 |")
            print()
            print("   O sistema irá AUTOMATICAMENTE adicionar:")
            print("   • Categoria")
            print("   • Unidade")
            print("   • Nome")
            print("   • Código")
            print()
        else:
            print("📁 Arquivos encontrados:")
            for i, arquivo in enumerate(arquivos, 1):
                print(f"   {i}. {arquivo}")
            
            if len(arquivos) == 1:
                print(f"\n⚙️  Processando '{arquivos[0]}'...\n")
                processar_arquivo_inteligente(arquivos[0])
            else:
                print("\n💡 Para processar um arquivo específico:")
                print("   python processar_inteligente.py nome_do_arquivo.xlsx")
