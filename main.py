from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import PIL
import random
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
matrix = [[random.choice([0,1]) for e in range(20)] for e in range(20)]
matrix2 = matrix
def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if matrix[(pos[0] + i[0]) % len(matrix)][(pos[1] + i[1]) % len(matrix[0])]:
            count += 1
    return count

def num():
    n1 = int(20)
    n2 = int(20)
    initBoard = np.zeros((n1, n2))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
               initBoard[i][j] = matrix[i][j] 
            else:
              initBoard[i][j] = matrix[i][j]
    ax.imshow(initBoard)
    canvas.draw_idle()

root = Tk()
root.title('Game of Life')
root.geometry('800x600')

fig = plt.figure()
ax = fig.add_subplot(111) 
ax.axis('off')
canvas = FigureCanvasTkAgg(fig, master=root)  
canvas.get_tk_widget().grid(row=4, column=0)


while True:
    num()
    mainloop()

    matrix2 = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j]:

                if near([i , j]) not in (2 , 3):
                    matrix2[i][j] = 0
                    continue

                matrix2[i][j] = 1
                continue

            if near([i , j]) == 3:
                matrix2[i][j] = 1
                continue

            matrix2[i][j] = 0
    matrix = matrix2
    print(1)