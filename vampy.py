#bibliotecas
import tkinter as tk
from tkinter import Label,Button, Toplevel
def janI():
    root.withdraw() # esconde a janela principal
    janI = tk.Toplevel() #cria uma nova janela de nível superior
    janI.title("Cadastrar")
    janI.geometry("800x300")

    Cabecario = Label(janI, text="Cadastro", font=('Arial', 24))
    Cabecario.pack(pady=20)
    #button de voltar
    back_button = tk.Button(janI, text='Voltar', command=lambda : closet_janI(janI))
    back_button.pack(pady=20)

    #quando a seguda janela é fechada,mosta novamente a janela principal
    janI.protocol("Wn_DELETE_WINDOW", lambda: closet_janI(janI))

# função de fecha a segunda janela e mostrar a janela principal
def closet_janI(window):
    window.destroy()
    root.deiconify()
#criar janela principal
root = tk.Tk()
root.title("Programa com Tk")
root.geometry("400x200")
CabecarioI = Label(root ,text="Inicio", font=("Arial",24))
CabecarioI.pack(pady=20)

# Button para abrir a segunda janela
cadastro_button = tk.Button(root, text='Cadastrar', command=janI)
cadastro_button.pack(pady=20)


# Inicia o loop principal da interface
root.mainloop()