import pygame
from tile_and_board import Square, TileCreator, Board
import os
import copy

INTERLEAVING = False

# class Visualiser():

#     def init(self, width, height):
#         self.width = width
#         self.height = height

#         self.wfc = WaveFunctionCollapse()

#         self.viewer = pygame.init()

#     def draw(self):
#         # self.wfc.domains[]
#         return
    

class WaveFunctionCollapse():

    def __init__(self, tiles, width, height, numbered_tiles, board):

        self.tiles = tiles
        self.tile_width = numbered_tiles[0].width
        self.tile_height = numbered_tiles[0].height
        self.width = width * self.tile_width
        self.height = height * self.tile_height
        self.numbered_tiles = numbered_tiles
        self.board = board

        # Each square may have any of the tiles to begin with
        self.domains = {square : copy.deepcopy(self.tiles)
                        for square in board.squares}
        
        self.viewer = pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wave Function Collapse Visualisation")

        self.BLACK = (255, 255, 255)
        self.WHITE = (0, 0, 0)

    def run(self):

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill(self.BLACK)

            assignment = self.solve()

            if self.complete(assignment) is True:
                input("Close?")
                running = False
        
        pygame.quit()
        

    def update_window(self, assignment):

        # For each Square in the assignment dictionary, draw it to the screen
        for square, tile in assignment.items():

            self.window.blit(tile.image, square.x * tile.width, square.y * tile.height)


    def solve(self):
        """
        Enforce arc consistency, and solve the CSP.
        """

        assignment = {}

        # Make an initial random assignment in or around the middle
        middle_square = Square(self.width / 2, self.height / 2, self.width, self.height)
        assignment[middle_square] = self.domains[middle_square].pop()
        self.domains[middle_square] = assignment[middle_square]

        if not INTERLEAVING:
            self.backtrack(assignment)
        else:
            self.backtrack_with_interleaving(assignment)

        return assignment


    def ac3(self, cell_prime=None):
        """
        Update self.domains such that each cell is arc consistent.
        If cells is None, begin with all cells. Otherwise, use cells
        as the initial list of cells to make consistent.

        Returns True if arc consistency is enforced and no domains
        are empty. Return False if any domains end up empty.
        """
        return
    

    def revise(self, x):
        """
        Make node 'x' arc consistent with its neighbours.
        Returns True if revision occurs, otherwise False.

        Does not assign values even if only one in domain.
        """
        return
    

    def complete(self, assignment):
        """Returns True if assignment assigns a value to
        every Square on the Board. Otherwise, False."""

        # Check that each square in the domains dictionary maps to a tile.
        for square in self.domains:

            if square not in assignment or assignment[square] is set():
                return False

        return True
    

    def consistent(self, assignment):
        """
        Returns True if assignment has no conflicting
        tiles - though may be incomplete. Otherwise, False.
        """
        return
    

    def backtrack(self, assignment):
        """
        Perform backtracking search to return a complete assignment dictionary.
        """

        # Base case
        if self.complete(assignment) and self.consistent(assignment):
            return assignment
        
        # Update visualisation
        self.update_window(assignment)
        
        # Recursive bit


        return
    

    def backtrack_with_interleaving(self, assignment):
        """
        Perform backtracking serach with inferences to return a complete assignment
        dictionary.
        """

        # Base case
        if self.complete(assignment) and self.consistent(assignment):
            return assignment
        
        # Update visualisation
        self.update_window(assignment)

        
        return


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned Square not already assigned in assignment.
        Choose the cell with the minimum number of remaining values
        in its domain. In the case of a tie, choose randomly.
        """

        # Get dictionary of Squares not in assignment
        unassigned_list = [(square, len(self.domains[square]))
                            for square in self.domains if square not in assignment]

        return sorted(unassigned_list, key=lambda x: x[1])[0][0]
    

    def order_domain_values(self, square):
        """
        Return a list of values in the domain of Square sorted by the number
        of values they rule out for neighbouring Squares. The first value
        rules out the fewest values in neighbours.
        """

        sides = ["top", "right", "bottom", "left"]

        available_tiles = self.domains[square]
        neighbours = square.neighbours

        values = []

        for tile in available_tiles:

            total = 0

            # For each neighbour, consider how many tiles fit if the current tile was selected
            # Get the overlap of 

            for side in sides:

                possible_tiles = self.domains[Square((*neighbours[side]), self.width, self.height)]
                compat_tiles = tile.compatible_tiles[side]
                overlap = possible_tiles.intersection(compat_tiles)

                total += len(overlap)

            values.append((tile, total))

        # Return the sorted list
        return sorted(values, key=lambda x:x[1], reverse=True)



def main():

    width = 4
    height = 4

    # Create a TileCreator
    tile_maker = TileCreator(os.join("images", "polka"), width, height)
    tiles = tile_maker.generate_tiles()

    # Get tile numbers
    numbered_tiles = tile_maker.numbered_images

    # Initialise the board
    board = Board(width, height, tiles, numbered_tiles)

    wfc = WaveFunctionCollapse(tiles, width, height, numbered_tiles, board)

    wfc(tiles, width, height, numbered_tiles, board).run()



if __name__ == "__main__":
    main()


