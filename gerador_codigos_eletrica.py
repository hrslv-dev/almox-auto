#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Códigos de Identificação para Materiais Elétricos
Almoxarifado - Setor de Elétrica
"""

import pandas as pd
import re
import hashlib
import unicodedata

class GeradorCodigosEletrica:
    """
    Gera códigos únicos e inteligentes para materiais elétricos
    baseados no nome, descrição e categoria do produto.
    """
    
    def __init__(self):
        # Prefixos por categoria comum
        self.prefixos_categoria = {
            'cabo': 'CAB',
            'fio': 'FIO',
            'disjuntor': 'DIS',
            'interruptor': 'INT',
            'tomada': 'TOM',
            'plugue': 'PLG',
            'conduíte': 'CND',
            'eletroduto': 'ELD',
            'luminária': 'LUM',
            'lâmpada': 'LAM',
            'reator': 'REA',
            'transformador': 'TRF',
            'fusível': 'FUS',
            'relé': 'REL',
            'contator': 'CNT',
            'borne': 'BOR',
            'conector': 'CON',
            'abraçadeira': 'ABR',
            'fita': 'FIT',
            'caixa': 'CXA',
            'quadro': 'QDR',
            'painel': 'PNL',
            'sensor': 'SEN',
            'timer': 'TMR',
            'socket': 'SCK',
            'resistor': 'RES',
            'capacitor': 'CAP',
            'indutor': 'IND',
            'led': 'LED',
            'driver': 'DRV',
            'fonte': 'FNT',
            'bateria': 'BAT',
            'pilha': 'PIL',
            'bucha': 'BCH',
            'parafuso': 'PAR',
            'arruela': 'ARR',
            'porca': 'POR',
            'terminal': 'TER',
            'prensa': 'PRN',
            'luva': 'LUV',
            'curva': 'CRV',
            'eletrocalha': 'ECH',
            'perfilado': 'PRF',
            'haste': 'HST',
            'aterramento': 'ATR',
            'default': 'ELE'  # Genérico para elétrica
        }
    
    def limpar_texto(self, texto):
        """Remove acentos e caracteres especiais"""
        if pd.isna(texto):
            return ""
        texto = str(texto).lower()
        # Remove acentos
        texto = unicodedata.normalize('NFKD', texto)
        texto = texto.encode('ascii', 'ignore').decode('ascii')
        # Remove caracteres especiais, mantém apenas letras, números e espaços
        texto = re.sub(r'[^a-z0-9\s]', '', texto)
        return texto.strip()
    
    def extrair_caracteristicas(self, nome, descricao):
        """Extrai características importantes do produto"""
        texto_completo = f"{nome} {descricao}".lower()
        texto_limpo = self.limpar_texto(texto_completo)
        
        caracteristicas = []
        
        # Extrai voltagem (110V, 220V, 127V, etc)
        voltagem = re.search(r'(\d+)\s*v(?:olts?)?', texto_completo)
        if voltagem:
            caracteristicas.append(f"{voltagem.group(1)}V")
        
        # Extrai amperagem (10A, 20A, etc)
        amperagem = re.search(r'(\d+)\s*a(?:mp(?:eres?)?)?', texto_completo)
        if amperagem:
            caracteristicas.append(f"{amperagem.group(1)}A")
        
        # Extrai potência (100W, 1000W, etc)
        potencia = re.search(r'(\d+)\s*w(?:atts?)?', texto_completo)
        if potencia:
            caracteristicas.append(f"{potencia.group(1)}W")
        
        # Extrai bitola/seção (2.5mm, 4mm2, etc)
        bitola = re.search(r'(\d+(?:\.\d+)?)\s*mm', texto_completo)
        if bitola:
            caracteristicas.append(f"{bitola.group(1)}MM")
        
        # Extrai metragem (10m, 100m, etc)
        metragem = re.search(r'(\d+)\s*m(?:etros?)?(?!\w)', texto_completo)
        if metragem and not bitola:  # Evita confundir com mm
            caracteristicas.append(f"{metragem.group(1)}M")
        
        # Extrai cores importantes
        cores = ['preto', 'branco', 'vermelho', 'azul', 'verde', 'amarelo', 
                 'marrom', 'cinza', 'laranja', 'rosa', 'violeta']
        for cor in cores:
            if cor in texto_limpo:
                caracteristicas.append(cor[:3].upper())
                break
        
        # Extrai polos (1P, 2P, 3P, etc)
        polos = re.search(r'(\d+)\s*p(?:olos?)?', texto_completo)
        if polos:
            caracteristicas.append(f"{polos.group(1)}P")
        
        return caracteristicas
    
    def obter_prefixo_categoria(self, categoria, nome):
        """Determina o prefixo baseado na categoria e nome"""
        texto_busca = self.limpar_texto(f"{categoria} {nome}")
        
        # Busca por palavras-chave na categoria e nome
        for palavra_chave, prefixo in self.prefixos_categoria.items():
            if palavra_chave in texto_busca:
                return prefixo
        
        return self.prefixos_categoria['default']
    
    def gerar_hash_curto(self, texto):
        """Gera um hash curto de 4 caracteres para garantir unicidade"""
        hash_obj = hashlib.md5(texto.encode())
        hash_hex = hash_obj.hexdigest()
        return hash_hex[:4].upper()
    
    def gerar_codigo(self, nome, descricao, categoria, indice):
        """
        Gera código de identificação no formato:
        PREFIXO-CARACTERISTICAS-HASH
        Exemplo: CAB-220V-4MM-PRE-A3F2
        """
        # Obtém prefixo da categoria
        prefixo = self.obter_prefixo_categoria(categoria, nome)
        
        # Extrai características do produto
        caracteristicas = self.extrair_caracteristicas(nome, descricao)
        
        # Cria texto único para o hash
        texto_unico = f"{nome}|{descricao}|{categoria}|{indice}"
        hash_codigo = self.gerar_hash_curto(texto_unico)
        
        # Monta o código
        partes = [prefixo] + caracteristicas + [hash_codigo]
        codigo = '-'.join(partes)
        
        return codigo
    
    def processar_tabela(self, df):
        """
        Processa toda a tabela e adiciona coluna de códigos
        
        Parâmetros:
        df: DataFrame com colunas 'nome', 'descricao', 'categoria'
        
        Retorna:
        DataFrame com coluna adicional 'codigo'
        """
        # Verifica se as colunas necessárias existem
        colunas_necessarias = ['nome', 'descricao', 'categoria']
        colunas_df = [col.lower() for col in df.columns]
        
        # Renomeia colunas para lowercase
        df.columns = colunas_df
        
        for col in colunas_necessarias:
            if col not in colunas_df:
                raise ValueError(f"Coluna '{col}' não encontrada na tabela. "
                               f"Colunas disponíveis: {', '.join(df.columns)}")
        
        # Gera códigos para cada linha
        codigos = []
        for idx, row in df.iterrows():
            codigo = self.gerar_codigo(
                row['nome'],
                row['descricao'],
                row['categoria'],
                idx
            )
            codigos.append(codigo)
        
        # Adiciona coluna de códigos
        df['codigo'] = codigos
        
        return df


def main():
    """Função principal - exemplo de uso"""
    print("=" * 70)
    print("GERADOR DE CÓDIGOS - ALMOXARIFADO ELÉTRICA")
    print("=" * 70)
    print()
    
    # Exemplo de tabela de entrada
    dados_exemplo = {
        'categoria': ['Cabo', 'Disjuntor', 'Lâmpada', 'Tomada', 'Cabo', 'Interruptor'],
        'nome': ['Cabo PP 2x2.5mm', 'Disjuntor 20A', 'Lâmpada LED 9W', 'Tomada 10A', 'Cabo Flexível 4mm', 'Interruptor Simples'],
        'descricao': ['Cabo PP preto 2x2.5mm rolo 100m', 'Disjuntor monopolar 20A 220V', 
                     'Lâmpada LED bulbo 9W branca 6500K', 'Tomada 2P+T 10A 250V branca',
                     'Cabo flexível vermelho 4mm rolo 100m', 'Interruptor simples 10A 250V branco']
    }
    
    df_exemplo = pd.DataFrame(dados_exemplo)
    
    print("📋 TABELA DE ENTRADA (Exemplo):")
    print(df_exemplo.to_string(index=False))
    print("\n" + "=" * 70 + "\n")
    
    # Gera códigos
    gerador = GeradorCodigosEletrica()
    df_resultado = gerador.processar_tabela(df_exemplo.copy())
    
    print("✅ TABELA COM CÓDIGOS GERADOS:")
    print(df_resultado.to_string(index=False))
    print("\n" + "=" * 70)
    print()
    print("💾 Para usar com sua própria tabela:")
    print("   1. Prepare um arquivo Excel (.xlsx) ou CSV (.csv)")
    print("   2. Certifique-se de ter as colunas: 'nome', 'descricao', 'categoria'")
    print("   3. Use o código abaixo:\n")
    print("   # Ler arquivo")
    print("   df = pd.read_excel('sua_tabela.xlsx')  # ou pd.read_csv('sua_tabela.csv')")
    print("   ")
    print("   # Gerar códigos")
    print("   gerador = GeradorCodigosEletrica()")
    print("   df_com_codigos = gerador.processar_tabela(df)")
    print("   ")
    print("   # Salvar resultado")
    print("   df_com_codigos.to_excel('tabela_com_codigos.xlsx', index=False)")
    print()


if __name__ == "__main__":
    main()
