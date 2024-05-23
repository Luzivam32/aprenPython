import tkinter as tk

# Função para abrir a segunda janela
def open_second_window():
    root.withdraw()  # Esconde a janela principal
    second_window = tk.Toplevel()  # Cria uma nova janela de nível superior
    second_window.title("Segunda Janela")

    # Botão para voltar à primeira janela
    back_button = tk.Button(second_window, text="Voltar", command=lambda: close_second_window(second_window))
    back_button.pack(pady=20)

    # Quando a segunda janela é fechada, mostrar novamente a janela principal
    second_window.protocol("WM_DELETE_WINDOW", lambda: close_second_window(second_window))

# Função para fechar a segunda janela e mostrar a primeira novamente
def close_second_window(window):
    window.destroy()  # Fecha a segunda janela
    root.deiconify()  # Mostra novamente a janela principal

# Cria a janela principal
root = tk.Tk()
root.title("Janela Principal")

# Botão na janela principal para abrir a segunda janela
open_button = tk.Button(root, text="Abrir Segunda Janela", command=open_second_window)
open_button.pack(pady=20)

# Inicia o loop principal da interface
root.mainloop()


