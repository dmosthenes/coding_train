class TileCreator():

    def __init__(self, tile_directory):

        self.images = []

        # Load all the images from the directory


        # Loop over each image and create a dictionar of dictionaries
        # Containing the pixel average for each section of edge
        self.image_connections = {}

        for image in self.images:

            self.image_connections[image] = {}

            # Loop over top, right, bottom, left



        

class Tile():

    def __init__(self, image):

        self.tile = image
        self.width
        self.height

        # Scan the edges to get the colour for three sections of each edge




