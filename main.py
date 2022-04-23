from tkinter import *
import tkinter as tk

root = Tk()
matrix = [[0 for e in range(20)] for e in range(20)]

def whenPressed(button):
    button.configure(bg = "black")

def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if matrix[(pos[0] + i[0]) % len(matrix)][(pos[1] + i[1]) % len(matrix[0])]:
            count += 1
    return count


for i in range(20):
    for j in range(20):
        current_button = Button(root,
                               text = f" ",
                               font=("tahoma", 5, "bold"),
                               height = 1,
                               width = 1,
                               bg="gainsboro",
                               command = lambda: whenPressed(current_button))
        current_button.grid(row = i+1, column = j+1)
        matrix[i][j] = current_button
root.mainloop()

while True:
    near()
