import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

data2 = {'Apuesta': [],
         'Saldo': []
        }
def graficar():
        df2 = DataFrame(data2,columns=['Apuesta','Saldo'])
        root= tk.Tk() 
        figure2 = plt.Figure(figsize=(5,4), dpi=100)
        ax2 = figure2.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure2, root)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        df2 = df2[['Apuesta','Saldo']].groupby('Apuesta').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('Promedio de Apuesta')
        root.mainloop()
