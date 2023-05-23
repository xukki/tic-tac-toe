# Modules
import random
import pygame
import sys
import copy
import numpy as np
from constants import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

class Board: #for interacting with back end 
    def __init__(self):
        self.squares = np.zeros((ROWS,COLS)) # makes a 2d list representing the grid 
    
    def mark_sqr(self, row , col, player): #allows marking a square
        self.squares[row][col] = player
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0
class Game:
    def __init__(self):
        self.showlines()
        self.board = Board()
        self.player = 1

    #makes the grid on the gui
    def showlines(self):
        #vertical
        pygame.draw.line(screen,LINE_COLOR, (SQSIZE,0),(SQSIZE,HEIGHT),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR, (2*SQSIZE,0),(2*SQSIZE,HEIGHT),LINE_WIDTH)
        #horizontal
        pygame.draw.line(screen,LINE_COLOR, (0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
        pygame.draw.line(screen,LINE_COLOR, (0,2*SQSIZE),(WIDTH,2*SQSIZE),LINE_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1 # p1 - X p2 - O

    def draw_fig(self,row,col):
        if self.player == 1:
            #draw cross
            #descending line
            start_desc = (col*SQSIZE + OFFSET, row*SQSIZE + OFFSET)
            end_desc = (col*SQSIZE + SQSIZE-OFFSET, row*SQSIZE + SQSIZE - OFFSET)
            #ascending line
            start_asc = (col*SQSIZE + OFFSET,row*SQSIZE + SQSIZE - OFFSET)
            end_asc = (col*SQSIZE +SQSIZE-OFFSET,row*SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
        elif self.player == 2:
            #draw circle
            center=(col*SQSIZE + SQSIZE // 2, row*SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen,CIRC_COLOR,center,RADIUS,CIRC_WIDTH)

def main():
    
    game = Game()
    board = game.board

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()  
              sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE # so that the coords are in terms of rows and collumns and not pixels
                col = pos[0] // SQSIZE
                
                if board.empty_sqr(row, col):
                    board.mark_sqr(row,col,game.player)
                    game.draw_fig(row,col)
                    game.next_turn()
                    
                    

        pygame.display.update()

main()

#Classes






