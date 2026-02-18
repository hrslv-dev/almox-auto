#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automação Completa - Análise Inteligente de Materiais Elétricos
Input: Apenas DESCRIÇÃO
Output: CATEGORIA + UNIDADE + CÓDIGO
"""

import pandas as pd
import re
from gerador_codigos_eletrica import GeradorCodigosEletrica


class AnalisadorMaterialEletrico:
    """
    Analisa descrições de materiais elétricos e extrai:
    - Categoria do produto
    - Unidade de medida
    - Nome resumido
    Depois gera o código usando o GeradorCodigosEletrica
    """
    
    def __init__(self):
        self.gerador = GeradorCodigosEletrica()
        
        # Dicionário de palavras-chave para categorias
        self.categorias_keywords = {
            'Cabo': ['cabo', 'pp', 'paralelo'],
            'Fio': ['fio', 'rigido', 'flexivel'],
            'Disjuntor': ['disjuntor', 'djt'],
            'Interruptor': ['interruptor', 'int'],
            'Tomada': ['tomada', 'tom'],
            'Plugue': ['plugue', 'plug'],
            'Conduíte': ['conduite', 'condulete'],
            'Eletroduto': ['eletroduto'],
            'Luminária': ['luminaria'],
            'Lâmpada': ['lampada'],
            'LED': ['led'],
            'Reator': ['reator'],
            'Transformador': ['transformador', 'trafo'],
            'Fusível': ['fusivel', 'fus'],
            'Relé': ['rele'],
            'Contator': ['contator'],
            'Borne': ['borne'],
            'Conector': ['conector'],
            'Abraçadeira': ['abracadeira'],
            'Fita': ['fita isolante', 'fita'],
            'Caixa': ['caixa'],
            'Quadro': ['quadro'],
            'Painel': ['painel'],
            'Sensor': ['sensor'],
            'Timer': ['timer', 'temporizador'],
            'Socket': ['socket', 'soquete'],
            'Resistor': ['resistor'],
            'Capacitor': ['capacitor'],
            'Indutor': ['indutor'],
            'Driver': ['driver'],
            'Fonte': ['fonte'],
            'Bateria': ['bateria'],
            'Pilha': ['pilha'],
            'Bucha': ['bucha'],
            'Parafuso': ['parafuso'],
            'Arruela': ['arruela'],
            'Porca': ['porca'],
            'Terminal': ['terminal'],
            'Prensa': ['prensa cabo', 'prensa'],
            'Luva': ['luva'],
            'Curva': ['curva'],
            'Eletrocalha': ['eletrocalha'],
            'Perfilado': ['perfilado'],
            'Haste': ['haste'],
            'Aterramento': ['aterramento'],
            'Disjuntor Motor': ['disjuntor motor'],
            'Minuteria': ['minuteria'],
            'Dimmer': ['dimmer'],
            'Varistor': ['varistor'],
            'Campainha': ['campainha'],
            'Sirene': ['sirene'],
            'Refletor': ['refletor'],
            'Projetor': ['projetor'],
        }
        
        # Dicionário de unidades por tipo de material
        self.unidades_keywords = {
            'Metro': ['rolo', 'metro', 'm', 'rolo de'],
            'Unidade': ['unidade', 'peça', 'peca', 'un'],
            'Caixa': ['caixa', 'cx'],
            'Pacote': ['pacote', 'pct', 'pacote com'],
            'Conjunto': ['conjunto', 'conj'],
            'Kit': ['kit'],
            'Par': ['par'],
            'Jogo': ['jogo'],
            'Barra': ['barra'],
            'Rolo': ['rolo'],
        }
    
    def limpar_texto(self, texto):
        """Remove acentos e normaliza texto"""
        import unicodedata
        if pd.isna(texto):
            return ""
        texto = str(texto).lower()
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.encode('ascii', 'ignore').decode('ascii')
        return texto.strip()
    
    def detectar_categoria(self, descricao):
        """Detecta a categoria do material baseado na descrição"""
        descricao_limpa = self.limpar_texto(descricao)
        
        # Busca por ordem de prioridade (mais específico primeiro)
        categorias_ordenadas = sorted(
            self.categorias_keywords.items(),
            key=lambda x: -len(x[0])
        )
        
        for categoria, keywords in categorias_ordenadas:
            for keyword in keywords:
                # Busca palavra completa para evitar falsos positivos
                if re.search(r'\b' + re.escape(keyword) + r'\b', descricao_limpa):
                    return categoria
        
        return 'Material Elétrico'  # Categoria genérica
    
    def detectar_unidade(self, descricao, categoria):
        """Detecta a unidade de medida baseada na descrição e categoria"""
        descricao_limpa = self.limpar_texto(descricao)
        
        # Prioriza unidades mais específicas
        for unidade, keywords in self.unidades_keywords.items():
            for keyword in keywords:
                if keyword in descricao_limpa:
                    return unidade
        
        # Regras específicas por categoria
        if categoria in ['Cabo', 'Fio', 'Conduíte', 'Eletroduto', 'Eletrocalha']:
            if any(word in descricao_limpa for word in ['rolo', 'metro', 'm']):
                return 'Metro'
            return 'Metro'
        
        if categoria in ['Abraçadeira', 'Parafuso', 'Arruela', 'Bucha', 'Porca']:
            if any(word in descricao_limpa for word in ['pacote', 'pct', 'cx', 'caixa']):
                return 'Pacote'
            return 'Unidade'
        
        if categoria in ['Fita']:
            return 'Rolo'
        
        # Default: Unidade
        return 'Unidade'
    
    def extrair_nome_resumido(self, descricao, categoria):
        """Extrai um nome resumido da descrição"""
        descricao_limpa = descricao.strip()
        
        # Tenta extrair especificações técnicas importantes
        specs = []
        
        # Voltagem
        voltagem = re.search(r'(\d+)\s*v', descricao_limpa, re.IGNORECASE)
        if voltagem:
            specs.append(f"{voltagem.group(1)}V")
        
        # Amperagem
        amperagem = re.search(r'(\d+)\s*a(?:\s|$)', descricao_limpa, re.IGNORECASE)
        if amperagem:
            specs.append(f"{amperagem.group(1)}A")
        
        # Bitola/Seção
        bitola = re.search(r'(\d+(?:\.\d+)?)\s*mm', descricao_limpa, re.IGNORECASE)
        if bitola:
            specs.append(f"{bitola.group(1)}mm")
        
        # Potência
        potencia = re.search(r'(\d+)\s*w', descricao_limpa, re.IGNORECASE)
        if potencia:
            specs.append(f"{potencia.group(1)}W")
        
        # Polos
        polos = re.search(r'(\d+)\s*p(?:olos?)?', descricao_limpa, re.IGNORECASE)
        if polos:
            specs.append(f"{polos.group(1)}P")
        
        # Monta nome
        if specs:
            nome = f"{categoria} {' '.join(specs)}"
        else:
            # Pega as primeiras palavras relevantes
            palavras = descricao_limpa.split()[:3]
            nome = ' '.join(palavras)
        
        return nome
    
    def analisar_material(self, descricao, indice):
        """
        Analisa uma descrição e retorna categoria, unidade, nome e código
        
        Returns:
            dict com 'categoria', 'unidade', 'nome', 'codigo'
        """
        # Detecta categoria
        categoria = self.detectar_categoria(descricao)
        
        # Detecta unidade
        unidade = self.detectar_unidade(descricao, categoria)
        
        # Extrai nome resumido
        nome = self.extrair_nome_resumido(descricao, categoria)
        
        # Gera código
        codigo = self.gerador.gerar_codigo(
            nome=nome,
            descricao=descricao,
            categoria=categoria,
            indice=indice
        )
        
        return {
            'categoria': categoria,
            'unidade': unidade,
            'nome': nome,
            'codigo': codigo
        }
    
    def processar_tabela(self, df, coluna_descricao='descricao'):
        """
        Processa tabela completa
        
        Parâmetros:
        df: DataFrame com coluna de descrição
        coluna_descricao: nome da coluna com a descrição (padrão: 'descricao')
        
        Retorna:
        DataFrame com colunas: descricao, categoria, unidade, nome, codigo
        """
        # Normaliza nome da coluna
        colunas_df = {col.lower(): col for col in df.columns}
        coluna_descricao_lower = coluna_descricao.lower()
        
        if coluna_descricao_lower not in colunas_df:
            raise ValueError(
                f"Coluna '{coluna_descricao}' não encontrada. "
                f"Colunas disponíveis: {', '.join(df.columns)}"
            )
        
        coluna_real = colunas_df[coluna_descricao_lower]
        
        # Processa cada descrição
        resultados = []
        for idx, descricao in enumerate(df[coluna_real]):
            resultado = self.analisar_material(descricao, idx)
            resultado['descricao'] = descricao
            resultados.append(resultado)
        
        # Cria DataFrame resultado
        df_resultado = pd.DataFrame(resultados)
        
        # Reordena colunas
        colunas_ordenadas = ['descricao', 'categoria', 'unidade', 'nome', 'codigo']
        df_resultado = df_resultado[colunas_ordenadas]
        
        return df_resultado


def main():
    """Função principal - exemplo de uso"""
    print("=" * 80)
    print("🤖 ANÁLISE INTELIGENTE DE MATERIAIS ELÉTRICOS")
    print("=" * 80)
    print()
    print("📋 Input:  APENAS DESCRIÇÃO")
    print("📊 Output: CATEGORIA + UNIDADE + NOME + CÓDIGO")
    print()
    print("=" * 80)
    print()
    
    # Exemplos de descrições
    descricoes_exemplo = [
        'Cabo PP preto 2x2.5mm rolo 100 metros',
        'Disjuntor monopolar 20A 220V curva C',
        'Lâmpada LED bulbo 9W branca fria 6500K E27',
        'Tomada 2P+T 10A 250V padrão NBR14136 branca',
        'Fio rígido azul 1.5mm rolo 100 metros',
        'Fita isolante preta 19mm x 20m autofusão',
        'Conduíte corrugado amarelo 3/4 polegada rolo 50m',
        'Contator tripolar 25A 220V bobina CA',
        'Abraçadeira nylon preta 200mm x 4.8mm pacote 100un',
        'Interruptor simples 10A 250V branco',
        'Reator eletrônico 2x20W bivolt alta frequência',
        'Quadro distribuição 12 disjuntores embutir metal',
        'Eletroduto rígido PVC 1/2 polegada cinza barra 3m',
        'Driver LED 50W 127-220V IP20 regulável',
        'Sensor presença teto 360° 6m alcance branco'
    ]
    
    # Cria DataFrame de entrada
    df_entrada = pd.DataFrame({'descricao': descricoes_exemplo})
    
    print("📥 TABELA DE ENTRADA (Apenas descrições):")
    print("-" * 80)
    for i, desc in enumerate(df_entrada['descricao'], 1):
        print(f"{i:2d}. {desc}")
    print()
    print("=" * 80)
    print()
    
    # Processa
    print("⚙️  Analisando materiais com IA...")
    analisador = AnalisadorMaterialEletrico()
    df_resultado = analisador.processar_tabela(df_entrada)
    print("✅ Análise concluída!")
    print()
    print("=" * 80)
    print()
    
    # Mostra resultado
    print("📊 TABELA COMPLETA GERADA:")
    print("-" * 80)
    # Mostra de forma mais legível
    for idx, row in df_resultado.iterrows():
        print(f"\n{idx + 1}. {row['descricao']}")
        print(f"   └─ Categoria: {row['categoria']}")
        print(f"   └─ Unidade:   {row['unidade']}")
        print(f"   └─ Nome:      {row['nome']}")
        print(f"   └─ Código:    {row['codigo']}")
    
    print()
    print("=" * 80)
    print()
    print("💾 Para usar com sua própria tabela:")
    print()
    print("   # Opção 1: Tabela com apenas uma coluna 'descricao'")
    print("   df = pd.read_excel('suas_descricoes.xlsx')")
    print()
    print("   # Opção 2: Tabela com várias colunas, especifique qual é a descrição")
    print("   df = pd.read_excel('sua_tabela.xlsx')")
    print()
    print("   # Processar")
    print("   analisador = AnalisadorMaterialEletrico()")
    print("   df_resultado = analisador.processar_tabela(df, coluna_descricao='descricao')")
    print()
    print("   # Salvar")
    print("   df_resultado.to_excel('resultado_completo.xlsx', index=False)")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
