import customtkinter as ctk


def checkbox_callback(selected_checkbox):
    # Desmarca todas as outras checkboxes quando uma é selecionada
    for checkbox in checkboxes:
        if checkbox != selected_checkbox:
            checkbox.deselect()


app = ctk.CTk()
checkboxes = []

options = ["Opção 1", "Opção 2", "Opção 3"]

for i, option in enumerate(options):
    checkbox = ctk.CTkCheckBox(app, text=option)
    checkbox.configure(command=lambda cb=checkbox: checkbox_callback(cb))
    checkbox.pack(pady=5)
    checkboxes.append(checkbox)

app.mainloop()