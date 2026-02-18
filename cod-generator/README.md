# 🔌 Gerador de Códigos para Almoxarifado Elétrica

Automação para gerar códigos de identificação inteligentes para materiais elétricos baseados no nome, descrição e categoria do produto.

## 📋 Características dos Códigos Gerados

Os códigos são gerados no formato: **PREFIXO-CARACTERÍSTICAS-HASH**

### Exemplos:
- `CAB-220V-4MM-PRE-A3F2` → Cabo 220V, 4mm, preto
- `DIS-220V-20A-14EC` → Disjuntor 220V, 20A
- `TOM-250V-10A-2P-C693` → Tomada 250V, 10A, 2 polos
- `LED-9W-7E6D` → Lâmpada LED 9W
- `INT-250V-10A-BRA-3193` → Interruptor 250V, 10A, branco

### O sistema detecta automaticamente:
- ⚡ **Voltagem**: 110V, 127V, 220V, 380V
- 🔌 **Amperagem**: 10A, 20A, 32A, etc.
- 💡 **Potência**: 9W, 20W, 50W, etc.
- 📏 **Bitola/Seção**: 1.5mm, 2.5mm, 4mm, 10mm
- 📐 **Metragem**: 10m, 50m, 100m
- 🎨 **Cores**: preto, branco, vermelho, azul, verde, amarelo
- ⚙️ **Polos**: 1P, 2P, 3P

### Prefixos por Categoria:
| Categoria | Prefixo | Categoria | Prefixo |
|-----------|---------|-----------|---------|
| Cabo | CAB | Disjuntor | DIS |
| Fio | FIO | Interruptor | INT |
| Tomada | TOM | Lâmpada | LAM |
| LED | LED | Conduíte | CND |
| Eletroduto | ELD | Contator | CNT |
| Relé | REL | Fusível | FUS |
| Reator | REA | Transformador | TRF |
| Sensor | SEN | Timer | TMR |
| + 20 outras categorias... | ... |

## 🚀 Como Usar

### Opção 1: Modo Automático (Mais Fácil)

1. **Prepare sua tabela Excel** com as colunas:
   - `categoria` (ex: Cabo, Disjuntor, Lâmpada)
   - `nome` (ex: Cabo PP 2x2.5mm)
   - `descricao` (ex: Cabo paralelo preto 2x2.5mm rolo 100m)

2. **Execute o processador:**
   ```bash
   python processar_tabela.py seu_arquivo.xlsx
   ```

3. **Pronto!** Um novo arquivo será criado: `seu_arquivo_com_codigos.xlsx`

### Opção 2: Usando o Gerador Diretamente

```python
import pandas as pd
from gerador_codigos_eletrica import GeradorCodigosEletrica

# Ler sua tabela
df = pd.read_excel('sua_tabela.xlsx')

# Gerar códigos
gerador = GeradorCodigosEletrica()
df_com_codigos = gerador.processar_tabela(df)

# Salvar resultado
df_com_codigos.to_excel('resultado.xlsx', index=False)
```

### Opção 3: Código Individual

```python
from gerador_codigos_eletrica import GeradorCodigosEletrica

gerador = GeradorCodigosEletrica()
codigo = gerador.gerar_codigo(
    nome='Cabo PP 2x2.5mm',
    descricao='Cabo paralelo preto 2x2.5mm rolo 100m',
    categoria='Cabo',
    indice=0
)
print(codigo)  # Saída: CAB-2.5MM-PRE-6A93
```

## 📂 Estrutura de Arquivos

```
.
├── gerador_codigos_eletrica.py    # Motor principal do gerador
├── processar_tabela.py            # Script simplificado para processar arquivos
├── criar_exemplo.py               # Cria arquivo de exemplo
├── materiais_eletrica_exemplo.xlsx                # Exemplo de entrada
└── materiais_eletrica_exemplo_com_codigos.xlsx   # Exemplo de saída
```

## 💻 Requisitos

```bash
# Instalar dependências
pip install pandas openpyxl
```

**Dependências:**
- Python 3.6+
- pandas
- openpyxl (para arquivos Excel)

## 📊 Formato da Tabela de Entrada

Sua tabela **DEVE** conter estas colunas (nomes não são case-sensitive):

| categoria | nome | descricao |
|-----------|------|-----------|
| Cabo | Cabo PP 2x2.5mm | Cabo paralelo PP preto 2x2.5mm² rolo 100m |
| Disjuntor | Disjuntor 20A | Disjuntor monopolar 20A 220V curva C |
| Lâmpada | Lâmpada LED 9W | Lâmpada LED bulbo 9W branca fria 6500K |

## ✅ Saída Gerada

A tabela de saída terá todas as colunas originais **MAIS** a coluna `codigo`:

| categoria | nome | descricao | **codigo** |
|-----------|------|-----------|---------|
| Cabo | Cabo PP 2x2.5mm | Cabo paralelo... | **CAB-2.5MM-PRE-6A93** |
| Disjuntor | Disjuntor 20A | Disjuntor monopolar... | **DIS-220V-20A-D152** |
| Lâmpada | Lâmpada LED 9W | Lâmpada LED bulbo... | **LED-9W-7E6D** |

## 🎯 Vantagens

✅ **Códigos Inteligentes**: Baseados nas características reais do produto  
✅ **Únicos**: Hash garante que não haverá duplicação  
✅ **Legíveis**: Fácil identificar o produto apenas pelo código  
✅ **Automático**: Processa centenas de itens em segundos  
✅ **Flexível**: Suporta Excel (.xlsx) e CSV (.csv)  

## 🔧 Personalização

Para adicionar novos prefixos ou categorias, edite o dicionário `prefixos_categoria` em `gerador_codigos_eletrica.py`:

```python
self.prefixos_categoria = {
    'seu_produto': 'PRD',  # Adicione aqui
    'cabo': 'CAB',
    # ...
}
```

## 📝 Exemplo Completo

```bash
# 1. Criar arquivo de exemplo
python criar_exemplo.py

# 2. Processar o arquivo
python processar_tabela.py materiais_eletrica_exemplo.xlsx

# 3. Verificar resultado
# O arquivo 'materiais_eletrica_exemplo_com_codigos.xlsx' será criado
```

## ❓ Problemas Comuns

**"Coluna não encontrada"**
- Certifique-se que sua tabela tem as colunas: `categoria`, `nome`, `descricao`

**"Arquivo não encontrado"**
- Verifique o caminho do arquivo
- Use o caminho completo se necessário

**"Erro ao salvar"**
- Feche o arquivo Excel antes de processar
- Verifique permissões de escrita na pasta

## 📧 Suporte

Para dúvidas ou problemas:
1. Verifique se os nomes das colunas estão corretos
2. Confirme que o arquivo não está aberto em outro programa
3. Teste com o arquivo de exemplo primeiro

---

**Desenvolvido para Almoxarifado - Setor de Elétrica** 🔌⚡
