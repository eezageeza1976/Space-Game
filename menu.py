#Main menu class
import pygame as pg
import Constants

class Menu():
    def __init__(self, screen):
        self.frame_rect = 0        
        self.menu_img = pg.image.load('graphics/main_menu.bmp').convert()
        
        self.menu_bg = pg.image.load('graphics/bg5.bmp').convert()
        self.menu_bg = pg.transform.scale(self.menu_bg, screen.get_size())
        
        self.screen = screen
        self.menu_running = True
        
        self.button_frames = []
        self.button_frames.append(self.menu_img.subsurface(pg.Rect(  20,  20, 260, 65)))
        self.button_frames.append(self.menu_img.subsurface(pg.Rect(  20,  215, 260, 65)))
        
        self.button_list = [Constants.NEW_GAME_BUTTON, Constants.QUIT_GAME_BUTTON]
        
    def display_frame(self):
        self.screen.blit(self.menu_bg, (0, 0))
        
        for i in range(2):
            self.frame_rect = self.button_frames[i].get_rect(center=self.button_list[i])
            
            if self.collision(self.frame_rect):
                self.button_frames[i].set_alpha(190)
            else:
                self.button_frames[i].set_alpha(255)
            
            self.screen.blit(self.button_frames[i], self.frame_rect)
            
        pg.display.flip()
        
    def update(self):
        return
    
    def process_events(self):     
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return pg.QUIT
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return pg.K_ESCAPE
            elif event.type == pg.MOUSEBUTTONDOWN:
                return pg.MOUSEBUTTONDOWN
                
        return self.menu_running
    
    
    def collision(self, rect):
        if rect.collidepoint(pg.mouse.get_pos()):
            return True

    def check_button(self):
        for i in range(2):          
            self.frame_rect = self.button_frames[i].get_rect(center=self.button_list[i])
            
            if self.frame_rect.collidepoint(pg.mouse.get_pos()) and self.button_list[i] == Constants.NEW_GAME_BUTTON:
                return 1
            elif self.frame_rect.collidepoint(pg.mouse.get_pos()) and self.button_list[i] == Constants.QUIT_GAME_BUTTON:
                return 2


        
        
        
        
        
        
        