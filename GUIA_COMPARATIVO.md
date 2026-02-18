# 🔌 Guia Completo - Sistemas de Codificação de Materiais Elétricos

## 📚 Dois Sistemas Disponíveis

Você tem acesso a **DOIS sistemas complementares** para gerenciar seus materiais elétricos:

### 🎯 Sistema 1: Gerador de Códigos (Básico)
**Input:** Categoria + Nome + Descrição  
**Output:** Código de Identificação  
**Arquivo:** `gerador_codigos_eletrica.py`

### 🤖 Sistema 2: Análise Inteligente (Avançado)
**Input:** Apenas Descrição  
**Output:** Categoria + Unidade + Nome + Código  
**Arquivo:** `analisador_inteligente.py`

---

## 🆚 Comparação Rápida

| Característica | Sistema Básico | Sistema Inteligente |
|----------------|----------------|---------------------|
| **Input mínimo** | 3 colunas (categoria, nome, descrição) | 1 coluna (descrição) |
| **Output** | 1 coluna (código) | 4 colunas (categoria, unidade, nome, código) |
| **Controle** | Manual - você define categoria e nome | Automático - IA analisa e define |
| **Velocidade** | Rápido | Muito Rápido |
| **Precisão** | 100% (você decide) | 95%+ (IA decide) |
| **Ideal para** | Dados já estruturados | Dados não estruturados |

---

## 🎯 Quando Usar Cada Sistema

### Use o Sistema BÁSICO quando:

✅ Você já tem os dados organizados com categoria e nome  
✅ Quer controle total sobre a classificação  
✅ Está padronizando um cadastro existente bem definido  
✅ Precisa de precisão absoluta na categorização  

**Exemplo de Caso:**
```
Você tem uma planilha assim:
| categoria  | nome              | descricao                    |
|------------|-------------------|------------------------------|
| Cabo       | Cabo PP 2.5mm     | Cabo PP preto 2x2.5mm...    |
| Disjuntor  | Disjuntor 20A     | Disjuntor monopolar 20A...  |
```

### Use o Sistema INTELIGENTE quando:

✅ Você só tem descrições de materiais (catálogo de fornecedor)  
✅ Quer automatizar todo o processo de classificação  
✅ Precisa processar grandes volumes rapidamente  
✅ Está importando dados de outro sistema  
✅ Quer que o sistema defina categoria e unidade automaticamente  

**Exemplo de Caso:**
```
Você tem uma planilha assim:
| descricao                                      |
|------------------------------------------------|
| Cabo PP preto 2x2.5mm rolo 100 metros         |
| Disjuntor monopolar 20A 220V curva C          |
```

---

## 📖 Exemplos Práticos

### Exemplo 1: Sistema Básico

**Entrada:**
```python
# arquivo: materiais.xlsx
categoria  | nome              | descricao
-----------|-------------------|----------------------------------
Cabo       | Cabo PP 2x2.5mm   | Cabo PP preto 2x2.5mm rolo 100m
Disjuntor  | Disjuntor 20A     | Disjuntor monopolar 20A 220V
```

**Comando:**
```bash
python processar_tabela.py materiais.xlsx
```

**Saída:**
```python
# arquivo: materiais_com_codigos.xlsx
categoria  | nome              | descricao                    | codigo
-----------|-------------------|------------------------------|------------------
Cabo       | Cabo PP 2x2.5mm   | Cabo PP preto 2x2.5mm...    | CAB-2.5MM-PRE-82ED
Disjuntor  | Disjuntor 20A     | Disjuntor monopolar 20A...  | DIS-220V-20A-14EC
```

---

### Exemplo 2: Sistema Inteligente

**Entrada:**
```python
# arquivo: descricoes.xlsx
descricao
------------------------------------------------
Cabo PP preto 2x2.5mm rolo 100 metros
Disjuntor monopolar 20A 220V curva C
```

**Comando:**
```bash
python processar_inteligente.py descricoes.xlsx
```

**Saída:**
```python
# arquivo: descricoes_completo.xlsx
descricao                      | categoria | unidade | nome            | codigo
-------------------------------|-----------|---------|-----------------|------------------
Cabo PP preto 2x2.5mm...      | Cabo      | Metro   | Cabo 2.5mm      | CAB-2.5MM-PRE-729A
Disjuntor monopolar 20A...    | Disjuntor | Unidade | Disjuntor 220V..| DIS-220V-20A-E348
```

---

## 🔄 Workflow Recomendado

### Cenário A: Importação de Catálogo de Fornecedor

1. **Recebeu:** Lista com apenas descrições
2. **Use:** Sistema Inteligente
3. **Processo:**
   ```bash
   python processar_inteligente.py catalogo_fornecedor.xlsx
   ```
4. **Revise:** O resultado gerado (opcional)
5. **Importe:** Para seu sistema de estoque

### Cenário B: Padronização de Cadastro Existente

1. **Tem:** Cadastro com categoria, nome e descrição
2. **Use:** Sistema Básico
3. **Processo:**
   ```bash
   python processar_tabela.py cadastro_atual.xlsx
   ```
4. **Resultado:** Códigos padronizados mantendo suas definições

### Cenário C: Processo Híbrido (Recomendado!)

1. **Use Sistema Inteligente** para gerar primeira versão
2. **Revise e ajuste** categorias/unidades se necessário
3. **Use Sistema Básico** para regenerar códigos com suas correções

**Exemplo:**
```bash
# Passo 1: Análise automática
python processar_inteligente.py materiais.xlsx

# Resultado: materiais_completo.xlsx
# Revise manualmente e corrija se necessário

# Passo 2: Regenerar códigos com dados corrigidos
python processar_tabela.py materiais_completo.xlsx

# Resultado final: materiais_completo_com_codigos.xlsx
```

---

## 📊 Exemplos de Arquivos

### Arquivo para Sistema BÁSICO:
```
materiais_entrada.xlsx:
┌────────────┬───────────────────┬─────────────────────────────────┐
│ categoria  │ nome              │ descricao                       │
├────────────┼───────────────────┼─────────────────────────────────┤
│ Cabo       │ Cabo PP 2x2.5mm   │ Cabo PP preto 2x2.5mm rolo 100m│
│ Disjuntor  │ Disjuntor 20A     │ Disjuntor monopolar 20A 220V    │
│ Lâmpada    │ Lâmpada LED 9W    │ Lâmpada LED bulbo 9W branca     │
└────────────┴───────────────────┴─────────────────────────────────┘
```

### Arquivo para Sistema INTELIGENTE:
```
descricoes_entrada.xlsx:
┌──────────────────────────────────────────────┐
│ descricao                                    │
├──────────────────────────────────────────────┤
│ Cabo PP preto 2x2.5mm rolo 100 metros       │
│ Disjuntor monopolar 20A 220V curva C        │
│ Lâmpada LED bulbo 9W branca fria 6500K E27  │
└──────────────────────────────────────────────┘
```

---

## 🚀 Instalação e Requisitos

### Requisitos
```bash
pip install pandas openpyxl
```

### Estrutura de Arquivos
```
📦 Sistema Completo
│
├── 📁 Sistema Básico
│   ├── gerador_codigos_eletrica.py
│   ├── processar_tabela.py
│   ├── criar_exemplo.py
│   └── README.md
│
├── 📁 Sistema Inteligente
│   ├── analisador_inteligente.py
│   ├── processar_inteligente.py
│   ├── criar_exemplo_descricoes.py
│   └── README_INTELIGENTE.md
│
└── 📄 GUIA_COMPARATIVO.md (este arquivo)
```

---

## 💡 Dicas Profissionais

### 1. Para Máxima Eficiência
Use o Sistema Inteligente para processamento inicial rápido, depois refine manualmente casos específicos se necessário.

### 2. Para Máxima Precisão
Use o Sistema Básico quando você precisa de controle absoluto sobre cada classificação.

### 3. Para Grandes Volumes
Sistema Inteligente é ideal - processa centenas de itens em segundos.

### 4. Para Integrações
Ambos sistemas podem ser integrados via Python em seus workflows existentes.

---

## 📞 Scripts de Linha de Comando

### Sistema Básico
```bash
# Uso básico
python processar_tabela.py sua_tabela.xlsx

# O arquivo DEVE ter: categoria, nome, descricao
```

### Sistema Inteligente
```bash
# Uso básico (coluna se chama 'descricao')
python processar_inteligente.py suas_descricoes.xlsx

# Se sua coluna tem outro nome
python processar_inteligente.py arquivo.xlsx nome_da_coluna
```

---

## 🎯 Resumo Final

| Situação | Sistema | Comando |
|----------|---------|---------|
| Tenho categoria, nome e descrição | Básico | `python processar_tabela.py arquivo.xlsx` |
| Tenho apenas descrição | Inteligente | `python processar_inteligente.py arquivo.xlsx` |
| Quero controle total | Básico | ⬆️ |
| Quero velocidade máxima | Inteligente | ⬆️ |
| Importando catálogo | Inteligente | ⬆️ |
| Padronizando cadastro | Básico | ⬆️ |

---

## 🎓 Tutoriais em Vídeo (Resumo)

### Tutorial 1: Sistema Básico
```
1. Abra seu Excel
2. Certifique-se de ter colunas: categoria, nome, descricao
3. Salve como materiais.xlsx
4. Execute: python processar_tabela.py materiais.xlsx
5. Abra materiais_com_codigos.xlsx
```

### Tutorial 2: Sistema Inteligente
```
1. Abra seu Excel
2. Crie uma coluna chamada 'descricao'
3. Preencha com as descrições dos materiais
4. Salve como descricoes.xlsx
5. Execute: python processar_inteligente.py descricoes.xlsx
6. Abra descricoes_completo.xlsx
```

---

## ✅ Checklist: Qual Sistema Usar?

Responda SIM/NÃO:

- [ ] Já tenho categoria e nome definidos? → SIM = Sistema Básico
- [ ] Tenho apenas descrições? → SIM = Sistema Inteligente
- [ ] Quero que o sistema decida a categoria? → SIM = Sistema Inteligente
- [ ] Preciso de controle total? → SIM = Sistema Básico
- [ ] Vou processar 100+ itens? → Ambos funcionam bem
- [ ] Importando dados de fornecedor? → Sistema Inteligente
- [ ] Migração de sistema legado? → Sistema Inteligente primeiro

---

**🎉 Agora você está pronto para usar ambos os sistemas!**

Para dúvidas específicas, consulte:
- `README.md` - Documentação do Sistema Básico
- `README_INTELIGENTE.md` - Documentação do Sistema Inteligente

---

**Desenvolvido para Almoxarifado - Setor de Elétrica** 🔌⚡
