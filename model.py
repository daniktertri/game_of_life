import random

##cells data##
n,m = 50,50
matrix = [[random.choice([True,False])for e in range(m)] for e in range(n)]

##cam and screen data##
x_cam, y_cam = 0.3,0.7
width_cam, height_cam = 10,10
w_screen,h_screen = 806, 636