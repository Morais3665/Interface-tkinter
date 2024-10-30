import tkinter as tk

janela = tk.Tk()
var_aviao = tk.StringVar()

botao_economica = tk.Radiobutton(text="Classe Econômica", variable=var_aviao, value="Classe Econômica")
botao_executiva = tk.Radiobutton(text="Classe Executiva", variable=var_aviao, value="Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text="Primeira classe", variable=var_aviao, value="Primeira classe")
botao_economica.grid(row=0, column=0)
botao_executiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0, column=2)

def enviar():
    print(var_aviao.get())


botao_enviar = tk.Button(text="Enviar", command=enviar)
botao_enviar.grid(row=1, column=0)

tk.mainloop()