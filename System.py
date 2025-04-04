import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random
import sqlite3

###

# Definição de variáveis
x = 0
y = 0

#definição do git

# importando a tabela

aleatorio = []
aleatorio2 = []
aleatorio3 = []
aleatoriors = []

saida_produtos = []  # Lista para armazenar os produtos e quantidades de saída

for i in range(1, 101):
    aleatorio.append(random.randint(1, 1000))
    aleatorio2.append(random.randint(1, 1000))
    aleatorio3.append(random.randint(1, 1000))
    aleatoriors.append(random.randint(1, 1000))


def criar_banco():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS itens (nome text, preco decimal, descricao text)")
    conexao.commit()
    conexao.close()
#dfgdfgf
#cghghgh
def limpar_campos_cadastro():
    entrada_cadastrar_nome_produto.delete(0, tk.END)
    entrada_cadastrar_preco.delete(0, tk.END)
    caixa_texto_cadastrar_descricao.delete('1.0', tk.END)


def salvar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(
        f"INSERT INTO itens (nome, preco, descricao) VALUES ('{entrada_cadastrar_nome_produto.get()}', "
        f"'{float(entrada_cadastrar_preco.get())}', '{caixa_texto_cadastrar_descricao.get('1.0', 'end')}')")
    conexao.commit()
    conexao.close()

    limpar_campos_cadastro()



criar_banco()


def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM itens")
    recebe_dados = terminal_sql.fetchall()
    for item in tree_estoque.get_children():
        tree_estoque.delete(item)

    for j in recebe_dados:
        nome = str(j[0])
        quantidade = 0
        preco = "R$ {:.2f}".format(float(j[1]))
        descricao = str(j[2])
        tree_estoque.insert('', tk.END, values=(nome, quantidade, preco, descricao))


def produtos_dados():
    global check_var
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM itens")
    items = terminal_sql.fetchall()

    for wigets_edit in scrollable_frame_editar.winfo_children():
        wigets_edit.destroy()

    check_var = customtkinter.StringVar()
    for item in items:
        box = customtkinter.CTkCheckBox(scrollable_frame_editar, text=item, onvalue=item, offvalue="",
                                        variable=check_var,
                                        command=lambda: ler_dados_produto_selecionado(check_var, scrollable_frame_editar) if check_var.get() else apagar_entradas_produto_desmarcado(scrollable_frame_editar))
        box.pack(pady=5, padx=10, fill="x")

def produtos_dados_entrada():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM itens")
    items = terminal_sql.fetchall()

    for wigets_edit in scrollable_frame_entrada.winfo_children():
        wigets_edit.destroy()

    check_var = customtkinter.StringVar()
    for item in items:
        box = customtkinter.CTkCheckBox(scrollable_frame_entrada, text=item, onvalue=item, offvalue="",
                                        variable=check_var,
                                        command=lambda: ler_dados_produto_selecionado(check_var, scrollable_frame_entrada) if check_var.get() else apagar_entradas_produto_desmarcado(scrollable_frame_entrada))
        box.pack(pady=0, padx=10, fill="x")


def produtos_dados_saida():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM itens")
    items = terminal_sql.fetchall()

    for wigets_edit in scrollable_frame_saida.winfo_children():
        wigets_edit.destroy()

    check_var = customtkinter.StringVar()

    for item in items:
        box = customtkinter.CTkCheckBox(scrollable_frame_saida, text=item, onvalue=item, offvalue="",
                                        variable=check_var,
                                        command=lambda: ler_dados_produto_selecionado(check_var, scrollable_frame_saida) if check_var.get() else apagar_entradas_produto_desmarcado(scrollable_frame_saida))
        box.pack(pady=0, padx=10, fill="x")


def ler_dados_produto_selecionado(arg_item, arg_frame):
    nome_produto = arg_item.get().strip("('),")
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT * FROM itens WHERE nome = '{nome_produto}'")
    dados_produto = terminal_sql.fetchall()
    if arg_frame == scrollable_frame_editar:
        entrada_editar_nome_produto.insert(0, dados_produto[0][0])
        entrada_editar_preco.insert(0, dados_produto[0][1])
        caixa_editar_texto.insert(0.0, dados_produto[0][2])
    elif arg_frame == scrollable_frame_entrada:
        entrada_nome_quantidade.insert(0, dados_produto[0][0])
    elif arg_frame == scrollable_frame_saida:
        entrada_nome_qtde.insert(0, dados_produto[0][0])
    else:
        pass


#fim config botão cancelar

def apagar_entradas_produto_desmarcado(arg_frame):
    if arg_frame == scrollable_frame_editar:
        entrada_editar_nome_produto.delete(0,tk.END)
        entrada_editar_preco.delete(0, tk.END)
        caixa_editar_texto.delete("1.0", tk.END)

        #Desmarca o checkbox
        for wigets_edit in scrollable_frame_editar.winfo_children():
            if isinstance(wigets_edit, customtkinter.CTkCheckBox):
                wigets_edit.deselect()

    elif arg_frame == scrollable_frame_entrada:
        entrada_nome_quantidade.delete(0, tk.END)
        entrada_qtde_adicionada.delete(0, tk.END)
        for wigets_edit in scrollable_frame_entrada.winfo_children():
            if isinstance(wigets_edit, customtkinter.CTkCheckBox):
                wigets_edit.deselect()

    elif arg_frame == scrollable_frame_saida:
        entrada_qtde_retirada.delete(0, tk.END)
        entrada_nome_qtde.delete(0, tk.END)
        for wigets_edit in scrollable_frame_saida.winfo_children():
            if isinstance(wigets_edit, customtkinter.CTkCheckBox):
                wigets_edit.deselect()

    elif arg_frame == frame_cadastrar:
        entrada_cadastrar_preco.delete(0, tk.END)
        entrada_cadastrar_nome_produto.delete(0, tk.END)
        caixa_texto_cadastrar_descricao.delete("1.0", tk.END)


    else:
        pass


def excluir_dados_produto_selecionado(bessa):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM itens WHERE nome = '{bessa}'")
    conexao.commit()
    conexao.close()
    entrada_editar_nome_produto.delete(0, "end")
    entrada_editar_preco.delete(0, "end")
    caixa_editar_texto.delete(0.0, "end")
    produtos_dados()

def atualizar_dados_produto_selecionado():
    produto_selecionado = check_var.get().strip("(',)")
    print(produto_selecionado)
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"UPDATE itens SET nome = '{entrada_editar_nome_produto.get()}', preco = '{entrada_editar_preco.get()}', descricao = '{caixa_editar_texto.get(0.0, 'end')}' WHERE nome = '{produto_selecionado}'")
    conexao.commit()
    conexao.close()
    entrada_editar_nome_produto.delete(0, "end")
    entrada_editar_preco.delete(0, "end")
    caixa_editar_texto.delete(0.0, "end")
    produtos_dados()

def cancelar_dados_produto_selecionado():
    entrada_cadastrar_nome_produto.delete(0, tk.END)
    entrada_cadastrar_preco.delete(0, tk.END)
    caixa_texto_cadastrar_descricao.delete('1.0', tk.END)
    produtos_dados()


def adicionar_item_entrada():
    nome_produto = entrada_nome_quantidade.get().strip()
    qtde_adicionada = entrada_qtde_adicionada.get().strip()

    if not nome_produto or not qtde_adicionada:
        showinfo("Aviso", "Preencha todos os campos!")
        return

    try:
        qtde = int(qtde_adicionada)
        if qtde <= 0:
            showinfo("Aviso", "A quantidade deve ser maior que zero!")
            return
    except ValueError:
        showinfo("Aviso", "Quantidade inválida!")
        return

    # Adiciona o item à lista de entrada
    item_texto = f"{nome_produto} - +{qtde} unidades"

    # Verifica se já existe na lista para atualizar a quantidade
    for child in frame_scroll3.winfo_children():
        if isinstance(child, customtkinter.CTkLabel) and nome_produto in child.cget("text"):
            existing_text = child.cget("text")
            existing_qtde = int(existing_text.split("+")[1].split()[0])
            new_qtde = existing_qtde + qtde
            child.configure(text=f"{nome_produto} - +{new_qtde} unidades")
            break
    else:
        # Se não existir, cria novo item
        x = len(frame_scroll3.winfo_children()) // 2 + 1  # Divide por 2 porque temos label + botão para cada item

        label = customtkinter.CTkLabel(frame_scroll3, text=item_texto)
        label.grid(row=x, column=0, pady=5, padx=0)

        botao_remover = customtkinter.CTkButton(frame_scroll3, text="🗑️", width=5,
                                                command=lambda l=label, b=None: remover_item_entrada(l, b))
        botao_remover.grid(row=x, column=3, columnspan=3, pady=5, padx=0)

    # Limpa os campos
    entrada_qtde_adicionada.delete(0, tk.END)

def remover_item_entrada(label, botao):
    label.destroy()
    if botao:
        botao.destroy()


def adicionar_item_saida():
    global saida_produtos
    nome_produto = entrada_nome_qtde.get().strip()
    qtde_adicionada = entrada_qtde_retirada.get().strip()

    if not nome_produto or not qtde_retirada:
        showinfo("Aviso", "Preencha todos os campos!")
        return

    try:
        qtde = int(qtde_retirada)
        if qtde <= 0:
            showinfo("Aviso", "A quantidade deve ser maior que zero!")
            return
    except ValueError:
        showinfo("Aviso", "Quantidade inválida!")
        return

    # Verifica se o produto já está na lista
    encontrado = False
    for i, item in enumerate(saida_produtos):
        if item['nome'] == nome_produto:
            saida_produtos[i]['quantidade'] += qtde
            encontrado = True
            break

    if not encontrado:
        # Adiciona novo item ao vetor
        saida_produtos.append({
            'nome': nome_produto,
            'quantidade': qtde
        })


    # Atualiza a exibição na interface
    atualizar_lista_saida()

    # Limpa o campo de quantidade
    entrada_qtde_retirada.delete(0, tk.END)

# Função para atualizar a exibição na interface de saída
def atualizar_lista_saida():
    # Limpa todos os widgets do frame_scroll4
    for widget in frame_scroll4.winfo_children():
        widget.destroy()

        # Adiciona cada item do vetor à interface
        for i, item in enumerate(saida_produtos):
            label = customtkinter.CTkLabel(frame_scroll4, text=f"{item['nome']} - -{item['quantidade']} unidades")
            label.grid(row=i, column=0, pady=5, padx=0, sticky="w")

            botao_remover = customtkinter.CTkButton(
                frame_scroll4,
                text="🗑️",
                width=5,
                command=lambda idx=i: remover_item_saida(idx)
            )
            botao_remover.grid(row=i, column=1, pady=5, padx=5)


    # Modifique a função remover_item_saida para trabalhar com o vetor
def remover_item_saida(indice):
    global saida_produtos
    if 0 <= indice < len(saida_produtos):
        saida_produtos.pop(indice)
        atualizar_lista_saida()

    # Adiciona o item à lista de saida
    item_texto = f"{nome_produto}  =  + {qtde} unidades"

    # Verifica se já existe na lista para atualizar a quantidade
    for child in frame_scroll4.winfo_children():
        if isinstance(child, customtkinter.CTkLabel) and nome_produto in child.cget("text"):
            existing_text = child.cget("text")
            existing_qtde = int(existing_text.split("+")[1].split()[0])
            new_qtde = existing_qtde + qtde
            child.configure(text=f"{nome_produto} - +{new_qtde} unidades")
            break
    else:
        # Se não existir, cria novo item
        x = len(frame_scroll4.winfo_children()) // 2 + 1  # Divide por 2 porque temos label + botão para cada item

        label = customtkinter.CTkLabel(frame_scroll4, text=item_texto)
        label.grid(row=x, column=0, pady=5, padx=0)

        botao_remover = customtkinter.CTkButton(frame_scroll4, text="🗑️", width=5,
                                                command=lambda l=label, b=None: remover_item_saida(l, b))
        botao_remover.grid(row=x, column=3, columnspan=3, pady=5, padx=0)

    # Limpa os campos
    entrada_qtde_retirada.delete(0, tk.END)

def remover_item_saida(label, botao):
    label.destroy()
    if botao:
        botao.destroy()



def salvar_entrada():
    # Implemente a lógica para salvar no banco de dados
    showinfo("Sucesso", "Entrada de produtos salva com sucesso!")

    # Limpa a lista após salvar
    for child in frame_scroll3.winfo_children():
        child.destroy()

    # Limpa os campos
    entrada_nome_quantidade.delete(0, tk.END)
    entrada_qtde_adicionada.delete(0, tk.END)


# função abrir
def abrir_frame_cadastrar():
    # fecha frame
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    # abre frame
    frame_cadastrar.grid_propagate(False)
    frame_cadastrar.grid(row=0, column=1, padx=5, pady=5)


def abrir_frame_editar():
    # fecha frame
    frame_cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    # abre frame
    frame_editar.grid_propagate(False)
    frame_editar.grid(row=0, column=1, padx=5, pady=5)
    produtos_dados()



def abrir_frame_saida():
    # fecha frame
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    # abre frame
    frame_saida.grid_propagate(False)
    frame_saida.grid(row=0, column=1, padx=5, pady=5)
    produtos_dados_saida()



def abrir_frame_entrada():
    # fecha frame
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_saida.grid_forget()
    # abre frame
    frame_entrada.grid_propagate(False)
    frame_entrada.grid(row=0, column=1, padx=5, pady=5)
    produtos_dados_entrada()




def abrir_frame_relatorio():
    # fecha frame
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()

    # abre frame
    frame_relatorio.grid_propagate(False)
    frame_relatorio.grid(row=0, column=1, padx=5, pady=5)
    # atualizar()

    ler_dados()


def abrir_frame_relatorio_entrada():
    # fecha frame
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_saida.grid_forget()

    # abre frame
    frame_relatorio_entrada.grid_propagate(False)
    frame_relatorio_entrada.grid(row=0, column=1, padx=5, pady=5)


def abrir_frame_relatorio_saida():
    # Fecha frame
    frame_cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio.grid_forget()
    frame_relatorio_entrada.grid_forget()
    # abre frame
    frame_relatorio_saida.grid_propagate(False)
    frame_relatorio_saida.grid(row=0, column=1, padx=5, pady=5)




popup = None


def abrir_popup():
    global popup
    if popup is None or not popup.winfo_exists():
        popup = customtkinter.CTkToplevel()
        popup.geometry("600x400")
        popup.title("popup")

        label = customtkinter.CTkLabel(popup, text="Popup", font=("Arial", 18, "bold"), text_color="white")
        label.grid(pady=0, padx=0, column=0, row=0, columnspan=4,
                   sticky="nsew")  # dentro do if pq ele so vai aparecer quando o popup tiver aberto

        label_relatorio = customtkinter.CTkLabel(popup, text="Escolher relatório(s):")
        label_relatorio.grid(row=1, column=0, pady=20, padx=20, sticky="w")

        exportar_estoque = customtkinter.CTkCheckBox(popup, text="Exportar Estoque")
        exportar_estoque.grid(row=2, column=0, pady=20, padx=20, sticky="w")

        exportar_saida = customtkinter.CTkCheckBox(popup, text="Exportar Saída")
        exportar_saida.grid(row=3, column=0, pady=20, padx=20, sticky="w")

        exportar_entrada = customtkinter.CTkCheckBox(popup, text="Exportar Entrada")
        exportar_entrada.grid(row=4, column=0, pady=20, padx=20, sticky="w")

        # titulo escolher extensão

        label_extencao = customtkinter.CTkLabel(popup, text="Escolher extensão:")
        label_extencao.grid(row=1, column=2, pady=20, padx=100, sticky="w")

        # Caixas para formatos de arquivo
        formato_word = customtkinter.CTkCheckBox(popup, text="Word")
        formato_word.grid(row=2, column=2, pady=20, padx=100, sticky="w")

        formato_pdf = customtkinter.CTkCheckBox(popup, text="PDF")
        formato_pdf.grid(row=3, column=2, pady=20, padx=100, sticky="w")

        formato_excel = customtkinter.CTkCheckBox(popup, text="Excel")
        formato_excel.grid(row=4, column=2, pady=20, padx=100, sticky="w")

        # botoes

        salvar_popup = customtkinter.CTkButton(popup, text="✔Salvar", width=100)
        salvar_popup.grid(row=5, column=2, pady=50, padx=20)

        cancelar_popup = customtkinter.CTkButton(popup, text="❌cancelar", fg_color="Red", width=100)
        cancelar_popup.grid(row=5, column=1, pady=50, padx=20)

        popup.protocol("WM_DELETE_WINDOW", fechar_popup)
        popup.attributes("-topmost", 1)  # garante que propup fica na frente
    else:
        popup.lift()


# noinspection PyUnresolvedReferences
def fechar_popup():
    global popup
    if popup is not None:
        popup.destroy()
        popup = None


# aparência
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# janela e título
janela = customtkinter.CTk()
janela.title("Sistema de Gerenciamento")
janela.geometry("800x400")

# frame_menu_SystemPy


frame_SystemPy = customtkinter.CTkFrame(janela, width=190, height=390, corner_radius=7)
frame_SystemPy.pack_propagate(False)
frame_SystemPy.grid(row=0, column=0, padx=5, pady=5)

frame_cadastrar = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_cadastrar.grid_propagate(False)
frame_cadastrar.grid(row=0, column=1, padx=5, pady=5)

frame_editar = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_editar.grid_propagate(False)

frame_saida = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_saida.grid_propagate(False)

frame_entrada = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_entrada.grid_propagate(False)

frame_relatorio = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_relatorio.grid_propagate(False)

frame_relatorio_saida = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_relatorio_saida.grid_propagate(False)

frame_relatorio_entrada = customtkinter.CTkFrame(janela, width=590, height=390, corner_radius=7)
frame_relatorio_entrada.grid_propagate(False)

# widgets menu system py

titulo_system_py = customtkinter.CTkLabel(frame_SystemPy, text="System Py", font=("Arial", 20, "bold"))
titulo_system_py.pack(pady=50)

botao_cadastrar = customtkinter.CTkButton(frame_SystemPy, text="Cadastrar", command=abrir_frame_cadastrar)
botao_cadastrar.pack()

botao_editar = customtkinter.CTkButton(frame_SystemPy, text="Editar", command=abrir_frame_editar)
botao_editar.pack(pady=10)

botao_saida = customtkinter.CTkButton(frame_SystemPy, text="Saida", command=abrir_frame_saida)
botao_saida.pack()

botao_entrada = customtkinter.CTkButton(frame_SystemPy, text="Entrada", command=abrir_frame_entrada)
botao_entrada.pack(pady=10)

botao_relatorio = customtkinter.CTkButton(frame_SystemPy, text="Relatório", command=abrir_frame_relatorio)
botao_relatorio.pack()

# widgets frame_cadastro
titulo_cadastrar_produto = customtkinter.CTkLabel(frame_cadastrar, text="Cadastro de Produto",
                                                  font=("Arial", 20, "bold"))
titulo_cadastrar_produto.grid(row=0, column=1, pady=20)

texto_cadastrar_nome_produto = customtkinter.CTkLabel(frame_cadastrar, text="Nome do Produto:")
texto_cadastrar_nome_produto.grid(row=1, column=0, padx=10, sticky="e")

texto_cadastrar_preco = customtkinter.CTkLabel(frame_cadastrar, text="Preço (R$):")
texto_cadastrar_preco.grid(row=2, column=0, padx=10, sticky="e")



# fim do formulário

texto_cadastrar_descricao = customtkinter.CTkLabel(frame_cadastrar, text="Descrição:")
texto_cadastrar_descricao.grid(row=3, column=0, padx=10, sticky="ne")

entrada_cadastrar_nome_produto = customtkinter.CTkEntry(frame_cadastrar, width=300,
                                                        placeholder_text="Digite o Nome do Produto")
entrada_cadastrar_nome_produto.grid(row=1, column=1, padx=10, sticky="w")

entrada_cadastrar_preco = customtkinter.CTkEntry(frame_cadastrar, width=80, placeholder_text="0.00")
entrada_cadastrar_preco.grid(row=2, column=1, pady=5, padx=10, sticky="w")

caixa_texto_cadastrar_descricao = customtkinter.CTkTextbox(frame_cadastrar, width=300, height=80)
caixa_texto_cadastrar_descricao.grid(row=3, column=1, padx=10, sticky="w")

botao_cadastrar_cancelar = customtkinter.CTkButton(frame_cadastrar, text="❌Cancelar", width=80, command=lambda : apagar_entradas_produto_desmarcado(frame_cadastrar))
botao_cadastrar_cancelar.grid(row=4, column=1, padx=10, pady=10, sticky="w")


botao_cadastrar_salvar = customtkinter.CTkButton(frame_cadastrar, text="✔Salvar", width=80, command=salvar_dados)
botao_cadastrar_salvar.grid(row=4, column=1, padx=10, pady=10, sticky="e")

# widget frame_editar

titulo_editar_produto = customtkinter.CTkLabel(frame_editar, text="Editar Produto Cadastrado",
                                               font=("Arial", 20, "bold"))
titulo_editar_produto.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

scrollable_frame_editar = customtkinter.CTkScrollableFrame(frame_editar)
scrollable_frame_editar.grid(row=2, column=0, padx=10, pady=10, sticky="w", rowspan=4)

entrada_editar_nome_produto = customtkinter.CTkEntry(frame_editar, width=300, placeholder_text="Nome do Produto")
entrada_editar_nome_produto.grid(row=2, column=1, padx=10, pady=5, sticky="w", columnspan=3)

entrada_editar_preco = customtkinter.CTkEntry(frame_editar, width=80, placeholder_text="0.00")
entrada_editar_preco.grid(row=3, column=1, pady=5, padx=10, sticky="w", columnspan=3)

caixa_editar_texto = customtkinter.CTkTextbox(frame_editar, width=300, height=80)
caixa_editar_texto.grid(row=4, column=1, padx=10, pady=5, sticky="w", columnspan=3)

entrada_editar_buscar_produto = customtkinter.CTkEntry(frame_editar, width=220, placeholder_text="Buscar Produto")
entrada_editar_buscar_produto.grid(row=1, column=0, padx=10, pady=5, sticky="w", columnspan=4)

botao_editar_excluir = customtkinter.CTkButton(frame_editar, text="🗑️Excluir", width=85, fg_color="Red",
                                               hover_color="#2f394a", command=lambda : excluir_dados_produto_selecionado(entrada_editar_nome_produto.get()))
botao_editar_excluir.grid(row=5, column=1, padx=10, pady=10, sticky="w")

botao_editar_cancelar = customtkinter.CTkButton(frame_editar, text="❌Cancelar", width=80, command=lambda : apagar_entradas_produto_desmarcado(scrollable_frame_editar))
botao_editar_cancelar.grid(row=5, column=2, padx=10, pady=10)

botao_editar_salvar = customtkinter.CTkButton(frame_editar, text="✔Salvar", width=80, command=lambda : atualizar_dados_produto_selecionado())
botao_editar_salvar.grid(row=5, column=3, padx=10, pady=10, sticky="e")

# widget frame_saida
scrollable_frame_saida = customtkinter.CTkScrollableFrame(frame_saida)
scrollable_frame_saida.grid(row=3, column=0, padx=10, pady=5, sticky="w", rowspan=2)

# configurando a lixeira

frame_scroll4 = customtkinter.CTkScrollableFrame(frame_saida, width=300, height=80)
frame_scroll4.grid_columnconfigure(2, weight=1)
frame_scroll4.grid(row=3, column=1, padx=10, pady=5, stick="w", columnspan=2)
items = []
for i in items:
    x += 1
    box = customtkinter.CTkLabel(frame_scroll4, text=i)
    box.grid(row=x, column=0, pady=5, padx=0)
x = 0
for i in items:
    y += 1
    box = customtkinter.CTkButton(frame_scroll4, text="🗑️", width=5)
    box.grid(row=y, column=3, columnspan=3, pady=5, padx=0)
y = 0

texto_saida_produto = customtkinter.CTkLabel(frame_saida, text="Saída de Produto", font=("Arial", 20, "bold"))
texto_saida_produto.grid(row=0, column=1, padx=10, columnspan=2)

entrada_qtde_retirada = customtkinter.CTkEntry(frame_saida, width=120, placeholder_text="Qtde a ser retirada")
entrada_qtde_retirada.grid(row=2, column=1, padx=10, pady=0, sticky="w", columnspan=2)

entrada_nome_qtde = customtkinter.CTkEntry(frame_saida, width=320, placeholder_text="Nome e Qtde")
entrada_nome_qtde.grid(row=1, column=1, padx=10, pady=20, columnspan=2)

entrada_nome_buscar = customtkinter.CTkEntry(frame_saida, width=220, placeholder_text="Buscar")
entrada_nome_buscar.grid(row=1, column=0, padx=10, sticky="w", columnspan=2)

botao_cancelar = customtkinter.CTkButton(frame_saida, text="❌Cancelar", fg_color="Red", width=80, command=lambda : apagar_entradas_produto_desmarcado(scrollable_frame_saida))
botao_cancelar.grid(row=5, column=1, padx=10, pady=10, stick="w")

botao_salvar = customtkinter.CTkButton(frame_saida, text="☑Salvar", width=80)
botao_salvar.grid(row=5, column=2, padx=10, pady=10, columnspan=2, sticky="e")

botao_adicionar_item = customtkinter.CTkButton(frame_saida, text="➕Adicionar item", width=120, command=adicionar_item_saida)
botao_adicionar_item.grid(row=2, column=1, padx=10, pady=0, columnspan=2, sticky="e")

# adicionando produto frame saida



# widget frame_entrada

scrollable_frame_entrada = customtkinter.CTkScrollableFrame(frame_entrada)
scrollable_frame_entrada.grid(row=3, column=0, padx=10, pady=5, sticky="w", rowspan=2)


# Adicionar estas funções para gerenciar a entrada de produtos


# adicionando produto

frame_scroll3 = customtkinter.CTkScrollableFrame(frame_entrada, width=300, height=80)
frame_scroll3.grid_columnconfigure(2, weight=1)
frame_scroll3.grid(row=3, column=1, padx=10, pady=5, stick="w", columnspan=2)
items = []
for i in items:
    x += 1
    box = customtkinter.CTkLabel(frame_scroll3, text=i)
    box.grid(row=x, column=0, pady=5, padx=0)
x = 0
for i in items:
    y += 1
    box = customtkinter.CTkButton(frame_scroll3, text="🗑️", width=5)
    box.grid(row=y, column=3, columnspan=3, pady=5, padx=0)
y = 0

texto_entrada_produto = customtkinter.CTkLabel(frame_entrada, text="Entrada de Produto", font=("Arial", 20, "bold"))
texto_entrada_produto.grid(row=0, column=1, padx=10, columnspan=2)

entrada_qtde_adicionada = customtkinter.CTkEntry(frame_entrada, width=140, placeholder_text="Qtde a ser adicionada")
entrada_qtde_adicionada.grid(row=2, column=1, padx=10, pady=0, sticky="w", columnspan=2)

entrada_nome_quantidade = customtkinter.CTkEntry(frame_entrada, width=320, placeholder_text="Nome e Qtde")
entrada_nome_quantidade.grid(row=1, column=1, padx=10, pady=20, columnspan=2)

entrada_buscar = customtkinter.CTkEntry(frame_entrada, width=220, placeholder_text="Buscar")
entrada_buscar.grid(row=1, column=0, padx=10, sticky="w", columnspan=2)

# Substitua estas linhas no frame_entrada:
botao_adicionar_item_entrada = customtkinter.CTkButton(frame_entrada, text="➕Adicionar item", width=120,
                                                     command=adicionar_item_entrada)
botao_adicionar_item_entrada.grid(row=2, column=1, padx=10, pady=0, columnspan=2, sticky="e")

botao_salvar_entrada = customtkinter.CTkButton(frame_entrada, text="☑Salvar", width=80,
                                             command=salvar_entrada)
botao_salvar_entrada.grid(row=5, column=2, padx=10, pady=10, columnspan=2, sticky="e")


botao_cancelar_entrada = customtkinter.CTkButton(frame_entrada, text="❌Cancelar", fg_color="Red", width=80, command=lambda : apagar_entradas_produto_desmarcado(scrollable_frame_entrada))
botao_cancelar_entrada.grid(row=5, column=1, padx=10, pady=10, stick="w")



# widget frame_relatorio - inicio

texto_relatorio = customtkinter.CTkLabel(frame_relatorio, text="Relatório de Estoque", font=("Arial", 20, "bold"))
texto_relatorio.grid(row=0, column=0, padx=0, columnspan=4)

entrada_buscar_produto_relatorio = customtkinter.CTkEntry(frame_relatorio, width=220, placeholder_text="Buscar Produto")
entrada_buscar_produto_relatorio.grid(row=1, column=0, padx=0, pady=10, sticky="w")

botao_estoque_relatorio = customtkinter.CTkButton(frame_relatorio, text="Estoque", width=80,
                                                  command=abrir_frame_relatorio)
botao_estoque_relatorio.grid(row=3, column=1, padx=0, pady=10, sticky="w")

botao_saida_relatorio = customtkinter.CTkButton(frame_relatorio, text="Saída", width=80,
                                                command=abrir_frame_relatorio_saida)
botao_saida_relatorio.grid(row=3, column=2, padx=0, pady=10)

botao_entrada_relatorio = customtkinter.CTkButton(frame_relatorio, text="Entrada", width=80,
                                                  command=abrir_frame_relatorio_entrada)
botao_entrada_relatorio.grid(row=3, column=3, padx=0, pady=10, sticky="e")

botao_exportar_entrada = customtkinter.CTkButton(frame_relatorio, text="Exportar", fg_color="green", width=80,
                                                 command=abrir_popup)
botao_exportar_entrada.grid(row=1, column=3, padx=0, pady=10, sticky="e")

# tabela frame_relatorio(estoque - associado)
columns = ('Nome', 'Quantidade', 'Preço(R$)', 'Descrição')
tree_estoque = ttk.Treeview(frame_relatorio, columns=columns, show='headings')
# define headings
tree_estoque.heading('Nome', text='Nome')
tree_estoque.heading('Quantidade', text='Quantidade')
tree_estoque.heading('Preço(R$)', text='Preço(R$)')
tree_estoque.heading('Descrição', text='Descrição')
tree_estoque.column('Nome', width=100)
tree_estoque.column('Quantidade', width=70)
tree_estoque.column('Preço(R$)', width=100)
tree_estoque.column('Descrição', width=280)

barra_scroll_estoque = ttk.Scrollbar(frame_relatorio, orient=tk.VERTICAL, command=tree_estoque.yview)
tree_estoque.config(yscroll=barra_scroll_estoque.set)
barra_scroll_estoque.grid(row=2, column=4, sticky='nsw')

tree_estoque.grid(row=2, column=0, padx=0, pady=10, columnspan=4)

# widget frame_relatorio - fim


# widget frame_relatorio_entrada - inicio

texto_relatorio_entrada = customtkinter.CTkLabel(frame_relatorio_entrada, text="Relatório de Entrada",
                                                 font=("Arial", 20, "bold"))
texto_relatorio_entrada.grid(row=0, column=0, padx=0, columnspan=4)

entrada_buscar_produto_entrada = customtkinter.CTkEntry(frame_relatorio_entrada, width=220,
                                                        placeholder_text="Buscar Produto")
entrada_buscar_produto_entrada.grid(row=1, column=0, padx=0, pady=10, sticky="w")

botao_estoque_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Estoque", width=80,
                                                command=abrir_frame_relatorio)
botao_estoque_entrada.grid(row=3, column=1, padx=0, pady=10, sticky="w")

botao_saida_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Saída", width=80,
                                              command=abrir_frame_relatorio_saida)
botao_saida_entrada.grid(row=3, column=2, padx=0, pady=10)

botao_entrada_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Entrada", width=80,
                                                command=abrir_frame_relatorio_entrada)
botao_entrada_entrada.grid(row=3, column=3, padx=0, pady=10, sticky="e")

botao_exportar_entrada = customtkinter.CTkButton(frame_relatorio_entrada, text="Exportar", fg_color="green", width=80,
                                                 command=abrir_popup)
botao_exportar_entrada.grid(row=1, column=3, padx=0, pady=10, sticky="e")

# tabela frame_relatorio_entrada
columns = ('Nome', 'Quantidade', 'Data/hora')
tree_entrada = ttk.Treeview(frame_relatorio_entrada, columns=columns, show='headings')

# define headings
tree_entrada.heading('Nome', text='Nome')
tree_entrada.heading('Quantidade', text='Quantidade')
tree_entrada.heading('Data/hora', text='Data/hora')
tree_entrada.column('Nome', width=184)
tree_entrada.column('Quantidade', width=182)
tree_entrada.column('Data/hora', width=184)

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'item {n}', f'{aleatorio[n]}', f'28/02/2025'))
# add data to the treeview
for contact in contacts:
    tree_entrada.insert('', tk.END, values=contact)

tree_entrada.grid(row=2, column=0, padx=0, pady=10, columnspan=4)
# tree.grid(row=0, column=0, sticky='nsew')


# add a scrollbar
barra_scroll_entrada = ttk.Scrollbar(frame_relatorio_entrada, orient=tk.VERTICAL, command=tree_entrada.yview)
tree_entrada.configure(yscroll=barra_scroll_entrada.set)
barra_scroll_entrada.grid(row=2, column=4, sticky='nsw')

# widget frame_relatorio_entrada - fim

# widget frame_relatorio_saida - inicio

texto_relatorio_saida = customtkinter.CTkLabel(frame_relatorio_saida, text="Relatório de Saída",
                                               font=("Arial", 20, "bold"))
texto_relatorio_saida.grid(row=0, column=0, padx=0, columnspan=4)

entrada_buscar_produto_saida = customtkinter.CTkEntry(frame_relatorio_saida, width=220,
                                                      placeholder_text="Buscar Produto")
entrada_buscar_produto_saida.grid(row=1, column=0, padx=0, pady=10, sticky="w")

botao_estoque_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Estoque", width=80,
                                              command=abrir_frame_relatorio)
botao_estoque_saida.grid(row=3, column=1, padx=0, pady=10, sticky="w")

botao_saida_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Saída", width=80,
                                            command=abrir_frame_relatorio_saida)
botao_saida_saida.grid(row=3, column=2, padx=0, pady=10)

botao_entrada_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Entrada", width=80,
                                              command=abrir_frame_relatorio_entrada)
botao_entrada_saida.grid(row=3, column=3, padx=0, pady=10, sticky="e")

botao_exportar_saida = customtkinter.CTkButton(frame_relatorio_saida, text="Exportar", fg_color="green", width=80,
                                               command=abrir_popup)
botao_exportar_saida.grid(row=1, column=3, padx=0, pady=10, sticky="e")

# tabela frame_relatorio_saida

columns = ('Nome', 'Quantidade', 'Data/hora')
tree_saida = ttk.Treeview(frame_relatorio_saida, columns=columns, show='headings')

# define headings
tree_saida.heading('Nome', text='Nome')
tree_saida.heading('Quantidade', text='Quantidade')
tree_saida.heading('Data/hora', text='Data/hora')
tree_saida.column('Nome', width=184)
tree_saida.column('Quantidade', width=182)
tree_saida.column('Data/hora', width=184)

# generate sample data
contacts = []
for n in range(1, 100):
    contacts.append((f'first {n}', f'{aleatorio2[n]}', f'email{n}@example.com'))
# add data to the treeview
for contact in contacts:
    tree_saida.insert('', tk.END, values=contact)

tree_saida.grid(row=2, column=0, padx=0, pady=10, columnspan=4)

# add a scrollbar
barra_scroll_saida = ttk.Scrollbar(frame_relatorio_saida, orient=tk.VERTICAL, command=tree_saida.yview)
tree_saida.configure(yscroll=barra_scroll_saida.set)
barra_scroll_saida.grid(row=2, column=4, sticky='nsw')


janela.mainloop()
