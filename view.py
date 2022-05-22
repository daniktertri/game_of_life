from tkinter import Tk,Canvas
from model import n,m,matrix,x_cam,y_cam,w_screen,h_screen,width_cam,height_cam

##tkinter window##
root = Tk()
root.title("Game of life")
root.geometry(f'{w_screen}x{h_screen}')

##init canvas##
canvas = Canvas(root, bg = "white")
canvas.pack(fill="both",expand=True)

