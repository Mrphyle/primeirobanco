import numpy as np
import matplotlib.pyplot as plt
categorias = ['1', '2', '3', '4', '5','6']
valores_yes = [6, 7, 5, 6, 4, 5]
valores_no = [4, 3, 5, 4, 6, 5]
x = np.arange(len(categorias))
largura_barra = 0.35
fig, ax = plt.subplots()
barras_yes = ax.bar(x - largura_barra/2, valores_yes, largura_barra, label='Yes')
barras_no = ax.bar(x + largura_barra/2, valores_no, largura_barra, label='No')
ax.set_title('What healthy habits do you practice?')
ax.set_xlabel('Questions')
ax.set_ylabel('Quantity')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
def autolabel(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate('{}'.format(altura),
                    xy=(barra.get_x() + barra.get_width() / 2, altura),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(barras_yes)
autolabel(barras_no)
plt.show()