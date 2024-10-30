import tkinter as tk

janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e_email promocionais?", variable=var_promocoes)
checkbox_promocoes.grid(row=0,column=0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text="Aceitar termos de uso Políticas de Privacidade", variable=var_politicas)
checkbox_politicas.grid(row=1,column=0)

def enviar():
    if var_promocoes.get():
        print("Usuário deseja receber promoções")
    else:
        print("Usuário NÃO deseja receber promoções")
    if var_politicas.get():
        print("Usuário concordou com os termos de uso e póliticas de privacidade")
    else:
        print("Usuário NÃO concordou")


botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=1, column=0)

janela.mainloop()