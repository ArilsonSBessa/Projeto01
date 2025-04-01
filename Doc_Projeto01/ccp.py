import customtkinter as ctk
from tkinter import PhotoImage

# Função de callback para o ícone de lixeira
def on_trash_icon_click(item_number):
    print(f"Ícone de lixeira da linha {item_number} clicado!")

# Configurações do CustomTkinter
ctk.set_appearance_mode("light")  # ou "dark"
ctk.set_default_color_theme("blue")  # Altere para o tema que preferir

# Criando a janela principal
root = ctk.CTk()

# Criando um frame principal para acomodar as linhas
frame = ctk.CTkFrame(root, width=400, height=300)
frame.pack(pady=20, padx=20)

# Função para criar uma linha com texto e lixeira
def create_line(frame, text, item_number):
    # Criando um frame para cada linha
    line_frame = ctk.CTkFrame(frame)
    line_frame.pack(fill="x", pady=5)

    # Adicionando o texto da linha
    label = ctk.CTkLabel(line_frame, text=text, anchor="w")
    label.pack(side="left", padx=10, pady=5)

    # Ícone de lixeira (pode ser um emoji ou imagem)
    trash_icon = ctk.CTkButton(line_frame, text="🗑️", command=lambda: on_trash_icon_click(item_number), width=40, height=40)
    trash_icon.pack(side="right", padx=10, pady=5)

# Adicionando várias linhas
for i in range(5):
    create_line(frame, f"Item {i + 1}", i + 1)

# Exibindo a janela
root.mainloop()
