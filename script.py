# ========================================
# 1) Cálculo da variável SOMA
# ========================================

def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K
   
    print(f"Valor final de SOMA: {SOMA}")

calcular_soma()

# ========================================
# 2) Verificar se um número pertence à sequência de Fibonacci
# ========================================

def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
   
    if b == numero or numero == 0:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Teste com um número
pertence_fibonacci(21)

# ========================================
# 3) Análise de faturamento diário
# ========================================

import json

# Simulando dados em JSON (exemplo fictício)
dados_faturamento = """
{
    "dias": [0, 1200, 1800, 0, 2200, 3400, 0, 2900, 3200, 2500, 0, 0, 4000, 0, 1000, 2700, 3000, 0, 1500, 1800]
}
"""

def analisar_faturamento(json_data):
    dados = json.loads(json_data)
    valores = [v for v in dados["dias"] if v > 0]  # Ignorando dias sem faturamento

    menor = min(valores)
    maior = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for v in valores if v > media_mensal)

    print(f"Menor faturamento: R${menor}")
    print(f"Maior faturamento: R${maior}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

analisar_faturamento(dados_faturamento)

# ========================================
# 4) Percentual de faturamento por estado
# ========================================

def calcular_percentual():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total = sum(faturamento_estados.values())

    for estado, valor in faturamento_estados.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}% do faturamento total.")

calcular_percentual()

# ========================================
# 5) Inverter uma string (sem usar funções prontas)
# ========================================

def inverter_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida  # Concatenação reversa
   
    print(f"String invertida: {invertida}")

# Teste com uma string
inverter_string("Hello, World!")


