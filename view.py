from tkinter import *
from model import w_screen,h_screen

##tkinter window##
root = Tk()
root.title("Game of life")
root.geometry(f'{w_screen}x{h_screen}')

##init canvas##
canvas = Canvas(root, bg = "white")
canvas.pack(fill="both",expand=True)