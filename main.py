import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting asteroids!")
    print("Screen width: "+str(SCREEN_WIDTH))
    print("Screen height: "+str(SCREEN_HEIGHT))

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000
        player.update(dt)

if __name__ == "__main__":
    main()
