import matplotlib.pyplot as plt

# Dados
gases = ['Hélio', 'Hidrogênio', 'Ar', 'Dióxido de Carbono']
min_tempo = [6, 6, 48, 72]
max_tempo = [12, 12, 72, 120]

# Criação do gráfico de barras
fig, ax = plt.subplots()

# Adicionando barras para o tempo mínimo e máximo
ax.bar(gases, min_tempo, label='Tempo Mínimo (horas)', color='blue', alpha=0.6)
ax.bar(gases, max_tempo, label='Tempo Máximo (horas)', color='red', alpha=0.6)

# Adicionando rótulos e título
ax.set_xlabel('Gás')
ax.set_ylabel('Taxa de Esvaziamento (horas)')
ax.set_title('Taxa de Esvaziamento de Balões com Diferentes Gases')
ax.legend()

# Exibindo o gráfico
plt.show()