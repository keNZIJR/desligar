import tkinter as tk
from tkinter import ttk
import subprocess

def converter_minutos_para_segundos(minutos):
    return minutos * 60

def desligar():
    minutos = tempo_entry.get()
    try:
        minutos = int(minutos)
        if minutos <= 0:
            resultado_label.config(text="Digite um valor maior que 0.")
        else:
            segundos = converter_minutos_para_segundos(minutos)
            subprocess.run(f"shutdown -s -t {segundos}")
            resultado_label.config(text=f"Desligando em {minutos} minutos.")
    except ValueError:
        resultado_label.config(text="Tempo inválido. Insira um número inteiro.")

def cancelar_desligamento():
    subprocess.run("shutdown -a")
    resultado_label.config(text="Desligamento cancelado.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Programa de Desligamento")
janela.geometry("400x250")

# Estilo com cores de fundo cinza
style = ttk.Style()

# Cor de fundo do botão Desligar
style.configure('Desligar.TButton', background='#404040', foreground='white', font=('Helvetica', 12))

# Cor de fundo do botão Cancelar
style.configure('Cancelar.TButton', background='#E53935', foreground='white', font=('Helvetica', 12))

# Cor de fundo dos rótulos e entrada de texto
style.configure('TLabel', background='#F5F5F5', foreground='#333', font=('Helvetica', 12))
style.configure('TEntry', background='white', foreground='#333', font=('Helvetica', 12))

# Borda dos botões e entradas
style.map('Desligar.TButton', background=[('active', '#303030')])  # Mudança de cor ao passar o mouse
style.map('Cancelar.TButton', background=[('active', '#C62828')])  # Mudança de cor ao passar o mouse
style.map('TEntry', relief=[('active', 'solid')])  # Borda quando ativo

# Rótulo de instrução
instrucao_label = ttk.Label(janela, text="Digite o tempo em minutos para desligar o Windows:")
instrucao_label.pack(pady=10)

# Entrada de tempo
tempo_entry = ttk.Entry(janela)
tempo_entry.pack()

# Botão de desligar
desligar_button = ttk.Button(janela, text="Desligar", style='Desligar.TButton', command=desligar)
desligar_button.pack(pady=10)

# Botão de cancelar
cancelar_button = ttk.Button(janela, text="Cancelar Desligamento", style='Cancelar.TButton', command=cancelar_desligamento)
cancelar_button.pack(pady=10)

# Rótulo de resultado
resultado_label = ttk.Label(janela, text="", background='#F5F5F5', foreground='#E53935')
resultado_label.pack()

# Rótulo de desenvolvedor
desenvolvido_por_label = ttk.Label(janela, text="Desenvolvido por FTP Team", background='#F5F5F5', foreground='#333')
desenvolvido_por_label.pack()

# Configurar a cor de fundo da janela
janela.configure(bg='#F5F5F5')

# Iniciar a janela
janela.mainloop()
