import tkinter

janela = tkinter.Tk()
janela.geometry("700x400")
janela.config(background="blue")
Meulabel = tkinter.Label (janela, text= "olá pessaol, sejam bem- vindos!")
botao = tkinter.Button (janela, text = 'clique aqui')
botao.pack()


Meulabel.pack()

janela.mainloop()