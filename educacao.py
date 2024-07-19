import tkinter as tk
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

dados = pd.read_excel('dados1.xlsx')
DF=pd.DataFrame(dados)
disciplina = dados['DISC']
nota = dados['NOTAS']
freq = dados['FREQ']
comportamento = dados['COMPORTAMENTO']

janela = tk.Tk()
janela.geometry('250x180')
janela.title('ESCOLA')
texto = tk.Label(janela, text =  'NOTAS DO ALUNO')
texto.pack()

def pizza():
    plt.pie(nota, labels = disciplina)
    plt.legend(nota, loc="lower right")
    plt.show()

btn  =  tk.Button(janela, text='CLIQUE AQUI', command=pizza)
btn.pack()

janela.mainloop()