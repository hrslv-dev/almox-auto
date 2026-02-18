# 🤖 Análise Inteligente de Materiais Elétricos

Automação avançada que recebe **APENAS DESCRIÇÕES** e gera automaticamente:
- ✅ **Categoria** do material
- ✅ **Unidade** de medida
- ✅ **Nome** resumido
- ✅ **Código** de identificação inteligente

## 🎯 O Diferencial

**Sistema Anterior:** Você precisava fornecer categoria, nome E descrição
```
INPUT:  categoria | nome | descricao
OUTPUT: categoria | nome | descricao | codigo
```

**Sistema Novo:** Você fornece APENAS a descrição, o resto é automático!
```
INPUT:  descricao
OUTPUT: descricao | categoria | unidade | nome | codigo
```

## 🚀 Como Usar (Super Simples!)

### Passo 1: Prepare sua tabela
Crie um arquivo Excel com **UMA ÚNICA COLUNA** chamada `descricao`:

| descricao |
|-----------|
| Cabo PP preto 2x2.5mm² rolo 100 metros |
| Disjuntor monopolar 20A 220V |
| Lâmpada LED 9W branca |

### Passo 2: Execute o processador
```bash
python processar_inteligente.py suas_descricoes.xlsx
```

### Passo 3: Pronto!
Um novo arquivo será criado: `suas_descricoes_completo.xlsx` com todas as colunas preenchidas!

## 📊 Exemplo Real

### ENTRADA (apenas descrição):
```
1. Cabo PP preto 2x2.5mm² rolo 100 metros
2. Disjuntor monopolar 20A 220V curva C
3. Lâmpada LED bulbo 9W branca fria 6500K
```

### SAÍDA (tabela completa):
```
┌──────────────────────────────────┬────────────┬─────────┬──────────────────┬──────────────────┐
│ descricao                        │ categoria  │ unidade │ nome             │ codigo           │
├──────────────────────────────────┼────────────┼─────────┼──────────────────┼──────────────────┤
│ Cabo PP preto 2x2.5mm² rolo...  │ Cabo       │ Metro   │ Cabo 2.5mm       │ CAB-2.5MM-PRE... │
│ Disjuntor monopolar 20A 220V...  │ Disjuntor  │ Unidade │ Disjuntor 220V...│ DIS-220V-20A-... │
│ Lâmpada LED bulbo 9W branca...  │ Lâmpada    │ Unidade │ Lâmpada 9W       │ LAM-9W-...       │
└──────────────────────────────────┴────────────┴─────────┴──────────────────┴──────────────────┘
```

## 🔍 O Que o Sistema Detecta Automaticamente

### 📦 Categorias (40+ tipos)
- Cabos, Fios, Disjuntores, Interruptores
- Tomadas, Lâmpadas, LEDs, Conduítes
- Eletrodutos, Contatores, Relés, Fusíveis
- Sensores, Timers, Drivers, Reatores
- Conectores, Terminais, Abraçadeiras
- E muito mais...

### 📏 Unidades de Medida
- **Metro**: para cabos, fios, conduítes, eletrodutos
- **Unidade**: para dispositivos individuais
- **Rolo**: para fitas isolantes
- **Pacote**: para abraçadeiras, parafusos
- **Caixa**: para kits/conjuntos
- **Par**: para pares de terminais
- **Conjunto**: para kits completos

### 🔧 Características Técnicas Extraídas
- ⚡ Voltagem: 110V, 127V, 220V, 380V
- 🔌 Amperagem: 10A, 20A, 32A, 63A
- 💡 Potência: 9W, 20W, 50W, 100W
- 📏 Bitola: 1.5mm, 2.5mm, 4mm, 10mm
- 📐 Comprimento: 10m, 50m, 100m
- 🎨 Cores: preto, branco, vermelho, azul, verde
- ⚙️ Polos: 1P, 2P, 3P

## 💻 Exemplos de Uso

### Exemplo 1: Uso Básico
```python
import pandas as pd
from analisador_inteligente import AnalisadorMaterialEletrico

# Carregar descrições
df = pd.read_excel('minhas_descricoes.xlsx')

# Processar
analisador = AnalisadorMaterialEletrico()
resultado = analisador.processar_tabela(df)

# Salvar
resultado.to_excel('resultado_completo.xlsx', index=False)
```

### Exemplo 2: Coluna com Nome Diferente
Se sua coluna não se chama "descricao":
```bash
python processar_inteligente.py arquivo.xlsx nome_da_sua_coluna
```

### Exemplo 3: Processar Material Individual
```python
from analisador_inteligente import AnalisadorMaterialEletrico

analisador = AnalisadorMaterialEletrico()
resultado = analisador.analisar_material(
    'Cabo PP preto 2x2.5mm rolo 100m',
    indice=0
)

print(resultado)
# {
#   'categoria': 'Cabo',
#   'unidade': 'Metro',
#   'nome': 'Cabo 2.5mm',
#   'codigo': 'CAB-2.5MM-PRE-729A'
# }
```

## 📂 Arquivos do Sistema

```
📦 Sistema de Análise Inteligente
├── 📄 analisador_inteligente.py          # Motor principal da IA
├── 📄 processar_inteligente.py           # Script simplificado
├── 📄 gerador_codigos_eletrica.py        # Gerador de códigos (usado internamente)
├── 📄 criar_exemplo_descricoes.py        # Cria arquivo de exemplo
├── 📊 descricoes_materiais.xlsx          # Exemplo com 55 descrições
└── 📊 descricoes_materiais_completo.xlsx # Resultado processado
```

## 🎓 Teste Rápido

Quer testar? Execute estes comandos:

```bash
# 1. Criar arquivo de exemplo
python criar_exemplo_descricoes.py

# 2. Processar o exemplo
python processar_inteligente.py descricoes_materiais.xlsx

# 3. Abrir o resultado
# descricoes_materiais_completo.xlsx
```

## 📋 Formato de Entrada Aceito

### ✅ Formato Correto
```
| descricao |
|-----------|
| Cabo PP preto 2x2.5mm² rolo 100 metros |
| Disjuntor monopolar 20A 220V |
```

### ✅ Também Funciona
Se você já tem outras colunas, sem problemas! O sistema só precisa de uma coluna com as descrições:
```
| codigo_antigo | descricao                              | estoque |
|---------------|----------------------------------------|---------|
| 001           | Cabo PP preto 2x2.5mm² rolo 100 metros | 50      |
| 002           | Disjuntor monopolar 20A 220V           | 100     |
```

O sistema irá adicionar as novas colunas (categoria, unidade, nome, codigo) mantendo as existentes.

## 🔄 Integração com Sistema Anterior

Você pode usar ambos os sistemas:

**Sistema Inteligente** (este):
- Quando você tem APENAS descrições
- Para análise automática de novos materiais
- Para importação de catálogos de fornecedores

**Sistema Anterior** (gerador_codigos_eletrica.py):
- Quando você JÁ TEM categoria e nome definidos
- Para padronização de cadastros existentes
- Para controle mais preciso das categorias

## 📊 Estatísticas do Exemplo

Ao processar o arquivo de exemplo (55 materiais):
- ✅ 24 categorias diferentes identificadas
- ✅ 4 tipos de unidades detectadas
- ✅ 55 códigos únicos gerados
- ⚡ Processamento em < 1 segundo

## ⚙️ Personalização

### Adicionar Nova Categoria
Edite `analisador_inteligente.py`:
```python
self.categorias_keywords = {
    'Sua_Categoria': ['palavra1', 'palavra2'],
    'Cabo': ['cabo', 'pp', 'paralelo'],
    # ...
}
```

### Adicionar Nova Unidade
```python
self.unidades_keywords = {
    'Sua_Unidade': ['palavra-chave'],
    'Metro': ['rolo', 'metro', 'm'],
    # ...
}
```

## 🆚 Comparação: Manual vs Automático

| Tarefa | Manual | Com Sistema |
|--------|--------|-------------|
| Classificar 100 materiais | 2-3 horas | 5 segundos |
| Definir unidades | 30-60 min | Automático |
| Gerar códigos | 1-2 horas | Automático |
| Risco de erro | Alto | Baixo |
| Consistência | Variável | 100% |

## 🎯 Casos de Uso

✅ **Importação de Catálogos**
- Recebeu catálogo de fornecedor com apenas descrições? Processe automaticamente!

✅ **Padronização de Estoque**
- Tem descrições antigas sem padrão? O sistema organiza tudo!

✅ **Novos Cadastros**
- Adicione novos materiais rapidamente sem preocupar com classificação

✅ **Migração de Sistemas**
- Migrando de outro sistema? Importe descrições e gere tudo automaticamente

## 💡 Dicas

1. **Descrições Completas**: Quanto mais informação na descrição, melhor a análise
   - ✅ "Cabo PP preto 2x2.5mm² rolo 100 metros"
   - ❌ "Cabo"

2. **Informações Técnicas**: Inclua voltagem, amperagem, bitola, etc.
   - ✅ "Disjuntor monopolar 20A 220V"
   - ❌ "Disjuntor monopolar"

3. **Unidades**: Mencione a embalagem/quantidade
   - ✅ "Abraçadeira 200mm pacote 100 unidades"
   - ❌ "Abraçadeira 200mm"

## ❓ Problemas Comuns

**"Coluna não encontrada"**
→ Certifique-se que existe uma coluna chamada 'descricao' ou especifique o nome correto

**"Categoria genérica atribuída"**
→ Adicione palavras-chave mais específicas na descrição ou personalize o sistema

**"Unidade incorreta"**
→ Inclua informações de embalagem (rolo, pacote, unidade) na descrição

## 📧 Suporte

Para melhorar o sistema:
1. Analise as descrições que não foram classificadas corretamente
2. Adicione as palavras-chave no código (seção Personalização)
3. Reprocesse o arquivo

---

**Desenvolvido para Almoxarifado - Setor de Elétrica** 🔌⚡

**Versão 2.0 - Sistema Inteligente com Análise Automática**
