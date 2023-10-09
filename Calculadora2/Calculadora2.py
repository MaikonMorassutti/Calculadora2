import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(tk.END, result)
    except Exception as e:
        clear()
        entry.insert(tk.END, "Erro")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Entry para exibir a expressão
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda key=button: press(key) if key != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão de limpar
tk.Button(root, text="C", padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)

root.mainloop()

