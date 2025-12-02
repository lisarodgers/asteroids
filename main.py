import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state 


def main():
    pygame.init()
   

    # REQUIRED BY BOOT.DEV TESTS:
    print("Starting Asteroids")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Load background image
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        # Draw the background
        screen.blit(background, (0, 0))

        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            # Player–asteroid collision (only if not invulnerable)
            if not player.invulnerable and player.collide(asteroid):
                player.lives -= 1
                print(f"Player hit! Lives left: {player.lives}")

                if player.lives <= 0:
                    print("Game over!")
                    return
                else:
                    # Respawn in the center and give brief invulnerability
                    player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    # Avoid multiple hits in the same frame
                    break
            
            for bullet in shots:
                if asteroid.collide(bullet):
                    if asteroid.radius > ASTEROID_MIN_RADIUS:
                      asteroid.split()
                    
                    asteroid.kill()
                    bullet.kill()
                    
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")


