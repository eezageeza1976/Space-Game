#Don't forget to add CONSTANTS file
import pygame as pg
import Constants
from menu import Menu
from sprite import Block
from sprite import Player
from sprite import Star
import random


class Game():
    def __init__(self, screen):
        #Set up game initialisation code here
        self.is_running = True
        self.game_over = False
        self.menu_running = True
        self.key_pressed = 0
        self.block_pos = ((random.randrange(50, 1100)), (random.randrange(10, 950)))
        self.surf = screen
        
        self.block_list = pg.sprite.Group()
        self.star_list = pg.sprite.Group()
        self.all_sprite_list = pg.sprite.Group()

        self.bg_img = pg.image.load('graphics/space1.bmp').convert()
        self.bg_img = pg.transform.scale(self.bg_img, screen.get_size())
        
        self.spritesheet = pg.image.load('graphics/spritesheet_explosion.bmp').convert()
        self.spritesheet.set_colorkey(Constants.BLACK)
        self.frames = []
        
        for i in range(4):
            x = 0
            for j in range(4):
                y = i * 64
                x = j * 64
                self.frames.append(self.spritesheet.subsurface(pg.Rect(  x,  y, 64, 64)))
                x = 0
        
        self.menu = Menu(self.surf)
        
        self.fps = pg.time.Clock()
        
        #Create an instances of Block class
        for i in range(4):
            self.block = Block(self.block_pos)
            
            self.block_pos = ((random.randrange(0, 1200)), (random.randrange(0, 980)))
            #Add Block to sprite list
            self.block_list.add(self.block)
            self.all_sprite_list.add(self.block)
        
        #Create an instances of Star class
        for i in range(4):
            self.star = Star((random.randrange(Constants.SCREEN_WIDTH), random.randrange(Constants.SCREEN_HEIGHT)))            
            #Add Star to sprite list
            self.star_list.add(self.star)
            self.all_sprite_list.add(self.star)
            
            
        #create and add player to all_sprite_list
        self.player = Player(Constants.PLAYER_START, self.surf)
        self.all_sprite_list.add(self.player)

        self.frame_rect = self.frames[0].get_rect(center=self.player.pos) #shows what frame to be displayed first
    
#Game event actions in here
#Keyboard/mouse presses presses
    def process_events(self):     
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
                return self.is_running
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                    return self.is_running
                if event.key == pg.K_n:
                    if self.game_over:
                        self.__init__(self.surf)
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.player.thrust_animation = True
            elif event.type == pg.MOUSEBUTTONUP:
                self.player.thrust_animation = False
                
        return self.is_running
    
#movement processing etc               
    def run_logic(self):
        self.collision()
        self.all_sprite_list.update()
        self.check_score()
        
        
#drawing screen and sprites etc.        
    def display_frame(self, screen):
        
        while self.menu_running:
            self.menu.display_frame()
            self.key_pressed = self.menu.process_events()
            
            if self.key_pressed == pg.K_ESCAPE:
                print("ESCAPE")
                self.is_running = False
                return self.is_running
            elif self.key_pressed == pg.MOUSEBUTTONDOWN:
                
                button = self.menu.check_button()
                if button == 1:
                    self.menu_running = False
                elif button == 2:
                    self.is_running = False
                    return self.is_running
        
        
        if self.game_over:
            number_of_frames = len(self.frames)
            self.is_running = False
            for i in range(number_of_frames):
                self.frame_rect = self.frames[0].get_rect(center=self.player.pos)
                
                screen.blit(self.bg_img,(0,0))
                self.drawscore()
                self.all_sprite_list.draw(screen)
                screen.blit(self.frames[i], self.frame_rect)

                pg.display.flip()

                self.fps.tick(50)
            return self.is_running
        else:    
            screen.blit(self.bg_img,(0,0))
            self.drawscore()
            self.all_sprite_list.draw(screen)
        
        pg.display.flip()
        return self.is_running
    
    def drawscore(self):
        font = pg.font.SysFont("serif", 25)
        text = font.render(("Player Score: " + str(self.player.star_count)), True, Constants.RED)
        center_x = (1040) - (text.get_width() // 2)
        center_y = (20) - (text.get_height() // 2)
        self.surf.blit(text, [center_x, center_y])
        
    def collision(self):
        #Check if play crashes into any blocks using mask
        for block in self.block_list:            
            if pg.sprite.collide_mask(self.player, block):
                #kill player and set game_over True
                self.player.kill()
                self.game_over = True
        
        #Check play has collected a star, if so remove star from star_list
        for star in self.star_list:
            if pg.sprite.collide_mask(self.player, star):
                star.remove(self.star_list, self.all_sprite_list)
                self.player.star_count += 1
            
            
    def check_score(self):
        if len(self.star_list.sprites()) == 0:
            print("IN")
            self.surf.blit(self.bg_img,(0,0))
            self.fps.tick(500)
#             font = pg.font.SysFont("serif", 25)
#             text = font.render(("Level Complete"), True, Constants.RED)
#             center_x = (1040) - (text.get_width() // 2)
#             center_y = (20) - (text.get_height() // 2)
            
#             self.surf.blit(text, (Constants.SCREEN_W_CENTRE, Constants.SCREEN_H_CENTRE))

            
        
        
        
        
        
        