from model import n,m,matrix,x_cam,y_cam,w_screen,h_screen,width_cam,height_cam
from view import canvas,root
from tkinter import *




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
             canvas.create_rectangle(x0_pix, y0_pix, x1_pix,y1_pix, fill= 'yellow', outline="black")
           else:
             canvas.create_rectangle(x0_pix, y0_pix, x1_pix,y1_pix, fill= 'white', outline="black")  




##fonction for bind##
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


##bind##
root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('=',plus)
root.bind('-',minus)
root.bind('<Button-1>',click)


update_screen()
mainloop()