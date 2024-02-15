import pygame
import sys
from bird_and_pipe import Bird, Pipe
import random
import copy

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
    INTERVAL = 800

    # Start the timer
    timer = pygame.time.get_ticks()

    generation = 0

    # Outer while loop initialises each new generation
    while True:

        # Initialise game objects
        birds = {Bird(screen) for _ in range(2)}
        # birds = {Bird(screen)}
        dead_birds = set()
        pipes = [Pipe(screen)]

        # Store reference to the pipe closest to
        # and moving towards player
        current_pipe = pipes[0]
        bird_x_pos = copy.copy(birds).pop().x
        # max_pipe_dst = current_pipe.toplft[0] - bird_x_pos
        # print(max_pipe_dst)
        # TODO: Find a better way to calculate max distance to pipe
        max_pipe_dst = 120

        generation += 1

        # Count the number of pipes which have passed the player
        passed_pipes = 0

        # Inner while loop runs a given generation
        while birds:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(black)

            clock.tick(FPS)

            current_time = pygame.time.get_ticks()

            time_passed = current_time - timer        

            # Add a new pipe every second second
            if time_passed >= INTERVAL:
                timer = current_time
                pipes.append(Pipe(screen))

            # Update current pipe
            if current_pipe.toplft[0] <= bird_x_pos:
                current_pipe = pipes[1]
                # max_pipe_dst = current_pipe.toplft[0] - bird_x_pos
                passed_pipes += 1
                # print(max_pipe_dst)

                # Check if 0th pipe is offscreen
                if pipes[0].toplft[0] + pipes[0].width <= 0:
                    pipes = pipes[1:]

            # Draw all pipes
            for pipe in pipes:
                pipe.draw()
                pipe.update()

            for bird in copy.copy(birds):

                # Decide whether to jump
                bird.choice(current_pipe.toplft[0] - bird.x / max_pipe_dst,
                            current_pipe.gapy / height,
                            current_pipe.gapy + current_pipe.gapdst / height)


                # height = screen.get_height()
                # if bird.brain.predict(bird.y / height, 
                #                         bird.yvelocity / -15, 
                #                         current_pipe.toplft[0] - bird.x / max_pipe_dst,
                #                         current_pipe.gapy / height,
                #                         current_pipe.gapy + current_pipe.gapdst / height) >= 0.5:
            
                #     bird.jump()

                bird.update()
                bird.draw()

                # Check boundary and collision
                if bird.out_of_bounds() or bird.collides(current_pipe):
                    dead_birds.add(bird)
                    birds.remove(bird)
                    bird.set_score(passed_pipes)
        
            pygame.display.flip()


def main():
    
    run()

if __name__ == "__main__":
    main()