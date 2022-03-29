from game import Game
import pygame
import Constants

def main():
    pygame.init()
    running = True
    size = [Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    game = Game(screen) 
    clock = pygame.time.Clock()
            
    while running:            
        #Update object positions, check for collisions, edge of screen etc
        game.run_logic()
        
        #Process events (Keystrokes, mouse clicks, etc.)
        running = game.process_events()
    
        #Draw current frame
        running = game.display_frame(screen)
    
        #Pause for next frame
        clock.tick(60)
    
    pygame.quit()
    
#Call main function start
if __name__ == "__main__":
    main()
    