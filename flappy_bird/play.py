import pygame
import sys
from bird_and_pipe import Bird, Pipe
import random
import copy
import time

def run():

    pygame.init()

    width = 800
    height = 600

    black = (0,0,0)

    FPS = 30
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("flappy bird with neural net")

    # Set pipe generation interval
    INTERVAL = 45

    # Start the timer
    # timer = pygame.time.get_ticks()

    generation = 0

    # Outer while loop initialises each new generation
    while True:

        frame_counter = 0

        # Initialise game objects
        birds = [Bird(screen) for _ in range(1000)]
        # birds = [Bird(screen)]
        dead_birds = []
        pipes = []

        # Store reference to the pipe closest to
        # and moving towards player
        current_pipe = None
        bird_x_pos = copy.copy(birds).pop().x
        max_pipe_dst = screen.get_width() - bird_x_pos

        generation += 1

        # Count the number of pipes which have passed the player
        passed_pipes = 0

        # last_pipe_time = pygame.time.get_ticks()
        # current_time = last_pipe_time

        # Inner while loop runs a given generation
        while birds:

            frame_counter += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(black)

            clock.tick(FPS)

            # current_time = pygame.time.get_ticks()
            # time_since_last_pipe = current_time - last_pipe_time        

            # Add a new pipe every second second
            # if time_since_last_pipe >= INTERVAL:
            if frame_counter % INTERVAL == 0 or len(pipes) == 0:
                # last_pipe_time = current_time
                pipes.append(Pipe(screen))

            # Update current pipe
            if not current_pipe and len(pipes) > 0:
                current_pipe = pipes[0]

            elif not current_pipe:
                pass

            elif current_pipe.toplft[0] + current_pipe.width <= bird_x_pos:
                current_pipe = pipes[1]
                passed_pipes += 1

                # Check if 0th pipe is offscreen
                if pipes[0].toplft[0] + pipes[0].width <= 0:
                    pipes = pipes[1:]

            # Draw all pipes
            for pipe in pipes:
                pipe.draw()
                pipe.update()

            removed_birds = []

            for bird in copy.copy(birds):

                if current_pipe:

                    # Decide whether to jump
                    bird.choice(current_pipe.toplft[0] - bird.x / max_pipe_dst,
                                current_pipe.gapy / height,
                                current_pipe.gapy + current_pipe.gapdst / height)

                    # Check boundary and collision
                    if bird.out_of_bounds() or bird.collides(current_pipe):
                        removed_birds.append(bird)
                        birds.remove(bird)
                        bird.set_score(passed_pipes)
        
                bird.update()
                bird.draw()

            # Remove any dead birds
            for rm_bird in removed_birds:
                if rm_bird in birds:
                    birds.remove(rm_bird)
            
            dead_birds.extend(removed_birds)
                
            pygame.display.flip()


def main():
    time.sleep(3)
    run()

if __name__ == "__main__":
    main()