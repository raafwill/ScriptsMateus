from skripts import baixando as b
from skripts import rotinas_relatórios as ro
from skripts import variaveis as v
import tkinter as tk
from tkinter import *
import sys

ro.previsao_estoque()

# root = tk.Tk()
# root.title("Extração de Arquivos")
# root.geometry("300x200")
# button_frame = tk.Frame(root)
# button_frame.pack(fill=tk.X, side=tk.BOTTOM)
#
# btn1 = tk.Button(button_frame, text="Previsão de Estoques", command=ro.previsao_estoque, fg="white", background="blue")
# btn2 = tk.Button(button_frame, text="Abrir GMCore", command=v.abrir_gmcore, fg="black", background="green")
# sair = tk.Button(button_frame, text="Sair", command=root.destroy, fg="red", background="white")
# credenciais = tk.Button(button_frame, text="Credenciais", command=v.acessar_credenciais, fg="yellow", background="black")
#
# button_frame.columnconfigure(0, weight=1)
# button_frame.columnconfigure(1, weight=1)
# button_frame.columnconfigure(2, weight=1)
#
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
# btn2.grid(row=1, column=0, sticky=tk.W+tk.E)
# sair.grid(row=3, column=0, sticky=tk.W+tk.E)
# credenciais.grid(row=2, column=0, sticky=tk.W+tk.E)
#
# root.mainloop()





