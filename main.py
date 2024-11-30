import tkinter as tk
from tkinter import messagebox

# Lista global para armazenar os pedidos
pedidos = []

# Preços dos lanches e do refrigerante
precos = {
    "Hambúrguer": 10,
    "X-Burguer": 9,
    "X-Salada": 11,
    "X-Bacon": 14,
    "Vegano": 13,
    "Refrigerante": 4
}

def fazer_pedido():
    """Função chamada ao clicar no botão 'Realizar Pedido'."""
    nome_cliente = entrada_nome.get().strip()
    lanche_selecionado = lanche_var.get()
    refrigerante = refrigerante_var.get()
    entrega = entrega_var.get()
    
    if not nome_cliente or not lanche_selecionado:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha o nome do cliente e escolha um lanche.")
        return

    # Calculando o valor do pedido
    valor_lanche = precos[lanche_selecionado]
    valor_refrigerante = precos["Refrigerante"] if refrigerante else 0
    valor_total = valor_lanche + valor_refrigerante

    # Criando o resumo do pedido
    pedido_resumo = f"{nome_cliente} - {lanche_selecionado} - {'Refrigerante' if refrigerante else 'Sem Refrigerante'} - {'Entrega' if entrega == 'entrega' else 'Retirada no Local'} - R${valor_total:.2f}"
    
    # Adicionando o pedido à lista
    pedidos.append(pedido_resumo)

    # Atualiza a lista na interface
    atualizar_lista_pedidos()

    # Exibe mensagem de confirmação
    messagebox.showinfo("Pedido Realizado", f"Seu pedido foi realizado com sucesso!\nTotal: R${valor_total:.2f}")

def atualizar_lista_pedidos():
    """Atualiza a listagem dos pedidos realizados na interface."""
    # Limpa a lista anterior
    for widget in lista_pedidos_frame.winfo_children():
        widget.destroy()

    # Exibe os pedidos
    for pedido in pedidos:
        tk.Label(lista_pedidos_frame, text=pedido, anchor="w", width=60, justify="left").pack(pady=2)

# Janela principal
janela = tk.Tk()
janela.title("Lanchonete OSP")
janela.geometry("500x500")
janela.resizable(False, False)

# Nome do cliente
tk.Label(janela, text="Nome do Cliente:").pack(pady=5)
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack(pady=5)

# Escolha do lanche
tk.Label(janela, text="Escolha o Lanche:").pack(pady=5)
lanche_var = tk.StringVar(value=None)
lanches = ["Hambúrguer", "X-Burguer", "X-Salada", "X-Bacon", "Vegano"]
for lanche in lanches:
    tk.Radiobutton(janela, text=f"{lanche} - R${precos[lanche]:.2f}", variable=lanche_var, value=lanche).pack(anchor="w")

# Opção de refrigerante
tk.Label(janela, text="Deseja acompanhar refrigerante?").pack(pady=5)
refrigerante_var = tk.BooleanVar()
tk.Checkbutton(janela, text=f"Sim - R${precos['Refrigerante']:.2f}", variable=refrigerante_var).pack(anchor="w")

# Entrega ou retirada
tk.Label(janela, text="Forma de Retirada:").pack(pady=5)
entrega_var = tk.StringVar(value="retirada")
tk.Radiobutton(janela, text="Entrega", variable=entrega_var, value="entrega").pack(anchor="w")
tk.Radiobutton(janela, text="Retirada no Local", variable=entrega_var, value="retirada").pack(anchor="w")

# Botão para realizar pedido
botao_pedido = tk.Button(janela, text="Realizar Pedido", command=fazer_pedido)
botao_pedido.pack(pady=20)

# Frame para listagem dos pedidos
tk.Label(janela, text="Pedidos Realizados:").pack(pady=10)
lista_pedidos_frame = tk.Frame(janela)
lista_pedidos_frame.pack(pady=10)

# Inicia a aplicação
janela.mainloop()
