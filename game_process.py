from model import n,m,matrix,x_cam,y_cam,w_screen,h_screen,width_cam,height_cam
from view import root,canvas
import tkinter

##screen update##


def update_screen():
    global matrix
    for x in range(n):
        for y in range(m):
           x0_pix = (x - x_cam)* w_screen // width_cam
           y0_pix = (y - y_cam)* h_screen // height_cam
           
           x1_pix = ((x+1) - x_cam)* w_screen // width_cam
           y1_pix = ((y+1) - y_cam)* h_screen // height_cam           
           if matrix[x][y] == True:
             canvas.create_rectangle(x0_pix, y0_pix, x1_pix,y1_pix, fill= 'yellow', outline="grey")
           else:
             canvas.create_rectangle(x0_pix, y0_pix, x1_pix,y1_pix, fill= 'white', outline="grey")  

def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if matrix[(pos[0] + i[0]) % len(matrix)][(pos[1] + i[1]) % len(matrix[0])]:
            count += 1
    return count


def update_cells_neighbors():
    global matrix
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
    update_screen()


# Buttons command fonctions# 

def one_step_fc():
    update_cells_neighbors()      
def start_fc():
    update_cells_neighbors()
    root.after(700, start_fc)
def clear_fc():
    global matrix
    matrix2 = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    matrix = matrix2



##  fonction for bind     ##

def left(event):
  global x_cam
  if x_cam > 0:
    x_cam -= .2
  else:
      pass
  update_screen()

def right(event):
    global x_cam
    x_cam += .2
    update_screen()

def plus(event):
    global width_cam,height_cam
    if width_cam > 12:
      width_cam /= 1.2
      height_cam /= 1.2
    else: 
        pass
    update_screen()

def minus(event):
    global width_cam,height_cam
    if width_cam < 30:
      width_cam *= 1.2
      height_cam *= 1.2
    else:
        pass
    update_screen()

def click(event):
    x_pos = event.x * width_cam // w_screen + x_cam
    y_pos = event.y * height_cam // h_screen + y_cam

    if matrix[round(x_pos)][round(y_pos)]:
      matrix[round(x_pos)][round(y_pos)] = False
    else:
      matrix[round(x_pos)][round(y_pos)] = True
    update_screen()




##bind##
root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('=',plus)
root.bind('-',minus)
root.bind('<Button-1>',click)
root.bind('<Up>',update_cells_neighbors)
one_step = tkinter.Button(root, text ="One step", command = one_step_fc)
one_step.pack()
start_btn = tkinter.Button(root, text ="Start", command = start_fc)
start_btn.pack()
clear_btn = tkinter.Button(root, text ="Clear", command = clear_fc)
clear_btn.pack()



update_screen()
root.mainloop()