import pygame
import sys
import bird_and_pipe

def main():

    pygame.init()

    width = 400
    height = 400

    black = (0,0,0)

    FPS = 30
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set("flappy bird with neural net")

    # game objects
    player = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)


        # Add a pair of pipes at the start
        # And then every third second


if __name__ == "__main__":
    main()