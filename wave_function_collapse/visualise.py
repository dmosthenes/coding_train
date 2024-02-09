import pygame
import tile_and_board
import os
import copy

class Visualiser():

    def init(self, width, height):
        self.width = width
        self.height = height

        self.wfc = WaveFunctionCollapse()

        self.viewer = pygame.init()

    def draw():
        return
    

class WaveFunctionCollapse():

    def __init__(self, tiles, width, height, numbered_tiles, board):


        # Each square may have any of the tiles to begin with
        self.domains = {square : copy.deepcopy(self.tiles)
                        for square in board.squares}


    def solve(assignment):

        # Make an initial random assignment


        return
    
    def ac3():
        return
    
    def complete(assignment):
        return
    
    def consistent(assignment):
        return
    
    def backtrack(assignment):
        return
    
    def backtrack_with_interleaving(assignment):
        return
    
    def 




def main():

    width = 4
    height = 4

    # Create a TileCreator
    tile_maker = tile_and_board.TileCreator(os.join("images", "circuit-coding-train"), width, height)
    tiles = tile_maker.generate_tiles()

    # Initialise the board
    board = tile_and_board.Board()

    # Get tile numbers
    numbered_tiles = tile_maker.numbered_images

    visualise = Visualiser(width, height)

    assignments = {}




if __name__ == "__main__":
    main()


