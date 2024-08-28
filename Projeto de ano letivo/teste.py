# prompt:  Crie um codigo python para fazer um app de pc que tenha uma barra de pesqusa para achar videos de treino para cada musculo adicione este video como exemplo de um dos agrupamentos: https://www.instagram.com/reel/C8Nn2exP5yv/?igsh=ZjBuZHpzdTJ2M2Nw

import tkinter as tk
from tkinter import ttk
import webbrowser

# Dicionário de vídeos de treino por músculo
videos_treino = {
    "Peito": [
        "https://www.instagram.com/reel/C8Nn2exP5yv/?igsh=ZjBuZHpzdTJ2M2Nw",
        # Adicione mais vídeos para o músculo "Peito" aqui
    ],
    "Costas": [],  # Adicione vídeos para outros músculos aqui
    "Ombros": [],
    "Bíceps": [],
    "Tríceps": [],
    "Pernas": [],
    "Abdominal": []
}

def buscar_video():
    musculo = entrada_busca.get()
    if musculo in videos_treino:
        lista_resultados.delete(0, tk.END)
        for video in videos_treino[musculo]:
            lista_resultados.insert(tk.END, video)
    else:
        lista_resultados.delete(0, tk.END)
        lista_resultados.insert(tk.END, "Nenhum vídeo encontrado para este músculo.")

def abrir_video(event):
    indice_selecionado = lista_resultados.curselection()
    if indice_selecionado:
        indice = indice_selecionado[0]
        link_video = lista_resultados.get(indice)
        webbrowser.open_new_tab(link_video)

# Criando a janela principal
janela = tk.Tk()
janela.title("App de Treinos")

# Rótulo e entrada de busca
rotulo_busca = ttk.Label(janela, text="Busque por músculo:")
rotulo_busca.grid(row=0, column=0, padx=10, pady=10)

entrada_busca = ttk.Entry(janela)
entrada_busca.grid(row=0, column=1, padx=10, pady=10)

# Botão de busca
botao_buscar = ttk.Button(janela, text="Buscar", command=buscar_video)
botao_buscar.grid(row=0, column=2, padx=10, pady=10)

# Lista de resultados
lista_resultados = tk.Listbox(janela, width=50)
lista_resultados.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
lista_resultados.bind("<Double-Button-1>", abrir_video)

janela.mainloop()