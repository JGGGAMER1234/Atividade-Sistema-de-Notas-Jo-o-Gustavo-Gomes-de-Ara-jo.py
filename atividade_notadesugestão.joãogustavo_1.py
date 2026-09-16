notas = [8.5, 7.2, 9.1, 6.8, 8.0, 7.5, 9.5, 8.8, 7.0, 8.3]

# Quantidade de alunos
quantidade = len(notas)

# Cálculos
media = sum(notas) / quantidade
maior = max(notas)
menor = min(notas)

# Resultados
print("Quantidade de alunos:", quantidade)
print("Média da turma:", round(media, 2))
print("Maior nota:", maior)
print("Menor nota:", menor)
