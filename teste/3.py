import json

# Leitura do arquivo JSON
with open("faturamento.json", "r") as f:
    faturamento = json.load(f)

# Cálculo do menor e do maior valor de faturamento
menor_valor = min(faturamento)
maior_valor = max(faturamento)

# Cálculo da média mensal
faturamento_sem_zeros = [valor for valor in faturamento if valor > 0]
media_mensal = sum(faturamento_sem_zeros) / len(faturamento_sem_zeros)

# Cálculo do número de dias com faturamento acima da média mensal
dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

# Exibição dos resultados
print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)