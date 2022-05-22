from tkinter import *
import random


root = Tk()
root.title("Game of life")
w_screen,h_screen = 806, 636

root.geometry(f'{w_screen}x{h_screen}')
canvas = Canvas(root, bg = "white")
canvas.pack(fill="both",expand=True)

n,m = 50,50
matrix = [[random.choice([True,False])]for e in range(m) for e in range(n)]
x_cam, y_cam = 0.3,0.7
width_cam, height_cam = 10,10

def update_screen():
    global matrix
    for x in range(n):
        for y in range(m):
           x0_pix = (x - x_cam)* w_screen // width_cam
           y0_pix = (y - y_cam)* h_screen // height_cam
           
           x1_pix = ((x+1) - x_cam)* w_screen // width_cam
           y1_pix = ((y+1) - y_cam)* h_screen // height_cam
           canvas.create_rectangle(x0_pix, y0_pix, x1_pix,y1_pix, fill= 'white', outline="black")   
#           if matrix[x][y] == True:
#             canvas.create_rectangle(x0_pix, y0_pix, x1_pix,y1_pix, fill= 'yellow', outline="black")
#           else:
            

update_screen()

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
    x_pos = None
    y_pos = None
root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('=',plus)
root.bind('-',minus)
root.bind('<Button-1>',click)

mainloop()