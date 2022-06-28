from tkinter import Tk,Button,Canvas 
import tkinter
from model import n,m,matrix,x_cam,y_cam,w_screen,h_screen,width_cam,height_cam

##tkinter##
root = Tk()
root.title("Game of life")
root.geometry(f'{w_screen}x{h_screen}')

##canvas##
canvas = Canvas(root, bg = "black")
canvas.pack(fill="both",expand=True)
