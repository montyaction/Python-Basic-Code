import pygame as pg,sys
from pygame.locals import *
import time

# initialize global variables
OX = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
line_color = (10,10,10)

# Tic Tac Toe 3x3 boad
TTT = [[None]*3,[None]*3,[None]*3]